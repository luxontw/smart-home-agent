import json
import logging
import os
import queue
import threading
import time

import pyzenbo.modules.error_code as error_code
import pyzenbo.modules.zenbo_command as commands
from pyzenbo.modules.socket_state_machine import (SOCKET_STATE, SOCKET_TYPE,
                                                  SocketStateMachine,
                                                  file_transfer_process)

logger = logging.getLogger('pyzenbo')

DESTINATION = {
    'commander': 1,
    'coordinator': 2,
    'vision': 3,
    'system': 4,
    'sensor': 5,
    'media': 6,
}
STATE = {
    0: 'INITIAL',
    1: 'PENDING',
    2: 'REJECTED',
    3: 'ACTIVE',
    4: 'FAILED',
    5: 'SUCCEED',
    6: 'PREEMPTED',
}
_serial = 0


def init_common(cmd, _hash=0, priority=2, pid=os.getpid(), user=""):
    return Common(**{
        "hash": _hash,
        "cmd": cmd,
        "priority": priority,
        "pid": pid,
        "user": user,
    })


def get_packet(des, cmd, data):
    common = init_common(cmd)
    return json.dumps({
        'TYPE': des,
        'COMMON': common.get_json(),
        'DATA': json.dumps(data)
    }), common.get_serial()


class Common:
    """docstring for Common()"""

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.kwargs.setdefault("hash", 0)
        self.kwargs.setdefault("pid", os.getpid())
        self.kwargs.setdefault("user", "")
        self.kwargs.setdefault("priority", 2)
        self.kwargs.setdefault("version", 0)
        self.kwargs.setdefault("ignoreIdle", False)
        self.kwargs.setdefault("ignorePreempted", False)

    @staticmethod
    def _get_serial():
        global _serial
        _serial += 1
        return _serial

    def get_serial(self):
        return self.kwargs['serial']

    def get_json(self):
        self.kwargs["serial"] = self._get_serial()
        return json.dumps(self.kwargs)


