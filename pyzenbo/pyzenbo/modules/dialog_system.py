import logging

import pyzenbo.modules.zenbo_command as commands
from pyzenbo.modules.inter_communication import DESTINATION
from pyzenbo.modules.wait_for import WaitForListen, WaitForListenDoa

logger = logging.getLogger('pyzenbo')


class RobotFace:
    """Face expression ID."""

    HIDEFACE = 'HIDEFACE'
    INTERESTED = 'INTERESTED'
    DOUBTING = 'DOUBTING'
    PROUD = 'PROUD'
    DEFAULT = 'DEFAULT'
    HAPPY = 'HAPPY'
    EXPECTING = 'EXPECTING'
    SHOCKED = 'SHOCKED'
    QUESTIONING = 'QUESTIONING'
    IMPATIENT = 'IMPATIENT'
    CONFIDENT = 'CONFIDENT'
    ACTIVE = 'ACTIVE'
    PLEASED = 'PLEASED'
    HELPLESS = 'HELPLESS'
    SERIOUS = 'SERIOUS'
    WORRIED = 'WORRIED'
    PRETENDING = 'PRETENDING'
    LAZY = 'LAZY'
    AWARE_RIGHT = 'AWARE_RIGHT'
    TIRED = 'TIRED'
    SHY = 'SHY'
    INNOCENT = 'INNOCENT'
    SINGING = 'SINGING'
    AWARE_LEFT = 'AWARE_LEFT'
    DEFAULT_STILL = 'DEFAULT_STILL'
    PREVIOUS = 'PREVIOUS'
    EXPECTING_ADV = 'EXPECTING_ADV'
    IMPATIENT_ADV = 'IMPATIENT_ADV'
    PLEASED_ADV = 'PLEASED_ADV'
    SHOCKED_ADV = 'SHOCKED_ADV'
    TIRED_ADV = 'TIRED_ADV'
    DEFAULT_ADV = 'DEFAULT_ADV'
    WORRIED_ADV = 'WORRIED_ADV'
    QUESTIONING_ADV = 'QUESTIONING_ADV'
    PRETENDING_ADV = 'PRETENDING_ADV'
    INTERESTED_ADV = 'INTERESTED_ADV'
    SHY_ADV = 'SHY_ADV'
    CONFIDENT_ADV = 'CONFIDENT_ADV'
    HAPPY_ADV = 'HAPPY_ADV'
    LAZY_ADV = 'LAZY_ADV'
    ACTIVE_ADV = 'ACTIVE_ADV'
    SINGING_ADV = 'SINGING_ADV'
    DOUBTING_ADV = 'DOUBTING_ADV'
    AWARE_RIGHT_ADV = 'AWARE_RIGHT_ADV'
    AWARE_LEFT_ADV = 'AWARE_LEFT_ADV'
    HELPLESS_ADV = 'HELPLESS_ADV'
    SERIOUS_ADV = 'SERIOUS_ADV'
    INNOCENT_ADV = 'INNOCENT_ADV'
    PROUD_ADV = 'PROUD_ADV'


class DynamicEditAction:
    ADD_NEW_INSTANCE = "addNewInstance"
    UPDATE_NEW_INSTANCE = "updateNewInstance"
    DELETE_INSTANCE = "deleteInstance"


class LanguageType:
    ZH_TW = 1
    EN_US = 2
    ZH_CN = 3
    JP = 4
    HK = 7
    DE = 8
    FR = 9
    ES = 10
    PT = 11
    NL = 12


