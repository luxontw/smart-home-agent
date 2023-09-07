#: no error
NO_ERROR = 0
#: unknown command
UNKNOWN_COMMAND = 1
#: command not in waiting queue
COMMAND_NOT_IN_QUEUE = 2
#: command is overridden
COMMAND_OVERRIDE = 3
#: waiting queue is full
WAITING_QUEUE_IS_FULL = 4
#: user canceled
USER_CANCELED = 5
#: process killed
PROCESS_KILLED = 6
#: permission denied
PERMISSION_DENIED = 7
#: service failed
SERVICE_FAILED = 8
#: robot followed the wrong person
FOLLOW_WRONG_USER = 9
#: unknown error
UNKNOWN_ERROR = 10
#: map does not exist
MAP_NOT_EXIST = 11
#: multi-task queue is full
MULTITASK_QUEUE_IS_FULL = 12
#: is not a multi-task command
NOT_MULTITASK_COMMAND = 13
#: adjust motion speed failed
ADJUST_SPEED_FAILED = 15
#: cancel failed
CANCEL_FAILED = 16
#: queue is empty
QUEUE_IS_EMPTY = 17
#: queue isn't empty
QUEUE_IS_NOT_EMPTY = 18
#: robot is charging
CHARGING = 19
#: unknown face
ERROR_FACE_UNKNOWN = -1
#: face detect failed
ERROR_FACE_DETECT_FAIL = -2
#: face recognition failed
ERROR_RECOGNITION_STATUS_FAILED = -3
#: face is sideways
ERROR_FACE_TOO_SIDE = -4
#: face is too dark
ERROR_FACE_TOO_DARK = -5
#: face under recognition
ERROR_FACE_UNDER_RECOGNITION = -6
#: face ID error
ERROR_FACE_INTERNAL_IDERROR = -7
#: no one appeared
ERROR_FACE_NO_ONE_APPEAR = -8
#: face too far
ERROR_FACE_TOO_FAR = -9
#: face is too close
ERROR_FACE_TOO_CLOSE = -10
#: face is too left
ERROR_FACE_TOO_LEFT = -11
#: face is too right
ERROR_FACE_TOO_RIGHT = -12
#: face already enrolled
ERROR_FACE_ALREADY_ENROLL = -13
#: under long process time
ERROR_UNDER_LONG_PROCESS_TIME = -14
#: fail timeout
FAIL_TIME_OUT = -16
#: face is ambiguous
ERROR_FACE_IS_AMBIGUOUS = -21

#: need to grant read/write SD Card permission
GOTO_NO_SDCARD_PERMISSION = 67502080
#: need to grant can draw overlays permission
GOTO_NO_CANDRAWOVERLAYS_PERMISSION = 67502081
#: could not find target slam map
GOTO_MAP_NOT_EXIST = 67502082
#: queried labeling location do not exist
GOTO_QUERY_LOCATION_FAIL_NO_LABEL = 67502083
#: invalid address which out of map size or occupy point
GOTO_INVALID_ADDRESS = 67502084
#: localization query fail
GOTO_LOCALIZATION_ONERROR = 67502085
#: could not find any free point from start
GOTO_NO_FREE_POINT_FROM_START = 67502086
#: user cancel to help localization
GOTO_USER_CANCELED_LOCALIZE_GUIDE = 67502087
#: user want to move zenbo to help to localize
GOTO_USER_REQUEST_MOVING_GUIDE = 67502088
#: user cancel moving task, need to send notification to zenbo mobile
#: application
GOTO_USER_CANCEL_MOVING_TASK = 67502089
#: avoid obstacle fail timeout, including user cancel moving task or wait user
#: ds command timeout
GOTO_FAIL_TIME_OUT = 67502090
#: undefined error including ds initial fail, motion initial fail, go to
#: time out ... etc
GOTO_UNEXPECTED_ERROR = 67502091
#: zenbo got stuck, and user cancel task
GOTO_STUCK_CANCEL = 67502092
#: guide time out or user cancel task
GOTO_GUIDE_TIMEOUT_OR_CANCEL = 67502093
#: zenbo got stuck and timeout
GOTO_STUCK_TIMEOUT = 67502094
#: queried labeling location have no free point to go
GOTO_QUERY_LOCATION_FAIL_NO_FREE_POINT = 67502095
#: zmc mode, camera disable
GOTO_ZMC_CAMERA_OFF = 67502096

#: bind compass service fail
COMPASS_SERVICE_BIND_FAIL = 67764225
#: the values returned by this sensor cannot be trusted because the sensor had
#: no contact with what it was measuring.
COMPASS_SENSOR_NO_CONTACT = 67764226