class InterComm:
    """docstring for _InterComm"""

    _on_state_change_callback_lock = threading.RLock()
    _on_result_callback_lock = threading.RLock()
    _listen_callback_lock = threading.RLock()
    _vision_callback_lock = threading.RLock()
    _on_state_change_callback = None
    _on_result_callback = None
    _listen_callback = None
    _vision_callback = None
    _destination = None
    _timeout = None
    skt = None
    _cb_receiver = None
    _cb_executor = None
    _sender = None
    _receiver = None
    _callback_switch = None
    _callback_sync = {}
    _callback_sync_error = {}
    _cancel_by_timeout = False
    _released = False

    def init(self,
             destination,
             on_state_change_callback,
             on_result_callback,
             timeout=2):
        self.on_state_change_callback = on_state_change_callback
        self.on_result_callback = on_result_callback
        self.listen_callback = None
        self.on_vision_callback = None
        self._destination = destination
        self._timeout = timeout
        self._cb_receiver = ExternalInterfacing(self._callback_receive_handler)
        self._cb_executor = ExternalInterfacing(self._callback_execute_handler)
        self.skt = SocketStateMachine(destination, timeout)
        ready = threading.Barrier(2)
        self._sender = ExternalSender(self.skt.get_socket(SOCKET_TYPE['Send']),
                                      ready, self.reconnect)
        self._receiver = ExternalReceiver(
            self.skt.get_socket(SOCKET_TYPE['Receive']), ready,
            self._cb_receiver.request, self.reconnect,
            self._send_alive_response)
        self._callback_switch = {
            1: self._callback_on_result_handler,
            2: self._callback_on_state_change_handler,
            3: self._callback_on_listen_handler,
            4: self._callback_on_vision_handler,
        }

    @property
    def on_state_change_callback(self):
        with self._on_state_change_callback_lock:
            return self._on_state_change_callback

    @on_state_change_callback.setter
    def on_state_change_callback(self, callback_fun):
        with self._on_state_change_callback_lock:
            self._on_state_change_callback = callback_fun

    @on_state_change_callback.deleter
    def on_state_change_callback(self):
        with self._on_state_change_callback_lock:
            self._on_state_change_callback = None

    @property
    def on_result_callback(self):
        with self._on_result_callback_lock:
            return self._on_result_callback

    @on_result_callback.setter
    def on_result_callback(self, callback_fun):
        with self._on_result_callback_lock:
            self._on_result_callback = callback_fun

    @on_result_callback.deleter
    def on_result_callback(self):
        with self._on_result_callback_lock:
            self._on_result_callback = None

    @property
    def listen_callback(self):
        return self._listen_callback

    @listen_callback.setter
    def listen_callback(self, callback_fun):
        with self._listen_callback_lock:
            self._listen_callback = callback_fun

    @listen_callback.deleter
    def listen_callback(self):
        with self._listen_callback_lock:
            del self._listen_callback

    @property
    def on_vision_callback(self):
        return self._vision_callback

    @on_vision_callback.setter
    def on_vision_callback(self, callback_fun):
        with self._vision_callback_lock:
            self._vision_callback = callback_fun

    @on_vision_callback.deleter
    def on_vision_callback(self):
        with self._vision_callback_lock:
            del self._vision_callback

    def reconnect(self):
        if self._released:
            logger.info('Already released, ignore reconnection.')
            return
        logger.info('Reconnect...')
        self.skt.set_state(SOCKET_TYPE['Send'], SOCKET_STATE['Disconnected'])
        self.skt.set_state(SOCKET_TYPE['Receive'],
                           SOCKET_STATE['Disconnected'])
        self._sender.stop()
        self._receiver.stop()
        self.skt.release()
        self.skt = SocketStateMachine(self._destination, self._timeout)
        if self.skt.get_socket(SOCKET_TYPE['Receive']) is None:
            logger.error('Socket reconnect failed')
            self._send_failed_to_waiting_command()
            return
        ready = threading.Barrier(2)
        self._sender = ExternalSender(self.skt.get_socket(SOCKET_TYPE['Send']),
                                      ready, self.reconnect)
        self._receiver = ExternalReceiver(
            self.skt.get_socket(SOCKET_TYPE['Receive']), ready,
            self._cb_receiver.request, self.reconnect,
            self._send_alive_response)

    def release(self):
        self._send_failed_to_waiting_command()
        del self.on_state_change_callback
        del self.on_result_callback
        self._released = True
        self._cancel_by_serial(0)
        logger.info('Cancel all completed')
        self._sender.stop()
        self._receiver.stop()
        self.skt.release()

    def send_command(self, des, cmd, data, sync=False, timeout=None):
        packet, serial = get_packet(des, cmd, data)

        if self._released and cmd != commands.CANCEL:
            # after release only cancel command is allowed
            logger.error(
                'send_command: reject command when releasing. serial:%d, cmd:%d',
                serial, cmd)
            if self.on_state_change_callback:
                self.on_state_change_callback(serial, cmd,
                                              error_code.COMMON_SOCKET_FAIL, 2)
            return serial, None

        if self.skt.get_state(SOCKET_TYPE['Send']) != SOCKET_STATE['Connected']:
            logger.error(
                'send_command: sender not connected. serial:%d, cmd:%d', serial,
                cmd)
            if self.on_state_change_callback:
                self.on_state_change_callback(serial, cmd,
                                              error_code.COMMON_SOCKET_FAIL, 2)
            return serial, None

        event = None
        if sync:
            event = threading.Event()
            self._callback_sync[serial] = (event, cmd)

        self._sender.request(packet)
        if sync:
            logger.info('Waiting serial:%d command execute completed', serial)

            if not event.wait(timeout):
                logger.info('Sync timeout, cancel command by serial:%d, cmd:%d',
                            serial, cmd)
                if not self._cancel_by_timeout:
                    self._cancel_by_timeout = True
                    self._cancel_command(serial, cmd)
                self._cancel_by_timeout = False
            logger.info('Serial:%d execute completed', serial)
            return serial, self._callback_sync_error.get(serial, None)
        else:
            return serial, None

    def file_transfer(self, target_file, over_write):
        return file_transfer_process(self._destination[0], target_file,
                                     over_write)

    def _send_alive_response(self):
        self._sender.request("KEEP_ALIVE_ACK")

    def _callback_receive_handler(self, *args):
        # logger.debug('Receive:%s', args[0])
        try:
            recv = json.loads(args[0])
        except Exception as e:
            logger.error('Exception: %s', args)
            raise e
        callback_type = recv.get("TYPE")
        if callback_type == 2:
            self._on_state_change_sync_handler(recv)
        self._cb_executor.request(recv)

    def _callback_execute_handler(self, kwargs):
        callback_type = kwargs.get("TYPE")
        self._callback_switch[callback_type](kwargs)

    def _on_state_change_sync_handler(self, kwargs):
        serial = kwargs.get("SERIAL", None)
        cmd = kwargs.get('CMD', None)
        error = kwargs.get("ERROR", None)
        state = kwargs.get("STATE", None)
        logger.debug('_onStateChange serial:%d, cmd:%d, error:%d, state:%s',
                     serial, cmd, error, STATE[state])
        if self._callback_sync.get(serial) and (1 < state <= 6 and state != 3):
            self._callback_sync_error[serial] = {
                'state': state,
                'error': error,
            }
            self._callback_sync.pop(serial)[0].set()

    def _callback_on_state_change_handler(self, kwargs):
        serial = kwargs.get("SERIAL", None)
        cmd = kwargs.get('CMD', None)
        error = kwargs.get("ERROR", None)
        state = kwargs.get("STATE", None)
        if self.on_state_change_callback:
            self.on_state_change_callback(serial=serial,
                                          cmd=cmd,
                                          error=error,
                                          state=state)

    def _callback_on_result_handler(self, kwargs):
        serial = kwargs.get("SERIAL", None)
        cmd = kwargs.get('CMD', None)
        error = kwargs.get("ERROR", None)
        result = kwargs.get('RESULT', None)
        logger.debug('_onResult serial:%d, cmd:%d error:%d, result:%s', serial,
                     cmd, error, result)
        if self.on_result_callback:
            self.on_result_callback(serial=serial,
                                    cmd=cmd,
                                    error=error,
                                    result=result)

    def _callback_on_listen_handler(self, kwargs):
        result = kwargs.get('RESULT', None)
        # logger.debug('_on_listen_handler:%s', result)
        if self.listen_callback:
            self.listen_callback(result)

    def _callback_on_vision_handler(self, kwargs):
        result = kwargs.get('RESULT', None)
        # logger.debug('_on_vision_handler:%s', result)
        if self.on_vision_callback:
            self.on_vision_callback(result)

    def _cancel_command(self, serial, cmd):
        args = {
            commands.VISION_REQUEST_DETECT_FACE: (
                DESTINATION["vision"],
                commands.VISION_CANCEL_DETECT_FACE,
            ),
            commands.VISION_REQUEST_DETECT_PERSON: (
                DESTINATION["vision"],
                commands.VISION_CANCEL_DETECT_PERSON,
            ),
            commands.VISION_REQUEST_RECOGNIZE_PERSON: (
                DESTINATION["vision"],
                commands.VISION_CANCEL_RECOGNIZE_PERSON,
            ),
        }.get(cmd, serial)

        {
            commands.VISION_REQUEST_DETECT_FACE: self._cancel_by_cmd,
            commands.VISION_REQUEST_DETECT_PERSON: self._cancel_by_cmd,
            commands.VISION_REQUEST_RECOGNIZE_PERSON: self._cancel_by_cmd,
        }.get(cmd, self._cancel_by_serial)(args)

    def _cancel_by_cmd(self, args, sync=False, timeout=None):
        des, cmd = args
        data = {}
        serial, error = self.send_command(des, cmd, data, sync, timeout)
        return serial, error

    def _cancel_by_serial(self, serial, sync=True, timeout=5):
        des = DESTINATION["coordinator"]
        cmd = commands.CANCEL
        data = {
            'command': 0,
            'target_id': int(serial),
        }
        serial, error = self.send_command(des, cmd, data, sync, timeout)
        return serial, error

    def _send_failed_to_waiting_command(self):
        while len(self._callback_sync):
            serial, item = self._callback_sync.popitem()
            self._callback_sync_error[serial] = {
                'state': 2,
                'error': error_code.COMMON_SOCKET_FAIL,
            }
            event, cmd = item
            logger.debug('serial:%d command:%s change state to failed', serial,
                         cmd)
            event.set()
            if self.on_state_change_callback:
                self.on_state_change_callback(serial, cmd,
                                              error_code.COMMON_SOCKET_FAIL, 2)