class DialogSystem:
    """contain of pyzenbo.robot attribute"""

    def __init__(self, inter_comm):
        self._inter_comm = inter_comm

    def register_listen_callback(self, domain, listen, sync=True, timeout=None):
        """
        Register the listen callback functions for Dialog System.

        .. code-block:: python
            :caption: Usage

            def listen_callback(args):
                utterance = args.get('event_user_utterance', None)
                vad = args.get('event_vad_status', None)
                slu = args.get('event_slu_query', None)
                msg = 'listen uu:{}, vad:{}, slu:{}'
                print(msg.format(utterance, vad, slu))
                if not utterance and not vad and not slu:
                    print('listen raw:{}'.format(args))
                result = parser_listen_result(slu)
                if result is not None:
                    print('slu_result:{}'.format(result))

            sdk = pyzenbo.connect(host_ip)
            sdk.robot.register_listen_callback(domain, listen_callback)

        :param domain: domain UUID
        :param listen: listen callback function
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        self._inter_comm.listen_callback = listen
        des = DESTINATION["system"]
        cmd = commands.DS_SERVICE_CONNECT
        data = {'domain': str(domain)}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def unregister_listen_callback(self, sync=True, timeout=None):
        """
        Unregister listen callback.

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.unregister_listen_callback()

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        del self._inter_comm.listen_callback
        des = DESTINATION["system"]
        cmd = commands.DS_SERVICE_RELEASE
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def speak(self, sentence, config=None, sync=True, timeout=None):
        """
        Start speaking.

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.speak("hello world")

        :param sentence: sentence of text to speech
        :param config: configuration for speak engine
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.SPEAK
        data = {
            'tts': str(sentence),
            'type': 11,
        }
        if config is None:
            config = {}

        data['speed'] = config.get('speed', -1)
        data['pitch'] = config.get('pitch', -1)
        data['volume'] = config.get('volume', -1)
        data['waitFactor'] = config.get('waitFactor', -1)
        data['readMode'] = config.get('readMode', -1)
        data['languageId'] = config.get('languageId', -1)

        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def stop_speak(self, sync=True, timeout=None):
        """
        Stop speaking.

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.stop_speak()

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.STOP_SPEAK
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def set_expression(self,
                       facial,
                       sentence=None,
                       config=None,
                       sync=True,
                       timeout=None):
        """
        Make robot expression and speak.

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.set_expression(RobotFace.PROUD, 'Hello World')

        :param facial: robot face expression ID: HIDEFACE, INTERESTED,
            DOUBTING, PROUD, DEFAULT, HAPPY, EXPECTING, SHOCKED, QUESTIONING,
            IMPATIENT, CONFIDENT, ACTIVE, PLEASED, HELPLESS, SERIOUS, WORRIED,
            PRETENDING, LAZY, AWARE_RIGHT, TIRED, SHY, INNOCENT, SINGING,
            AWARE_LEFT, DEFAULT_STILL, PREVIOUS
        :param sentence: sentence of text to speech
        :param config: configuration for expression engine
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.SET_EXPRESSION

        data = {
            'face': str(facial),
            'type': 11,
        }
        if sentence is not None:
            data['tts'] = str(sentence)
        if config is None:
            config = {}

        data['speed'] = config.get('speed', -1)
        data['pitch'] = config.get('pitch', -1)
        data['volume'] = config.get('volume', -1)
        data['waitFactor'] = config.get('waitFactor', -1)
        data['readMode'] = config.get('readMode', -1)
        data['languageId'] = config.get('languageId', -1)

        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def query_expression_status(self, sync=True, timeout=None):
        """
        Query expression status,
        return result in onResult callback,
        result will have an JSON string, key is "RESULT".
        JSON object have two element, FaceID and FaceExit. FaceID is current
        face value, and FaceExit is an boolean True is currently have
        display expression.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.QUERY_EXPRESSION_STATUS
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def clear_app_context(self, domain, sync=True, timeout=None):
        """
        Clear specific domain UUID in current dialog system stack.
        pyzenbo.robot.clear_app_context

        :param domain: domain UUID
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_CLEAR_APP_CONTEXT
        data = {'domain': str(domain), 'type': 1}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def clear_background_context(self, domain, sync=True, timeout=None):
        """
        Clear background context.

        :param domain: domain UUID
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_CLEAR_BACKGROUND_CONTEXT
        data = {'domain': str(domain), 'type': 10}
        # cmd.type and cmd.context is not used
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def dynamic_edit_instance(self,
                              domain,
                              action,
                              entity,
                              instances,
                              sync=True,
                              timeout=None):
        """
        Add/Delete/Update user defined instances of an specific Entity.

        :param domain: domain UUID
        :param action: types of action
        :param entity: the existed entity added on the Concept page of DS
            Editor
        :param instances: the instances to be modified
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_DYNAMIC_EDIT_INSTANCE
        data = {
            'domain': str(domain),
            'action': str(action),
            'entity': str(entity),
            'instances': {
                'values': instances
            },
        }
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def jump_to_plan(self,
                     domain,
                     plan,
                     cross_intent=None,
                     sync=True,
                     timeout=None):
        """
        Let dialog state switch to specific plan, and
        set output context of this plan on top of the context stack.

        :param domain: domain UUID
        :param plan:  plan ID to be switched to
        :param cross_intent: set True to enable cross intent
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        cmd = commands.DS_JUMP_TO_PLAN
        des = DESTINATION["commander"]
        if cross_intent is None:
            cross_intent = 0
        else:
            cross_intent = 1 if bool(cross_intent) else -1

        data = {
            'domain': str(domain),
            'context': str(plan),
            'type': int(cross_intent)
        }
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def set_background_context(self, domain, plan, sync=True, timeout=None):
        """
        Set background context.

        :param domain: domain UUID
        :param plan: plan ID
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_SET_BACKGROUND_CONTEXT
        data = {'domain': str(domain), 'plan': str(plan), 'type': 10}
        # type is not used
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def set_voice_trigger(self, enable, sync=True, timeout=None):
        """
        Set dialog system voice trigger.

        :param enable: flag to enable/disable dialog system voice trigger
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_VOICE_TRIGGER
        data = {'enable': bool(enable)}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def reset_voice_trigger(self, enable, sync=True, timeout=None):
        """
        Reset dialog system voice trigger counter and force voice trigger
        enable or disable.

        :param enable: flag to enable/disable dialog system voice trigger
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_VOICE_TRIGGER
        data = {'enable': bool(enable), 'resetType': 2}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def reset_voice_trigger_to_default(self, sync=True, timeout=None):
        """
        Reset dialog system voice trigger to default setting.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_VOICE_TRIGGER
        data = {'enable': True, 'resetType': 1}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def set_listen_context(self, domain, context, sync=True, timeout=None):
        """
        Force Dialog System to listen specific context in the DS Editor

        :param domain: domain UUID
        :param context: context to listen to
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_SET_LISTEN_CONTEXT
        data = {'domain': domain, 'context': context, 'type': 0}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def speak_and_listen(self, sentence, config=None, sync=True, timeout=None):
        """
        Start speaking and listening.
        If sentence is an empty string (""), Zenbo will listen directly.

        :param sentence: sentence sentence of text to speech
        :param config: configuration for speak engine
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_SPEAK_AND_LISTEN
        data = {
            'tts': str(sentence),
            'type': 11,
        }
        if config is None:
            config = {}
        data['timeout'] = config.get('timeout', -1)
        data['retry'] = config.get('retry', -1)
        data['speed'] = config.get('speed', -1)
        data['pitch'] = config.get('pitch', -1)
        data['volume'] = config.get('volume', -1)
        data['waitFactor'] = config.get('waitFactor', -1)
        data['readMode'] = config.get('readMode', -1)
        data['languageId'] = config.get('languageId', -1)
        data['listenLanguageId'] = config.get('listenLanguageId', -1)
        data['domain'] = config.get('domain', None)
        data['context'] = config.get('context', None)
        data['domainList'] = config.get('domainList', None)
        data['alwaysListenState'] = config.get('alwaysListenState', -1)
        data['listenCurrentDomain'] = config.get('listenCurrentDomain', False)
        data['displayListenAnimation'] = config.get('displayListenAnimation',
                                                    True)

        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def stop_speak_and_listen(self, sync=True, timeout=None):
        """
        Stop speak and listen.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_STOP_SPEAK_AND_LISTEN
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def update_dialog_corpus_by_server(self,
                                       domain,
                                       package_name,
                                       version,
                                       sync=True,
                                       timeout=None):
        """
        Automatic compare corpus data version while call the API and
        will trigger command set update process if needed.

        :param domain: domain UUID string
        :param package_name: package name on DDE
        :param version: version string
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_UPDATE_CORPUS_BY_SERVER
        data = {
            'domain': domain,
            'packageName': package_name,
            'version': version,
        }
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def query_word_similarity(self,
                              input_sentence,
                              target_sentence,
                              sync=True,
                              timeout=None):
        """
        Query word similarity between input and target sentences and get data from onResult callback, result bundle will have an JSON string, key is "RESULT".
        JSON object have three element, input_sentence, target_sentence and similarity.

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.query_word_similarity(input_sentence='who are you',
                                    target_sentence=['who are you', 'where are you'])

        RESULT: '{"input_sentence":"who are you","target_sentence":["who are you","where are you"],
        "similarity":[{"who are you":1.01},{"where are you":0.57}]}'}

        :param input_sentence: input sentence
        :param target_sentence: array for target sentence
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_WORD_SIMILARITY
        data = {
            'inputSentence': input_sentence,
            'targetSentence': target_sentence
        }
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def zh_to_number(self, input_sentence, sync=True, timeout=None):
        """
        Transform ZH to number for inputSentence and get data from onResult callback, result bundle will have an JSON string, key is "RESULT".
        Example: {"input_sentence":"轉換數字一二三四","result":"1234"}

        :param input_sentence: input sentence
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_ZH_TO_NUMBER
        data = {'inputSentence': input_sentence}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def en_to_number(self, input_sentence, sync=True, timeout=None):
        """
        Transform EN to number for inputSentence and get data from onResult callback, result bundle will have an JSON string, key is "RESULT".
        Example: {"input_sentence":"transform one thousand four hundred and fifty","result":"1450"}

        :param input_sentence: input sentence
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_EN_TO_NUMBER
        data = {'inputSentence': input_sentence}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def config_next_csr(self,
                        language_type,
                        disable_slu,
                        sync=True,
                        timeout=None):
        """
        Config next CSR setting. Include HeyZenbo trigger and speakAndListen API.

        :param language_type: LanguageType.ZH_TW, LanguageType.EN_US or LanguageType.ZH_CN, etc..
        :param disable_slu: Disable SLU report and skip questioning expression
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["commander"]
        cmd = commands.DS_CONFIG_NEXT_CSR
        data = {
            'languageType': int(language_type),
            'disableSLU': bool(disable_slu),
        }
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def wait_for_listen(self, sentence, config=None, timeout=10):
        """
        Wait for speak and listen execute completed and return SLU result.

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.set_expression(RobotFace.HAPPY, timeout=5)
             sdk.robot.jump_to_plan('E7AABB554ACB414C9AB9BF45E7FA8AD9',
                'lanuchHelloWolrd_Plan')
             slu_result = sdk.robot.wait_for_listen('Which city do you like?\
 You can say Hello Block City, or Hello White City')

        :param sentence: sentence sentence of text to speech
        :param config: configuration for speak engine
        :param timeout: maximum blocking time in second, None means infinity
        :return: SLU result, if timeout will return None
        """
        serial, result = self.speak_and_listen(sentence,
                                               config,
                                               timeout=timeout)
        if result is not None and result['state'] == 5:
            logger.info('wait for listen start')
            wait_for_listen = WaitForListen(self._inter_comm)
            slu_result = wait_for_listen.start(timeout)
            return slu_result
        else:
            logger.warning('speak and listen start fail serial:%d, result:%s',
                           serial, result)

    def wait_for_doa(self, sentence, config=None, timeout=10):
        """
        Wait for speak and listen execute completed and return
        DOA (direction of arrival).

        .. code-block:: python
            :caption: Usage

             sdk = pyzenbo.connect(host_ip)
             sdk.robot.set_expression(RobotFace.HAPPY, timeout=5)
             sdk.robot.jump_to_plan('E7AABB554ACB414C9AB9BF45E7FA8AD9',
                'lanuchHelloWolrd_Plan')
             doa = sdk.robot.wait_for_doa('Which city do you like?\
 You can say Hello Block City, or Hello White City')

        :param sentence: sentence sentence of text to speech
        :param config: configuration for speak engine
        :param timeout: maximum blocking time in second, None means waiting speak and listen completed.
        :return: DOA result, if timeout or the error code of the listen result is not success will return None
        """
        self.speak_and_listen(sentence, config, sync=False)
        logger.info('wait for doa start')
        wait_for_doa = WaitForListenDoa(self._inter_comm)
        doa_result = wait_for_doa.start(timeout)
        logger.debug('wait for doa result:%s', doa_result)
        if not isinstance(doa_result, dict):
            return None
        return doa_result.get('doa')