#: expression initial successfully
EXP_INIT_FINISH = -46
#: expression do not initial successfully
EXP_NOT_INIT_FINISH = -47
#: send error argument to expression
EXP_SEND_ERROR_ARGUMENT = -48
#: can't resume when TTS is playing
EXP_TTS_IS_PLAYING = -49
#: face don't play finish when new face command have preempted
EXP_FACE_PREEMPTED = -50
#: expression need restart when TTS or face service occur error
EXP_NEED_RESTART = -51
#: TTS has stopped when playing
EXP_TTS_STOPPED = -52
#: previous pause TTS sentence has abandoned cause by new one TTS to be paused
EXP_PREVIOUS_PAUSE_TTS_ABANDONED = -53
#: TTS has paused when playing
EXP_TTS_PAUSED = -54
#: TTS has resumed
EXP_TTS_RESUME = -55
#: request facial system change but not finish
EXP_FACIAL_SYSTEM_CHANGE = -56
#: request to put property to setting database but occurs error
EXP_WRITE_DATABASE_FAILED = -57
#: TTS and face queue is resetting
EXP_QUEUE_RESET = -58

#: command isn't in coordinator queue
COORDINATOR_COMMAND_NOT_IN_QUEUE = 131328
#: no permission to execute this command
COORDINATOR_PERMISSION_DENIED = 131584
#: coordinator queue is empty
COORDINATOR_QUEUE_EMPTY = 131840
#: coordinator queue isn't empty
COORDINATOR_QUEUE_NOT_EMPTY = 132096
#: it's an unknown command
COORDINATOR_UNKNOWN_COMMAND = 132352
#: coordinator queue is full
COORDINATOR_QUEUE_FULL = 132608
#: robot needs to charge first
COORDINATOR_READY_TO_CHARGE = 132864
#: coordinator destroyed
COORDINATOR_DESTROYED = 133120
#: command is canceled by application
COORDINATOR_APP_CANCELED = 133376
#: command is preempted
COORDINATOR_COMMAND_PREEMPTED = 133632
#: command cancel failed
COORDINATOR_CANCEL_FAILED = 133888
#: a high-priority application is running, coordinator will reject commands
#: from other package
COORDINATOR_PRIORITY_TOO_LOW = 134144
#: not allow that application use motion command with permission camera or
#: record
COORDINATOR_CAMERA_RECORD_NOT_ALLOW = 134400
#: not allow that application use motion command with USB connected
COORDINATOR_USB_CONNECTED = 134656
#: it's an unknown error
COMMON_UNKNOWN_ERROR = 196864
#: start service failed
COMMON_SERVICE_FAILED = 197120
#: RobotAPI version too old, please update to newest version
COMMON_API_VERSION_TOO_OLD = 197121
#: In sleep mode, reject command
COMMON_IN_SLEEP_MODE = 197122
#: robot not suppord this command
COMMON_NOT_SUPPORTED_COMMAND = 197123
#: process has been killed
COMMON_PROCESS_KILLED = 197376
#: robot is charging now
COMMON_CHARGING = 197632
#: robot is charging with AC-type now
COMMON_CHARGING_AC = 197633
#: robot is charging with Docking-type now
COMMON_CHARGING_DOCKING = 197634
#: robot is moving to docking station for charging, can't execute any command
COMMON_MOVING_TO_DOCKING_STATION = 197635
#: Can't get map because map is building
COMMON_MAP_IS_BUILDING = 197636
#: robot is out of battery, can't execute any command
COMMON_OUT_OF_BATTERY = 197888
#: robot is off in screen, can't execute any command
COMMON_SCREEN_OFF = 197889
#: robot is moving away docking station to execute motion task, can't execute
#: any command
COMMON_MOVING_AWAY_DOCKING_STATION = 197890
#: robot get failed when go away docking station because obstacle in front of
#: docking station
COMMON_MOVING_AWAY_DOCKING_STATION_TIMEOUT_FAILED = 197891
#: camera disable by ZMC
COMMON_ZMC_CAMERA_OFF = 197892
#: moving disable by ZMC
COMMON_ZMC_MOVING_OFF = 197893

#: File isn't found
COMMON_FILE_NOT_FOUND = 197894
#: network request error
COMMON_NETWORK_REQUEST_ERROR = 197895
#: json parse error
COMMON_JSON_PARSE_ERROR = 197896

#: TCP/IP socket connection fail
COMMON_SOCKET_FAIL = 262400