class ExternalSender(threading.Thread):
    """ """

    def __init__(self, skt, ready, recover_fun, **kwargs):
        super().__init__(**kwargs)
        self.setName('ExternalSender')
        self.daemon = True
        self.sock = skt
        # self.sock = socket.create_connection(destination, timeout)
        # self.destination = destination
        # self.timeout = timeout
        self._recover_fun = recover_fun
        self._ready = ready
        self.work_request_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.start()

    def stop(self):
        self.work_request_queue.put(None)
        if self.sock:
            self.sock.close()

    def request(self, *args, **kwargs):
        """ call from other thread """
        self.work_request_queue.put((args, kwargs))
        return self.result_queue.get()

    def run(self):
        self._ready.wait()
        del self._ready
        if self.sock is None:
            logger.warning('Sender socket connect failed')
            return
        logger.info('ExternalSender %s', self.sock)
        while True:
            # a, k = self.work_request_queue.get()
            item = self.work_request_queue.get()
            if item is None:
                break
            a, k = item
            try:
                self.result_queue.put(self._send_message(self.sock, *a, **k))
            except ConnectionResetError:
                logger.info('Server reset connection. Reconnect to server.')
                self.result_queue.put(None)
                self._recover_fun()
            self.work_request_queue.task_done()
        logger.info('ExternalSender stop')

    @staticmethod
    def _send_message(sock, packet):
        if packet != "KEEP_ALIVE_ACK":
            logger.info('Send command')
        logger.debug(packet)
        try:
            sock.sendall(packet.encode(encoding='utf-8'))
            sock.sendall('\n'.encode(encoding='utf-8'))
        except Exception as e:
            raise e
        # else:
        #     logger.info('Send message Done')


