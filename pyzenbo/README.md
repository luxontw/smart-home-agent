# Python Zenbo junior SDK project #

## Table of contents
* [Import](#import)
* [Usage](#usage)
* [Tests](#tests)

## Import ##
***pyzenbo 支援 python 3.6 以上版本***

在 pyzenbo 目錄下執行 `python setup.py install` or
`python3 setup.py install` 安裝 pyzenbo 後可直接 import
```Python
import pyzenbo
```
在 pyzenbo 未安裝前，可透過 tests\context.py 在執行時將目前目錄加入 system path，
未來將會提供 pip 安裝或預載。
```Python
from context import pyzenbo
```
## Initial ##
開始使用 Python Zenbo junior SDK 前，需要先開啟 Zenbo junior 上的 Zenbo Lab，
開啟後會顯示目前連線的 Wi-Fi SSID 及 IP。
<img alt="Zenbo Lab IP" src="img/zenbo_lab.png" />

第一次啟動時需要同意忽略電池效能最佳化設定。
<img alt="Allow ignore battery optimization" src="img/battery_optimization.png" />

pyzenbo 需要 Zenbo Lab 上顯示的 IP 並且與 Zenbo junior 在同一區網中。

SDK 使用完畢後，需使用 `sdk.release()` 結束與 Zenbo junior 的連線。
如未正常結束連線， service 將會在 25 秒後斷開連線，等待下一次連線。
```Python
import pyzenbo

host = '192.168.0.214'
sdk = pyzenbo.connect(host)

sdk.motion.move_head(0, 30, 2)

sdk.release()
```

## Usage ##
pyzenbo 指令參數與 android 版 Zenbo SDK 相同，相關參數請參閱 Zenbo SDK 文件。

pyzenbo 可使用 callback 形式取得指令執行的結果
```Python
from pyzenbo.modules.error_code import code_to_description


def on_state_change(serial, cmd, error, state):
    msg = 'on_state_change serial:{}, cmd:{}, error:{}, state:{}'
    print(msg.format(serial, cmd, error, state))
    if error:
        print('on_state_change error:', code_to_description(error))


def on_result(**kwargs):
    print('on_result', kwargs)


sdk.on_state_change_callback = on_state_change
sdk.on_result_callback = on_result

result = sdk.motion.move_body(10, 0, 0, 2, sync=True, timeout=10)
```

同時也可使用 method 內參數 `sync=True` 來同步執行，當指令執行完畢後回傳結果或 timeout
後取消目前指令後回傳結果。回傳結果為 tuple，第一項為指令執行的 serial number，
第二個為 dict 包含執行結果 'state' 及 'error'。
```Python
STATE = {0: 'INITIAL', 1: 'PENDING', 2: 'REJECTED',
         3: 'ACTIVE', 4: 'FAILED', 5: 'SUCCEED', 6: 'PREEMPTED', }
```

Utility 中`sdk.utility.track_face(sync=False, timeout=None),
sdk.utility.follow_face(sync=False, timeout=None),
sdk.utility.follow_object(sync=False, timeout=None)`
三個指令因為不會主動停止，因此預設 `sync=False`，建議使用 callback 或使用 timeout
來結束指令。


## Tests ##
Tests 下提供 pyzenbo SDK 基本功能展示及功能測試。

### demo_callback.py ###
展示基礎 Python Zenbo junior SDK callback 功能。

* 預期效果隱藏大臉後開始偵測人臉並在 Zenbo junior 螢幕上顯示 detect face debug 畫面。
* 偵測到人臉後說出 'Hello, my name is Zenbo Junior. Nice to meet you.',
'Which city do you like? You can say Hello Block City, or Hello White City'
後開啟收音，收音結果會顯示在 PC 執行視窗。
* 偵測人臉時超過15秒沒有看到人會說出 'No one is here'。

### demo_file_transfer.py ###
展示基本檔案傳送功能。

* 預期結果拍照後將照片從 Zenbo junior 下載至 PC 的執行目錄下。

### demo_hello_world.py ###
展示基本表情及語音功能。

* 顯示開心表情並說出 'Hello World'。

### demo_media.py ###
展示錄音功能。

* 開啟錄音功能10秒。
* 錄音完成後，撥放錄製的音檔後將檔案從 Zenbo junior 下載至 PC 的執行目錄下。

### demo_media_play.py ###
展示錄影及撥放功能。

* 開啟倒數15秒的錄影功能，錄影10秒後停止錄影。
* 錄影完成後撥放錄製的影片。
* 開啟拍照功能後，顯示照片五秒後結束。

### demo_move_body.py ###
展示基本移動指令。

* 向前移動40公分後再迴轉後退40公分。

### demo_wait_for.py ###
展示 vision wait for 功能。

* 預期效果隱藏大臉後開始偵測人臉並 Zenbo junior 螢幕上顯示 detect face debug 畫面。
* 收到偵測 callback 後說出 'Hello, my name is Zenbo Junior. Nice to meet you.',
'Which city do you like? You can say Hello Block City, or Hello White City'
後開啟收音，收音結果會顯示在 PC 執行視窗。
* 偵測人臉時超過15秒沒有看到人會說出 'No one is here'。