#: fail to send command
MOTION_FAIL_SEND_CMD_DATA = 33554433
#: block command
MOTION_BLOCK_COMMAND = 33554434
#: command over flow
MOTION_FAIL_OVER_FLOW = 33554435
#: command data size is not correct
MOTION_FAIL_SEND_CMD_SIZE = 33554438
#: fail to open the trajectory file
MOTION_FAIL_OPEN_FILE = 33554443
#: base status timeout
MOTION_FAIL_TIMEOUT = 33554448
#: fail obstacle
MOTION_FAIL_OBSTACLE = 33554449
#: fail reach
MOTION_FAIL_REACH = 33554450
#: go from A to B reset end point
MOTION_RESET_END_POINT = 33554451
#: go from A to B start end point
MOTION_RESET_START_POINT = 33554452
#: fail to load the map
MOTION_FAIL_LOAD_MAP = 33554453
#: end point is out of map
MOTION_END_POINT_OUT_OF_MAP = 33554454
#: start point is out of map
MOTION_START_POINT_OUT_OF_MAP = 33554455
#: there is no route in path planning
MOTION_NO_ROUTE = 33554456
#: no slam map
MOTION_NO_SLAM_MAP = 33554457
#: check door label
MOTION_CHECK_DOOR_LABEL = 33554458
#: no route a
MOTION_NO_ROUTE_A = 33554459
#: no route b
MOTION_NO_ROUTE_B = 33554460
#: no section path
MOTION_NO_SECTION_PATH = 33554461
#: B60 detects cliff
MOTION_FAIL_DROP_IR_B60 = 33554542
#: R70 detects cliff
MOTION_FAIL_DROP_IR_R70 = 33554543
#: R45 detects cliff
MOTION_FAIL_DROP_IR_R45 = 33554544
#: L70 detects cliff
MOTION_FAIL_DROP_IR_L70 = 33554545
#: L45 detects cliff
MOTION_FAIL_DROP_IR_L45 = 33554546
#: both L70 and R70 detect cliff
MOTION_FAIL_DROP_IR_LR70 = 33554547
#: Robot has left the ground
MOTION_FAIL_DROP_IR_LIFTED = 33554548
#: drop recover fail
MOTION_FAIL_DROP_IR_RECOVER_FAIL = 33554549
#: both R45 and L45 detect cliff
MOTION_FAIL_DROP_IR_LR45 = 33554550
#: speed level exceed velocity bound
MOTION_EXCEED_VEL_BOUND = 33554468
#: out work space
MOTION_OUT_WORK_SPACE = 33554473
#: robot faces with obstacles
MOTION_AVOIDANCE_STOP = 33554478
#: any drop IR is triggered
MOTION_ANTI_DROP = 33554479
#: fail set odometry
MOTION_FAIL_SET_ODOMETRY = 33554483
#: speed level out of bounds
MOTION_FAIL_OUT_OF_BOUNDS = 33554488
#: exceed the bound of tempo
MOTION_FAIL_OUT_OF_TEMPO_BOUND = 33554493
#: specific action ID is out of definition
MOTION_SPECIFIC_ACTION_OUT_OF_DEFINITION = 33554494
#: docking process retry time is over limit
MOTION_FAIL_DOCKING_THREE_TIMES = 33554582
#: go back docking timeout
MOTION_FAIL_DOCKING_TIMEOUT = 33554583
#: docking error timeout state
MOTION_FAIL_DOCKING_ERROR = 33554584
#: docking abort state
MOTION_FAIL_DOCKING_ABORT = 33554585
#: docking process terminated
MOTION_FAIL_DOCKING_TERMINATE = 33554586
#: it's a warning hint instead of a fail case for coordinator's post
#: application
MOTION_FAIL_FOLLOW_USER_OBSTACLE = 33554633
#: remote exception
MOTION_REMOTE_EXCEPTION = 33555332
#: fail battery plugged AC
MOTION_FAIL_BATTERY_PLUGGED_AC = 33555337
#: neck yaw motor over temperature
MOTION_OVER_TEMPERATURE_NECK_YAW = 33554933
#: neck pitch motor over temperature
MOTION_OVER_TEMPERATURE_NECK_PITCH = 33554934
#: left wheel motor over temperature
MOTION_OVER_TEMPERATURE_WHEEL_L = 33554936
#: right wheel motor over temperature
MOTION_OVER_TEMPERATURE_WHEEL_R = 33554940
#: all motor over temperature
MOTION_OVER_TEMPERATURE_ALL = 33554947
#: neck yaw motor over current
MOTION_OVER_CURRENT_NECK_YAW = 33554953
#: neck yaw motor over current
MOTION_OVER_CURRENT_NECK_PITCH = 33554954
#: left wheel motor over current
MOTION_OVER_CURRENT_WHEEL_L = 33554956
#: right wheel motor over current
MOTION_OVER_CURRENT_WHEEL_R = 33554960
#: all motor over current
MOTION_OVER_CURRENT_ALL = 33554967
#: neck yaw motor over load
MOTION_OVER_LOAD_NECK_YAW = 33554973
#: neck pitch motor over load
MOTION_OVER_LOAD_NECK_PITCH = 33554974
#: left wheel motor over load
MOTION_OVER_LOAD_WHEEL_L = 33554976
#: right wheel motor over load
MOTION_OVER_LOAD_WHEEL_R = 33554980
#: all motor over load
MOTION_OVER_LOAD_ALL = 33554987
#: robot faces with trapping situation
MOTION_TRAPPING = 33554513
#: robot faces with bumping situation
MOTION_BUMPING = 33554514
#: nothing
MOTION_NOTHING = 33554515
#: fail to recover from bumping situation.
#: (B60 drop while recover from bumping)
MOTION_BUMPING_RECOVER_FAIL = 33554516
#: FR detects cliff
MOTION_FAIL_DROP_IR_FR = 33554552
#: FL detects cliff
MOTION_FAIL_DROP_IR_FL = 33554553
#: FC detects cliff
MOTION_FAIL_DROP_IR_FC = 33554554
#: both FR and FC detect cliff
MOTION_FAIL_DROP_IR_FRC = 33554555
#: both FL and FC detect cliff
MOTION_FAIL_DROP_IR_FLC = 33554556
#: both FR and FL detect cliff
MOTION_FAIL_DROP_IR_FRL = 33554557
#: both FR, FL and FC detect cliff
MOTION_FAIL_DROP_IR_FRLC = 33554558
#: robot faces with not safety situation during ctrlBaseVel
MOTION_FAIL_CTRL_BASE_VEL_SAFETY = 33554833
#: follow line timeout (Can't detect line over 3 sec)
MOTION_FAIL_TRACK_LINE_TIME_OUT = 33554733
#: the difference between line and floor is too small
MOTION_FAIL_LINE_DIFFERENCE = 33554734
#: user not calibration before execute line following
MOTION_FAIL_NOT_CALIBRATION = 33554735
#: color sensor non update
MOTION_FAIL_SENSOR_NON_UPDATE = 33554736
#: some parameters are not applied
MOTION_PARAMETER_IS_NOT_APPLIED = 33554688