class ExternalReceiver(threading.Thread):
    """"""

    def __init__(self, skt, ready, external_callable, recover_fun,
                 send_alive_response, **kwargs):
        super().__init__(**kwargs)
        self.setName('ExternalReceiver')
        self.daemon = True
        self.sock = skt
        self._recover_fun = recover_fun
        self._send_alive_response = send_alive_response
        # self.sock = socket.create_connection(destination, timeout)
        # self.destination = destination
        # self.timeout = timeout
        self._ready = ready
        self._external_callable = external_callable
        self._stop_event = threading.Event()
        self.start()

    def stop(self):
        self._stop_event.set()
        if self.sock:
            self.sock.close()
        logger.info('ExternalReceiver stop')

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        self._ready.wait()
        del self._ready
        if self.sock is None:
            logger.warning('Receiver socket connect failed')
            return
        logger.info('Ready receive message from %s', self.sock)
        if_disconnect = False
        buf_size = 4096
        remaining_data = []
        while not self.stopped():
            try:
                if self.sock:
                    received = self.sock.recv(buf_size).decode('utf-8',
                                                               errors='replace')
                else:
                    time.sleep(0.5)
                    received = ''
            except ConnectionAbortedError as e:
                # ignore
                logger.warning(e)
                break
            except OSError:
                if not self.stopped():
                    logger.error('Receiver not stopped')
                    raise
            except Exception:
                raise
            else:
                if not self.sock:
                    continue
                if not len(received):
                    if_disconnect = True
                    if self.stopped():
                        logger.info('Receiver stopped')
                        break
                    logger.warning('Receiver disconnected recover it')
                    self._recover_fun()
                    break
                else:
                    if len(remaining_data):
                        remaining_data.append(received)
                        received = ''.join(remaining_data)
                        # logger.debug('remaining_data %s' remaining_data)
                        remaining_data.clear()
                    end = received.rfind('\n')
                    # '\n' not in received string end, i.e. not received full
                    # packet, only use completed packet, store not end packet
                    # in remaining date for next time receive data.
                    if end != len(received) - 1:
                        remaining_data.append(received[end + 1:])
                        # logger.debug(
                        #     'len > buf size, end:%d, len:%d, size:%d, received:%s, remaining:%s ',
                        #     end, len(received), sys.getsizeof(received),
                        #     received, remaining_data)
                        continue
                    recv = received[0:end].splitlines()
                    [
                        self._send_alive_response() if 'KEEP_ALIVE_PROBE' == s
                        else self._external_callable(s)
                        for s in recv
                        if len(s) > 0
                    ]
        if not if_disconnect:
            logger.info('Receive message canceled')


class ExternalInterfacing(threading.Thread):
    """ """

    def __init__(self, external_callable, **kwargs):
        super().__init__(**kwargs)
        self.setName('ExternalInterfacing')
        self.daemon = True
        self.external_callable = external_callable
        self.work_request_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.start()

    def request(self, *args, **kwargs):
        """ call from other thread """
        self.work_request_queue.put((args, kwargs))
        # return self.result_queue.get()

    def run(self):
        while True:
            a, k = self.work_request_queue.get()
            self.result_queue.put(self.external_callable(*a, **k))
            # self.work_request_queue.task_done()


class Serializer(threading.Thread):
    """ """

    def __init__(self, **kwargs):
        threading.Thread.__init__(self, **kwargs)
        self.demon = True
        self.work_request_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.start()

    def apply(self, external_callable, *args, **kwargs):
        """ call from other thread """
        self.work_request_queue.put((external_callable, args, kwargs))
        return self.result_queue.get()

    def run(self):
        while True:
            external_callable, args, kwargs = self.work_request_queue.get()
            self.result_queue.put(external_callable(*args, **kwargs))
            self.work_request_queue.task_done()