#: no specific charging station
RETURN_BASE_NO_SPECIFIC_CHARGING_STATION = 67764224

#: identify color timeout (Can't detect color result over 3 sec)
COLOR_IDENTIFICATION_TIMEOUT = 67829760
#: set invalid argument to track line
LINE_FOLLOWER_INVALID_ARGUMENT = 67830016
#: set duplicate argument to track line
LINE_FOLLOWER_DUPLICATE_ARGUMENT = 67830017
#: follow line timeout (Can't detect line over 3 sec)
LINE_FOLLOWER_TRACK_LINE_TIME_OUT = 67830018
#: set invalid color type
LINE_FOLLOWER_INVALID_COLOR_TYPE = 67830019
#: set invalid behavior
LINE_FOLLOWER_INVALID_BEHAVIOR = 67830020
#: set up too many color array on line
LINE_FOLLOWER_TOO_MANY_COLOR_ARRAY = 67830021

#: R200 open failed
VISION_R200_OPEN_FAILED = 83951617
#: unknown error
VISION_LOCALIZATION_UNKNOWN_ERROR = 84017153
#: localization start without initialization first
VISION_LOCALIZATION_INVALID_STATUS = 84017154
#: loading map failed
VISION_LOCALIZATION_MAP_FAILED = 84017155
#: no specified map directory
VISION_LOCALIZATION_NO_SPECIFIED_MAP_DIR = 84017156
#: no camera/storage permission
VISION_LOCALIZATION_PERMISSION_DENIED = 84017157
#: localization is canceled by caller
VISION_LOCALIZATION_CANCELED = 84017158
#: localization result is unreliable
VISION_LOCALIZATION_RESULT_UNRELIABLE = 84017159
#: localization result is occupied
VISION_LOCALIZATION_OCCUPIED_POINT = 84017160
#: localization is unavailable since migration is running
VISION_LOCALIZATION_DOING_MIGRATION = 84017161

#: vision resource is occupied by system plugin
VISION_PROXY_RESOURCE_OCCUPIED = 84082689
#: the vision command is interrupted by others
VISION_PROXY_COMMAND_INTERRUPTED = 84082690
#: vision resource is blocked
VISION_PROXY_RESOURCE_BLOCKED = 84082691

#: user cannot be recognized as faces already enroll in Database
VISION_ENROLL_RESULT_UNKNOWN_USER = 84148481
#: the face in current image is ambiguous
VISION_ENROLL_RESULT_FACE_IS_AMBIGUOUS = 84148482

#: begin face feature extraction
VISION_ENROLL_STATUS_BEGIN_FACE_FEATURE_EXTRACTION = 84148737
#: enroll image collect success
VISION_ENROLL_STATUS_ENROLL_IMAGE_COLLECT_SUCCESS = 84148738
#: person have blur face and fail to recognize
VISION_ENROLL_STATUS_FACE_IMAGE_LOW_QUALITY = 84148739
#: not detected any face
VISION_ENROLL_STATUS_FACE_NOT_DETECTED = 84148740
#: face pitch angle is too large
VISION_ENROLL_STATUS_FACE_PITCH_TOO_LARGE = 84148741
#: user is looking somewhere else but not look into zenbo
VISION_ENROLL_STATUS_FACE_POSE_TOO_EXTREME = 84148742
#: vision service is retrying to recognize face because of low score
VISION_ENROLL_STATUS_FACE_RECOGNITION_SCORE_LOW_RETRYING = 84148743
#: face is too close
VISION_ENROLL_STATUS_FACE_TOO_CLOSE = 84148744
#: face is too far
VISION_ENROLL_STATUS_FACE_TOO_FAR = 84148745
#: face yaw angle is too large
VISION_ENROLL_STATUS_FACE_YAW_TOO_LARGE = 84148746
#: face enroll is finished
VISION_ENROLL_STATUS_FINISH_FACE_ENROLL = 84148747
#: pause enroll command is succeed
VISION_ENROLL_STATUS_PAUSE_ENROLL_SUCCESS = 84148748
#: no any person is detected
VISION_ENROLL_STATUS_PERSON_NOT_DETECTED = 84148749
#: framework not specify turn on recognition during person detection
VISION_ENROLL_STATUS_RECOGNITION_OFF = 84148750
#: report all the predefined enroll posture
VISION_ENROLL_STATUS_REPORT_DEFINE_POSES = 84148751
#: resume enroll command is succeed
VISION_ENROLL_STATUS_RESUME_ENROLL_SUCCESS = 84148752
#: skip enroll command is succeed
VISION_ENROLL_STATUS_SKIP_POSTURE_ENROLL_SUCCESS = 84148753
#: service is waiting R200 snapshot taken
VISION_ENROLL_STATUS_WAIT_SNAPSHOT_ENROLL_IMAGE = 84148754

#: abort enroll fail
VISION_ENROLL_WARNING_ABORT_ENROLL_FAIL = 84148993
#: duplicate enroll request
VISION_ENROLL_WARNING_DUPLICATE_ENROLL_REQUEST = 84148994
#: new enroll face is already enroll
VISION_ENROLL_WARNING_FACE_ALREADY_ENROLL = 84148995
#: face in image is too dark
VISION_ENROLL_WARNING_FACE_TOO_DARK = 84148996
#: pause enroll command is failed
VISION_ENROLL_WARNING_PAUSE_ENROLL_FAIL = 84148997
#: fail to do recognition even when face detection success
VISION_ENROLL_WARNING_RECOGNITION_STATUS_FAILED = 84148998
#: current registration fail internally
VISION_ENROLL_WARNING_REGISTRATION_STATUS_FAIL = 84148999
#: resume enroll command is failed
VISION_ENROLL_WARNING_RESUME_ENROLL_FAIL = 84149000
#: skip enroll command is failed
VISION_ENROLL_WARNING_SKIP_POSTURE_ENROLL_FAIL = 84149001
#: new enroll person is similar to existing user but different
VISION_ENROLL_WARNING_TOO_SIMILAR_FACE_FOR_NEW_USER = 84149002
#: id already exist
VISION_ENROLL_ID_ALREADY_EXIST = 84149003
#: id can't be empty
VISION_ENROLL_ID_IS_EMPTY = 84149004
#: too many invalid pictures
VISION_ENROLL_PICTURE_INVALID = 84149005
#: photo enroll folder not exist
VISION_ENROLL_FOLDER_NOT_EXIST = 84149006

#: wheel light locked, access denied
WHEEL_LIGHT_EPERM = 100663297
#: no such file or directory
WHEEL_LIGHT_ENOENT = 100663298
#: no such device or address
WHEEL_LIGHT_ENXIO = 100663302
#: permissions denied
WHEEL_LIGHT_EACCES = 100663309
#: no such device
WHEEL_LIGHT_ENODEV = 100663315
#: invalid argument
WHEEL_LIGHT_EINVAL = 100663318
#: i2c timeout
WHEEL_LIGHT_I2C_TIMEOUT = 100663406
#: remote I/O error
WHEEL_LIGHT_EREMOTEIO = 100663417
#: wheel light locked by irreversible abnormality
WHEEL_LIGHT_LOCKED_BY_IRREVERSIBLE_ABNORMALITY = 100663552
#: wheel light locked by recoverable abnormality
WHEEL_LIGHT_LOCKED_BY_RECOVERABLE_ABNORMALITY = 100663553
#: wheel light locked by battery status
WHEEL_LIGHT_LOCKED_BY_BATTERY_STATUS = 100663554

#: http service start code
VOICE_ENROLL_HTTP_SERVICE_START_CODE = 117440513
#: http service end code
VOICE_ENROLL_HTTP_SERVICE_END_CODE = 117440514

#: sdk request start code
VOICE_ENROLL_SDK_REQUEST_START_CODE = 117440768
#: sdk request end code
VOICE_ENROLL_SDK_REQUEST_END_CODE = 117440769
#: sdk request login handle illegal
VOICE_ENROLL_SDK_REQUEST_LOGIN_HANDLE_ILLEGAL = 117440770
#: sdk request connect to service fail
VOICE_ENROLL_SDK_REQUEST_CONNECT_TO_SERVICE_FAIL = 117440771
#: sdk request response json prase fail
VOICE_ENROLL_SDK_REQUEST_RESPONSE_JSON_PRASE_FAIL = 117440772
#: sdk request error file as open fail
VOICE_ENROLL_SDK_REQUEST_ERROR_FILE_AS_OPEN_FAIL = 117440773
#: sdk request sdk unregister url
VOICE_ENROLL_SDK_REQUEST_SDK_UNREGISTER_URL = 117440774

#: logic service internal error
VOICE_ENROLL_LOGIC_SERVICE_INTERNAL_ERROR = 117441024
#: login service signature verify fail
VOICE_ENROLL_LOGIC_SERVICE_SIGNATURE_VERIFY_FAIL = 117441025
#: login service error input param
VOICE_ENROLL_LOGIC_SERVICE_ERROR_INPUT_PARAM = 117441026
#: login service invalid signature
VOICE_ENROLL_LOGIC_SERVICE_INVALID_SIGNATURE = 117441027
#: login service appid no exist
VOICE_ENROLL_LOGIC_SERVICE_APPID_NOEXIST = 117441028
#: login service refresh packet failure
VOICE_ENROLL_LOGIC_SERVICE_REFRESH_PACKET_FAILURE = 117441029
#: login service packet id can not be empty
VOICE_ENROLL_LOGIC_SERVICE_PACKET_ID_CAN_NOT_BE_EMPTY = 117441030
#: login service clientname can not be empty
VOICE_ENROLL_LOGIC_SERVICE_CLIENTNAME_CAN_NOT_BE_EMPTY = 117441031
#: login service create client failure
VOICE_ENROLL_LOGIC_SERVICE_CREATE_CLIENT_FAILURE = 117441032
#: login service refresh client failure
VOICE_ENROLL_LOGIC_SERVICE_REFRESH_CLIENT_FAILURE = 117441033
#: login service sql error
VOICE_ENROLL_LOGIC_SERVICE_SQL_ERROR = 117441034
#: login service token refresh fail
VOICE_ENROLL_LOGIC_SERVICE_TOKEN_REFRESH_FAIL = 117441035
#: login service creating path system error
VOICE_ENROLL_LOGIC_SERVICE_CREATING_PATH_SYSTEM_ERROR = 117441036
#: login serivce save file failure
VOICE_ENROLL_LOGIC_SERVICE_SAVE_FILE_FAILURE = 117441037
#: login service registration failure
VOICE_ENROLL_LOGIC_SERVICE_REGISTRATION_FAILURE = 117441038
#: login service verification failure
VOICE_ENROLL_LOGIC_SERVICE_VERIFICATION_FAILURE = 117441039
#: service client create error
VOICE_ENROLL_SERVICE_CLIENT_CREATE_ERROR = 117441040

#: sentence no match
VOICE_ENROLL_SENTENCE_NO_MATCH = 117441280
#: sound level too low
VOICE_ENROLL_SOUND_LEVEL_TOO_LOW = 117441281
#: environment too noisy
VOICE_ENROLL_ENVIRONMENT_TOO_NOISY = 117441282
#: enroll timeout
VOICE_ENROLL_ENROLL_TIMEOUT = 117441283
#: enroll force stop
VOICE_ENROLL_FORCESTOP = 117441284
#: Enroll service initialization has not been completed. Please try again
#: later.
VOICE_ENROLL_INIT_NOT_READY = 117441285
#: wifi disconnect
VOICE_ENROLL_WIFI_DISCONNECT = 117441286

#: plugin followUser stopped because of not found
PLUGIN_FAIL_FOLLOW_USER_NOT_FOUND = 67436544
#: plugin followUser stopped because of meeting obstacle
PLUGIN_FAIL_FOLLOW_USER_OBSTACLE = 67436545
#: plugin followUser stopped because of lost
PLUGIN_FAIL_FOLLOW_USER_LOST = 67436546

description = {
    0: "no error",
    1: "unknown command",
    2: "command not in waiting queue",
    3: "command is overridden",
    4: "waiting queue is full",
    5: "user canceled",
    6: "process killed",
    7: "permission denied",
    8: "service failed",
    9: "robot followed the wrong person",
    10: "unknown error",
    11: "map does not exist",
    12: "multi-task queue is full",
    13: "is not a multi-task command",
    15: "adjust motion speed failed",
    16: "cancel failed",
    17: "queue is empty",
    18: "queue isn't empty",
    19: "robot is charging",
    -1: "unknown face",
    -2: "face detect failed",
    -3: "face recognition failed",
    -4: "face is sideways",
    -5: "face is too dark",
    -6: "face under recognition",
    -7: "face ID error",
    -8: "no one appeared",
    -9: "face too far",
    -10: "face is too close",
    -11: "face is too left",
    -12: "face is too right",
    -13: "face already enrolled",
    -14: "under long process time",
    -16: "fail timeout",
    -21: "face is ambiguous",

    67502080: "need to grant read/write SD Card permission",
    67502081: "need to grant can draw overlays permission",
    67502082: "could not find target slam map",
    67502083: "queried labeling location do not exist",
    67502084: "invalid address which out of map size or occupy point",
    67502085: "localization query fail",
    67502086: "could not find any free point from start",
    67502087: "user cancel to help localization",
    67502088: "user want to move zenbo to help to localize",
    67502089: "user cancel moving task, need to send notification to zenbo mobile application",
    67502090: "avoid obstacle fail timeout, including user cancel moving task or wait user ds command timeout",
    67502091: "undefined error including ds initial fail, motion initial fail, go to time out ... etc",
    67502092: "zenbo got stuck, and user cancel task",
    67502093: "guide time out or user cancel task",
    67502094: "zenbo got stuck and timeout",
    67502095: "queried labeling location have no free point to go",
    67502096: "zmc mode, camera disable",

    67764225: "bind compass service fail",
    67764226: "the values returned by this sensor cannot be trusted because "
              "the sensor had no contact with what it was measuring.",

    -46: "expression initial successfully",
    -47: "expression do not initial successfully",
    -48: "send error argument to expression",
    -49: "can't resume when TTS is playing",
    -50: "face don't play finish when new face command have preempted",
    -51: "expression need restart when TTS or face service occur error",
    -52: "TTS has stopped when playing",
    -53: "previous pause TTS sentence has abandoned cause by new one TTS to be paused",
    -54: "TTS has paused when playing",
    -55: "TTS has resumed",
    -56: "request facial system change but not finish",
    -57: "request to put property to setting database but occurs error",
    -58: "TTS and face queue is resetting",

    131328: "command isn't in coordinator queue",
    131584: "no permission to execute this command",
    131840: "coordinator queue is empty",
    132096: "coordinator queue isn't empty",
    132352: "it's an unknown command",
    132608: "coordinator queue is full",
    132864: "robot needs to charge first",
    133120: "coordinator destroyed",
    133376: "command is canceled by application",
    133632: "command is preempted",
    133888: "command cancel failed",
    134144: "a high-priority application is running, coordinator will reject commands from other package",
    134400: "not allow that application use motion command with permission camera or record",
    134656: "not allow that application use motion command with USB connected",
    196864: "it's an unknown error",
    197120: "start service failed",
    197121: "RobotAPI version too old, please update to newest version",
    197122: "In sleep mode, reject command",
    197123: "robot not supported this command",
    197376: "process has been killed",
    197632: "robot is charging now",
    197633: "robot is charging with AC-type now",
    197634: "robot is charging with Docking-type now",
    197635: "robot is moving to docking station for charging, can't execute any command",
    197636: "Can't get map because map is building",
    197888: "robot is out of battery, can't execute any command",
    197889: "robot is off in screen, can't execute any command",
    197890: "robot is moving away docking station to execute motion task, can't execute any command",
    197891: "robot get failed when go away docking station because obstacle in front of docking station",
    197892: "camera disable by ZMC",
    197893: "moving disable by ZMC",

    262400: 'python sdk build sockets failed.',

    33554433: "fail to send command",
    33554434: "block command",
    33554435: "command over flow",
    33554438: "command data size is not correct",
    33554443: "fail to open the trajectory file",
    33554448: "base status timeout",
    33554449: "fail obstacle",
    33554450: "fail reach",
    33554451: "go from A to B reset end point",
    33554452: "go from A to B start end point",
    33554453: "fail to load the map",
    33554454: "end point is out of map",
    33554455: "start point is out of map",
    33554456: "there is no route in path planning",
    33554457: "no slam map",
    33554458: "check door label",
    33554459: "no route a",
    33554460: "no route b",
    33554461: "no section path",
    33554542: "B60 detects cliff",
    33554543: "R70 detects cliff",
    33554544: "R45 detects cliff",
    33554545: "L70 detects cliff",
    33554546: "L45 detects cliff",
    33554547: "both L70 and R70 detect cliff",
    33554548: "Robot has left the ground",
    33554549: "drop recover fail",
    33554550: "both R45 and L45 detect cliff",
    33554468: "speed level exceed velocity bound",
    33554473: "out work space",
    33554478: "robot faces with obstacles",
    33554479: "any drop IR is triggered",
    33554483: "fail set odometry",
    33554488: "speed level out of bounds",
    33554493: "exceed the bound of tempo",
    33554494: "specific action ID is out of definition",
    33554582: "docking process retry time is over limit",
    33554583: "go back docking timeout",
    33554584: "docking error timeout state",
    33554585: "docking abort state",
    33554586: "docking process terminated",
    33554633: "it's a warning hint instead of a fail case for coordinator's post application",
    33555332: "remote exception",
    33555337: "fail battery plugged AC",
    33554933: "neck yaw motor over temperature",
    33554934: "neck pitch motor over temperature",
    33554936: "left wheel motor over temperature",
    33554940: "right wheel motor over temperature",
    33554947: "all motor over temperature",
    33554953: "neck yaw motor over current",
    33554954: "neck yaw motor over current",
    33554956: "left wheel motor over current",
    33554960: "right wheel motor over current",
    33554967: "all motor over current",
    33554973: "neck yaw motor over load",
    33554974: "neck pitch motor over load",
    33554976: "left wheel motor over load",
    33554980: "right wheel motor over load",
    33554987: "all motor over load",
    33554513: "robot faces with trapping situation",
    33554514: "robot faces with bumping situation",
    33554515: "nothing",
    33554516: "fail to recover from bumping situation.B60 drop while recover from bumping)",
    33554552: "FR detects cliff",
    33554553: "FL detects cliff",
    33554554: "FC detects cliff",
    33554555: "both FR and FC detect cliff",
    33554556: "both FL and FC detect cliff",
    33554557: "both FR and FL detect cliff",
    33554558: "both FR, FL and FC detect cliff",
    33554833: "robot faces with not safety situation during ctrlBaseVel",
    33554733: "follow line timeout Can't detect line over 3 sec)",
    33554734: "the difference between line and floor is too small",
    33554735: "user not calibration before execute line following",
    33554736: "color sensor non update",
    33554688: "some parameters are not applied",

    67764224: "no specific charging station",

    67829760: "identify color timeout Can't detect color result over 3 sec)",
    67830016: "set invalid argument to track line",
    67830017: "set duplicate argument to track line",
    67830018: "follow line timeout Can't detect line over 3 sec)",
    67830019: "set invalid color type",
    67830020: "set invalid behavior",
    67830021: "set up too many color array on line",

    83951617: "R200 open failed",
    84017153: "unknown error",
    84017154: "localization start without initialization first",
    84017155: "loading map failed",
    84017156: "no specified map directory",
    84017157: "no camera/storage permission",
    84017158: "localization is canceled by caller",
    84017159: "localization result is unreliable",
    84017160: "localization result is occupied",
    84017161: "localization is unavailable since migration is running",

    84082689: "vision resource is occupied by system plugin",
    84082690: "the vision command is interrupted by others",
    84082691: "vision resource is blocked",

    84148481: "user cannot be recognized as faces already enroll in Database",
    84148482: "the face in current image is ambiguous",

    84148737: "begin face feature extraction",
    84148738: "enroll image collect success",
    84148739: "person have blur face and fail to recognize",
    84148740: "not detected any face",
    84148741: "face pitch angle is too large",
    84148742: "user is looking somewhere else but not look into zenbo",
    84148743: "vision service is retrying to recognize face because of low score",
    84148744: "face is too close",
    84148745: "face is too far",
    84148746: "face yaw angle is too large",
    84148747: "face enroll is finished",
    84148748: "pause enroll command is succeed",
    84148749: "no any person is detected",
    84148750: "framework not specify turn on recognition during person detection",
    84148751: "report all the predefined enroll posture",
    84148752: "resume enroll command is succeed",
    84148753: "skip enroll command is succeed",
    84148754: "service is waiting R200 snapshot taken",

    84148993: "abort enroll fail",
    84148994: "duplicate enroll request",
    84148995: "new enroll face is already enroll",
    84148996: "face in image is too dark",
    84148997: "pause enroll command is failed",
    84148998: " fail to do recognition even when face detection success",
    84148999: "current registration fail internally",
    84149000: "resume enroll command is failed",
    84149001: "skip enroll command is failed",
    84149002: "new enroll person is similar to existing user but different",
    84149003: "id already exist",
    84149004: "id can't be empty",
    84149005: "too many invalid pictures",
    84149006: "photo enroll folder not exist",

    100663297: "wheel light locked, access denied",
    100663298: "no such file or directory",
    100663302: "no such device or address",
    100663309: "permissions denied",
    100663315: "no such device",
    100663318: "invalid argument",
    100663406: "i2c timeout",
    100663417: "remote I/O error",
    100663552: "wheel light locked by irreversible abnormality",
    100663553: "wheel light locked by recoverable abnormality",
    100663554: "wheel light locked by battery status",

    117440513: "HTTP service start code",
    117440514: "HTTP service end code",

    117440768: "SDK request start code",
    117440769: "SDK request end code",
    117440770: "SDK request login handle illegal",
    117440771: "SDK request connect to service fail",
    117440772: "SDK request response JSON parser fail",
    117440773: "SDK request error file as open fail",
    117440774: "SDK request SDK unregister url",

    117441024: "logic service internal error",
    117441025: "login service signature verify fail",
    117441026: "login service error input parameter",
    117441027: "login service invalid signature",
    117441028: "login service appid no exist",
    117441029: "login service refresh packet failure",
    117441030: "login service packet id can not be empty",
    117441031: "login service client name can not be empty",
    117441032: "login service create client failure",
    117441033: "login service refresh client failure",
    117441034: "login service SQL error",
    117441035: "login service token refresh fail",
    117441036: "login service creating path system error",
    117441037: "login service save file failure",
    117441038: "login service registration failure",
    117441039: "login service verification failure",
    117441040: "service client create error",

    117441280: "sentence no match",
    117441281: "sound level too low",
    117441282: "environment too noisy",
    117441283: "enroll timeout",
    117441284: "enroll force stop",
    117441285: "Enroll service initialization has not been completed. Please try again later.",
    117441286: "WIFI disconnect",

    67436544: "plugin followUser stopped because of not found",
    67436545: "plugin followUser stopped because of meeting obstacle",
    67436546: "plugin followUser stopped because of lost",
}


def code_to_description(code):
    """
    Get error code description.

    :param code: error code number
    :return: error code description
    """
    if description[code]:
        return description[code]
    return 'Unknown error code'
