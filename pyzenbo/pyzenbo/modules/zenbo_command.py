#: Robot command cancel.
CANCEL = 0
# Ask robot to go to the location before the users.
COME_HERE = 1
# Ask robot to follow the user.
FOLLOW_USER = 2
# Ask robot to move to specific location.
GOTO_LOCATION = 3
# Move robot to find specified person.
FIND_PERSON = 4
# Release Base wheel lock.
RELEASE_BASE = 5
#: Ask robot to turn its head.
MOVE_HEAD = 6
# Ask robot to move to the location by specifying locationId or coordination.
RETURN_BASE = 8
# Ask robot to return its charging station.
PATROL = 9
# Ask robot to patrol.
RETURN_HOME = 10
#
PARTY_MODE = 11
#
TRACK_USER = 12

# Set screen blue light.
SET_SCREEN_BLUE_LIGHT = 13
#
GO_BACK = 14
# Show \"touch only\" on top of screen.
TOUCH_ONLY_SIGNAL = 15
# Get system robot API level.
GET_SYSTEM_ROBOT_API_LEVEL = 16

#
MOTION_MISSION_CONFIRM = 17
#
CONTINUE_MISSION = 18
#
CANCEL_MISSION = 19
# Query abnormal state.
GET_ABNORMAL_EVENT = 20
# Declare/relieve abnormal state.
ABNORMAL_EVENT = 21
# Set commander config.
SET_CONFIG = 22
# Enable/disable audio echo cancellation.
AUDIO_ECHO_CANCELLATION = 23
# Let user tell Zenbo bumping.
BUMP_SOMETHING = 24
#: Application back to background.
BACK_TO_BACKGROUND = 25
# The mode is 1, a talk process will be interrupted by using DS_STOP_TTS.
# The mode is 0, a talk process will be interrupted by using DS_PAUSE_SPEAK &
# DS_RESUME_SPEAK.
GET_DAILY_DIALOGUE_MODE = 26
# If the robot talk process is interrupted by using DS_STOP_TTS or
# DS_PAUSE_SPEAK & DS_RESUME_SPEAK. The robot will say the interrupted
# paragraph again, the mode is 1 about the DS_STOP_TTS using. The robot will
# continue to say from its breakpoint, the mode is 0 about the DS_PAUSE_SPEAK
# & DS_RESUME_SPEAK using.
SET_DAILY_DIALOGUE_MODE = 27
# Set new trigger world.
SET_TRIGGER_WORD = 28
# Change facial model.
CHANGE_FACIAL_MODEL = 29
#: Query current robot expression status.
QUERY_EXPRESSION_STATUS = 30

#: Make robot expression and speak.
SET_EXPRESSION = 31
#: Perform robot expression and predefined action.
PLAY_EMOTIONAL_ACTION = 32
#: Start speaking.
SPEAK = 33
#: Stop speaking.
STOP_SPEAK = 34
# Screen off.
SCREEN_OFF = 35
# Register system action monitor.
REGISTER_SYSTEM_ACTION_MONITOR = 37
# Unregister system action monitor.
UNREGISTER_SYSTEM_ACTION_MONITOR = 38

#: Move a relative distance in Cartesian coordinate.
MOTION_MOVE_BODY = 39
# Smart move head with different distance.
MOTION_HEAD_ADJUSTMENT = 40
# Move from current position to target position, based on the path-finding
# algorithm.
MOTION_GO_FROM_A_TO_B = 41
#: Do specific action for neck and wheel.
MOTION_PLAY_ACTION = 42
# Smart move forward/back/left/right with different distance.
MOTION_ADJUSTMENT = 43
#: Motion remote control.
MOTION_REMOTE_CONTROL_BODY = 44
#: Stop all motion action.
MOTION_STOP = 45

#: The led will light up by the bright value with the default color or the
#: color set by the setColor command.
WHEEL_LIGHTS_SET_BRIGHT = 47
#: The color will be stored on HAL and wait the setBright command to trigger
#: the light.
WHEEL_LIGHTS_SET_COLOR = 48
#: Start the lights pattern action.
WHEEL_LIGHTS_SET_PATTERN = 50
#: Stop the lights pattern set by startPattern.
WHEEL_LIGHTS_STOP_PATTEN = 51

#: Connect to DS service.
DS_SERVICE_CONNECT = 61
#: Release DS service.
DS_SERVICE_RELEASE = 62
# Start TTS from DS service.
DS_START_TTS = 63
# Start CSR from DS service.
DS_START_CSR = 64
# Start TTS/CSR/SLU from DS service.
DS_START_TTS_CSR_SLU = 65
# Start SLU query for domain change.
DS_SLU_QUERY = 66
#: Set DS voice trigger enable/disable.
DS_VOICE_TRIGGER = 67
# Config auto CSR/SLU after trigger word.
DS_CONFIG_AUTO_TRIGGER_CSR_SLU = 68
# Stop TTS from DS service.
DS_STOP_TTS = 69
# Stop CSR from DS service.
DS_STOP_CSR = 70
# Stop TTS/CSR/SLU from DS service.
DS_STOP_TTS_CSR_SLU = 71
# Enrollment.
DS_TD_JsonCMD = 72

# Execute in JSON format of dialog system.
APP_EXECUTION = 73
# Get the current coordinator active application hash.
GET_ACTIVE_APP_NAME = 74
# Check if robot is busy or idle.
IS_IDLE = 75
# Request idle monitor.
IDLE_MONITOR = 76
# Ask coordinator to ignore idle status for next received command.
COORDINATOR_IGNORE_IDLE = 77
#: Release all robot API resource.
RELEASE = 78
# Finish routing TTS command.
DS_ROUTING_FINISH_TTS_CMD = 79
# Request battery monitor.
BATTERY_MONITOR = 80
# The light up/down.
SET_BRIGHT = 81
# Get queue current status.
GET_QUEUE_STATUS = 82
#: Motion remote control neck.
MOTION_REMOTE_CONTROL_HEAD = 83
# Get intelligent plug-in version.
QUERY_PLUGIN_VERSION = 84
# Ask robot to move to specific location by using arm gesture.
GO_THERE_BY_GESTURE = 85
# reset all service.
RESET_ALL_SERVICE = 88

# Reset all feature parameters to default value.
TTS_RESET_FEATURE = 92
# Sets the language and the speaker of the speech, and load the corresponding
# models. While using English model, TTS will only synthesize English words
# and pass all Mandarin words. However, Mandarin model can synthesize both
# Mandarin and English.
TTS_SET_SPEAKER_ID = 93
# Sets the pitch of entire sentence.
TTS_SET_PITCH = 94
# Sets the speed of entire sentence.
TTS_SET_SPEED = 95
# sets the volume to the specified level, where level is a value between 0
# (no volume) and 100 (the maximum volume), where 80 is typically the default
# volume.
TTS_SET_VOLUME = 96
# Sets the end of sentence pause duration (wait period) to a value between 0
# and 9, where the pause will be 200 msec multiplied by that number.
TTS_SET_WAIT_FACTOR = 97
# Sets reading Mode of TTS, it can change the reading mode from sentence mode
# (the default) to various specialized modes.
TTS_SET_READ_MODE = 98
# Get current TTS setting information, and return current setting values in
# JSON format by callback function.
TTS_GET_SETTING_INFO = 99

# Set application information for DS trigger.
SET_APPINFO = 100
#
RETURN_ANDROID = 101
# Ask robot to return its charging station for debug mode.
RETURN_BASE_DEBUG_MODE = 102
# Request top package name.
GET_TOP_PACKAGE_NAME = 103
# Request TTS from DS.
SPEAK_FROM_DS = 104
# Request STOP_TTS from DS.
STOP_SPEAK_FROM_DS = 105
# Request TTS episode (Pause speak).
EPISODE_PAUSE_SPEAK = 106
# Request TTS episode (Resume speak).
EPISODE_RESUME_SPEAK = 107
# Request CLEAR_TTS_AND_FACE_QUEUE.
CLEAR_TTS_AND_FACE_QUEUE = 108

# Execute external command.
EXTERNAL_COMMAND = 109
# Request commander to execute application due to passive find person.
EXECUTE_APP_BY_PFP = 110

# Ask coordinator to not to preempt current executed command.
COORDINATOR_IGNORE_PREEMPTED = 111
# Request coordinator if reserved task can be executed currently.
COORDINATOR_REQUEST_EXECUTE_TASK = 112
# Modify the parameter enableHardDeadlineNotify after using
# requestToExecuteReservedTask.
COORDINATOR_UPDATE_HARD_DEADLINE_NOTIFY = 113
# Display loading screen and hide status/navigation bar.
SYSTEM_LOADING_DISPLAY = 114
# Set expression service loading.
EXPRESSION_SERVICE_LOADING = 115

# Register TTS monitor.
REGISTER_TTS_MONITOR = 116
# Unregister TTS monitor.
UNREGISTER_TTS_MONITOR = 117
# Register system action monitor.
REGISTER_FACIAL_ACTION_MONITOR = 118
# Unregister system action monitor.
UNREGISTER_FACIAL_ACTION_MONITOR = 119

# Set companion mode compatibility.
SET_COMPANION_MODE_COMPATIBILITY = 120
# Set edge trigger.
SET_EDGE_TRIGGER = 121
# Get edge trigger.
GET_EDGE_TRIGGER = 122
# Set subtitle.
SET_SUBTITLE = 123
# Set globe voice trigger.
SET_GLOBE_VOICE_TRIGGER = 124
# Get globe voice trigger.
GET_GLOBE_VOICE_TRIGGER = 125
# Register DOA monitor.
REGISTER_DOA_MONITOR = 148
# Unregister DOA monitor.
UNREGISTER_DOA_MONITOR = 149
# Set migration status.
MIGRATION_SET_STATUS = 150
# Check migration status.
MIGRATION_CHECK_STATUS = 151
# Trigger migration.
MIGRATION_TRIGGER = 152
# Query current user id.
QUERY_CURRENT_USER_ID = 153
# Show the stop action button.
SHOW_BUTTON_STOP_ACTION = 154
# Show the csr listen signal.
SHOW_CSR_LISTEN_SIGNAL = 155

# Ask robot to extract and learn face features in order to recognize faces.
VISION_REQUEST_ENROLL_FACE = 1 * 65536 + 1
# Call when you want erase user enrolled face data from face DB.
VISION_REMOVE_ENROLL_UUID = 1 * 65536 + 2
# Get Enroll FaceID List, return by onEnrollGetAllIDList.
VISION_REQUEST_ENROLL_GET_ALL_ID = 1 * 65536 + 3
#: Request detect person.
VISION_REQUEST_DETECT_PERSON = 1 * 65536 + 4
#: Cancel detect person.
VISION_CANCEL_DETECT_PERSON = 1 * 65536 + 5
#: Request recognize person.
VISION_REQUEST_RECOGNIZE_PERSON = 1 * 65536 + 6
#: Cancel recognize person.
VISION_CANCEL_RECOGNIZE_PERSON = 1 * 65536 + 7
# Ask robot to measure height.
VISION_REQUEST_MEASURE_HEIGHT = 1 * 65536 + 8
# Set camera preview for debug.
VISION_REQUEST_CAMERA_PREVIEW = 1 * 65536 + 9
# Cancel gesture point.
VISION_REQUEST_GESTURE_POINT = 1 * 65536 + 10
# Use CV to find a good location for camera and move to there.
VISION_CAMERA_POSITION = 1 * 65536 + 11
# Set vision config.
VISION_CONFIG = 1 * 65536 + 12
# Cancel enroll face process.
VISION_CANCEL_ENROLL_FACE = 1 * 65536 + 13
#: Request detect face. It support multiple face.
VISION_REQUEST_DETECT_FACE = 1 * 65536 + 14
#: Cancel detect face.
VISION_CANCEL_DETECT_FACE = 1 * 65536 + 15
# Query vision proxy status.
VISION_PROXY_QUERY_STATUS = 1 * 65536 + 16
# Force register vision callback.
VISION_PROXY_REGISTER_CALLBACK = 1 * 65536 + 17
# Unregister vision callback.
VISION_PROXY_UNREGISTER_CALLBACK = 1 * 65536 + 18
# Ask pause face enroll process, collected face images will keep but tracker
# id lost.
VISION_ENROLL_FACE_PAUSE = 1 * 65536 + 19
# Ask pause face enroll process, assign a new track id to be enrolled from.
VISION_ENROLL_FACE_RESUME = 1 * 65536 + 20
# Ask to skip enroll face head posture check.
VISION_ENROLL_FACE_SKIP_POSE_CHECK = 1 * 65536 + 21
# Query define head posture for enrolling face.
VISION_ENROLL_FACE_QUERY_DEFINED_POSES = 1 * 65536 + 22
# Enable/Disable blank camera preview.
VISION_REQUEST_BLANK_CAMERA_PREVIEW = 1 * 65536 + 23
# block/unblock vision resource.
VISION_PROXY_BLOCK_VISION_RESOURCE = 1 * 65536 + 24

#: Connect to DS service.
DS_REGISTER_LISTEN_CALLBACK = 2 * 65536 + 1
#: Release DS service.
DS_UNREGISTER_LISTEN_CALLBACK = 2 * 65536 + 2
#: Start CSR from DS service.
DS_SPEAK_AND_LISTEN = 2 * 65536 + 3
#: Start SLU query for domain change.
DS_STOP_SPEAK_AND_LISTEN = 2 * 65536 + 4
#: Stop TTS from DS service.
DS_CLEAR_APP_CONTEXT = 2 * 65536 + 5
#: Config auto CSR/SLU after trigger word.
DS_DYNAMIC_EDIT_INSTANCE = 2 * 65536 + 6
#: Stop CSR from DS service.
DS_JUMP_TO_PLAN = 2 * 65536 + 7
# Stop TTS/CSR/SLU from DS service.
DS_SET_LISTEN_CONTEXT = 2 * 65536 + 8
# Change dialog system current app to other domain.
DS_CHANGE_CURRENT_APP = 2 * 65536 + 9
# Clear all dialog system output context from context stack.
DS_RESET_ALL_CONTEXT = 2 * 65536 + 10
# Get speak features setting.
DS_GET_SPEAK_FEATURES_SETTING = 2 * 65536 + 11
# Pause speak.
DS_PAUSE_SPEAK = 2 * 65536 + 12
#: Resume speak.
DS_RESUME_SPEAK = 2 * 65536 + 13
# Set the speak pitch of dialog system.
DS_SET_SPEAK_PITCH = 2 * 65536 + 14
# Set the speak speed of dialog system.
DS_SET_SPEAK_SPEED = 2 * 65536 + 15
# Set the speak speed of dialog system.
DS_SET_SPEAK_VOLUME = 2 * 65536 + 16
# Ds set utterance select list.
DS_SET_UTTERANCE_SELECT_LIST = 2 * 65536 + 17
#: Set background context.
DS_SET_BACKGROUND_CONTEXT = 2 * 65536 + 18
#: Clear background context.
DS_CLEAR_BACKGROUND_CONTEXT = 2 * 65536 + 19
# Enable Always Listen Mode.
DS_ENABLE_ALWAYS_LISTEN_MODE = 2 * 65536 + 20
# Reset Listen timeout.
DS_RESET_LISTEN_TIMEOUT = 2 * 65536 + 21
# Sentence input.
DS_SENTENCE_INPUT = 2 * 65536 + 22
# Get dialog scripts.
DS_GET_DIALOG_SCRIPTS = 2 * 65536 + 23
# Set all dialog scripts.
DS_SET_DIALOG_SCRIPTS = 2 * 65536 + 24
# Set dialog script by index.
DS_SET_DIALOG_SCRIPT_BY_INDEX = 2 * 65536 + 25
# Request system to check if the utterance is exist in utterance list.
DS_UTTERANCE_COLLISION_CHECK = 2 * 65536 + 26
# Dynamic control/builder intent.
DS_INTENT_CONTROL = 2 * 65536 + 27
# Update corpus by server.
DS_UPDATE_CORPUS_BY_SERVER = 2 * 65536 + 28
# Head key trigger enable/disable.
DS_TRIGGER_KEY = 2 * 65536 + 29
# Get word similarity.
DS_WORD_SIMILARITY = 2 * 65536 + 30
# Transform ZH to number.
DS_ZH_TO_NUMBER = 2 * 65536 + 31
# Config next CSR setting.
DS_CONFIG_NEXT_CSR = 2 * 65536 + 32
# Transform EN to number.
DS_EN_TO_NUMBER = 2 * 65536 + 33

# Adjust loop predefined action tempo
MOTION_ADJUST_LOOP_PREDEFINED_ACTION_TEMPO = 3 * 65536 + 1
# For CV SLAM only.
MOTION_ABS_MOVE_TO = 3 * 65536 + 2
# Set avoidance mode.
MOTION_SET_AVOIDANCE_MODE = 3 * 65536 + 3
# Set anti dropping.
MOTION_SET_ANTI_DROPPING = 3 * 65536 + 4
# Direct operate charging dock.
MOTION_OPERATE_CHARGING_DOCK = 3 * 65536 + 5
# Drive the robot to a given translational velocity (vx) and rotational
# speed (wz) within an interval (time).
MOTION_CTRL_BASE_VEL = 3 * 65536 + 6
# Get base wheel lock status.
MOTION_GET_BASE_WHEEL_LOCK_STATUS = 3 * 65536 + 7
#
MOTION_MOVE_BODY_WITHOUT_AVOIDANCE = 3 * 65536 + 8
#
MOTION_REMOTE_CONTROL_BODY_WITHOUT_AVOIDANCE = 3 * 65536 + 9
#
MOTION_CONTROL_BASE_VELOCITY_WITHOUT_AVOIDANCE = 3 * 65536 + 10
#
MOTION_EXCEPTION_HANDLER = 3 * 65536 + 11
#
MOTION_BUMPING_HANDLER = 3 * 65536 + 12
#: Motion remote control stop.
MOTION_REMOTE_CONTROL_BODY_STOP = 3 * 65536 + 13
#
MOTION_REMOTE_CONTROL_BODY_WITHOUT_AVOIDANCE_STOP = 3 * 65536 + 14
# Move from current position (xA, yA, thetaA) to a target (xB, yB, thetaB)
# based on the path-finding algorithm.
MOTION_CHECK_PATH_EXISTENCE = 3 * 65536 + 15
#: Motion remote control neck stop.
MOTION_REMOTE_CONTROL_HEAD_STOP = 3 * 65536 + 16
# Drive the robot to a given translational velocity (vx) and rotational
# speed (wz) within an interval (time).
MOTION_CTRL_BODY_VEL = 3 * 65536 + 17
# Ask motion service to calibrate color in line follower.
MOTION_CAL_SIMPLE_LINE_FOLLOWER = 3 * 65536 + 18
# Get anti dropping.
MOTION_GET_ANTI_DROPPING = 3 * 65536 + 19
# Set avoidance status.
MOTION_SET_AVOIDANCE = 3 * 65536 + 20
# Get avoidance status.
MOTION_GET_AVOIDANCE = 3 * 65536 + 21

# Internal use.
UTILITY_ACTION_LOOK_AT_USER = 4 * 65536 + 1
#: Send information to plug-in.
UTILITY_SEND_INFO = 4 * 65536 + 2
# Start part mode.
UTILITY_PARTY_MODE = 4 * 65536 + 3
#: Ask robot to look at user.
UTILITY_LOOK_AT_USER = 4 * 65536 + 11
#: Ask robot to find specified person nearby.
UTILITY_FIND_PERSON_NEARBY = 4 * 65536 + 12
#
UTILITY_COMPASS_CALIBRATION = 4 * 65536 + 13
#
UTILITY_COMPASS_ACCURACY = 4 * 65536 + 14
# Hey zenbo action.
UTILITY_HEY_ZENBO_ACTION = 4 * 65536 + 15
# Get last kidnap time.
UTILITY_GET_LAST_KIDNAP_TIME = 4 * 65536 + 16
# Show request map labeling UI.
UTILITY_REQUEST_MAP_LABELING = 4 * 65536 + 17
# Show go to hot spot UI.
UTILITY_GO_TO_HOT_SPOT_HANDLER = 4 * 65536 + 18
# Reset to default setting.
UTILITY_RESET_TO_DEFAULT_SETTING = 4 * 65536 + 19
# Operate charging dock from plug-in.
UTILITY_OPERATE_CHARGING_DOCK = 4 * 65536 + 20
# Recognize the user and learn.
UTILITY_WHO_AM_I = 4 * 65536 + 21
# Turn and recognize the user.
UTILITY_TURN_AND_REG_USER = 4 * 65536 + 22
#: Ask robot to track/follow face.
UTILITY_TRACK_FACE = 4 * 65536 + 23
#: Ask robot to walk around.
UTILITY_WALKING = 4 * 65536 + 24
#: Line follower's color identification.
UTILITY_LINE_FOLLOWER_COLOR_IDENTIFICATION = 4 * 65536 + 25
#: Line follower.
UTILITY_LINE_FOLLOWER = 4 * 65536 + 26
#: Ask robot to follow object.
UTILITY_FOLLOW_OBJECT = 4 * 65536 + 27
#: Ask robot to follow line by motion service algorithm.
UTILITY_SIMPLE_LINE_FOLLOWER = 4 * 65536 + 28
#: Ask line follower to do color calibrate.
UTILITY_LINE_FOLLOWER_COLOR_CALIBRATE = 4 * 65536 + 29
#: Ask robot to demo follow line.
UTILITY_DEMO_LINE_FOLLOWER = 4 * 65536 + 30

# Start led system pattern.
WHEEL_LIGHTS_SYSTEM_PATTERN = 5 * 65536 + 1
# Wheel lights override acquire.
WHEEL_LIGHTS_OVERRIDE_ACQUIRE = 5 * 65536 + 2
# Wheel lights override release.
WHEEL_LIGHTS_OVERRIDE_RELEASE = 5 * 65536 + 3

# Add new family member data.
CONTACTS_ADD_NEW_FAMILY = 6 * 65536 + 1
# Update family member data.
CONTACTS_UPDATE_FAMILY = 6 * 65536 + 2
# Create robot data.
CONTACTS_CREATE_ROBOT = 6 * 65536 + 3
# Delete family member data.
CONTACTS_DELETE_FAMILY = 6 * 65536 + 4

# Ask robot to get current location actively.
SLAM_ACTIVE_LOCALIZATION = 7 * 65536 + 1
# Ask robot current location.
SLAM_STOP_LOCALIZATION = 7 * 65536 + 2
# Ask robot current location.
SLAM_GET_LOCATION = 7 * 65536 + 3
# Ask robot to get current location actively with high accuracy.
SLAM_ACTIVE_PRECISE_LOCALIZATION = 7 * 65536 + 4

# Lock status/navigation bar.
EXTRA_LOCK_NAVIGATION_BAR = 8 * 65536 + 1
# Start face enroll progress.
START_FACE_ENROLL_PROGRESS = 8 * 65536 + 2
# Start voice enroll progress.
START_VOICE_ENROLL_PROGRESS = 8 * 65536 + 3
# Start picture enroll progress.
START_PICTURE_ENROLL_PROGRESS = 8 * 65536 + 4

#: Use Baidu AI to detect face from photo.
VISION_PROXY_BAIDU_DETECT_FACE_FROM_PHOTO = 9 * 65536 + 1
#: Use Baidu AI to recognize face from photo.
VISION_PROXY_BAIDU_RECOGNIZE_FACE_FROM_PHOTO = 9 * 65536 + 2
#: Use Baidu AI to recognize text from photo.
VISION_PROXY_BAIDU_RECOGNIZE_TEXT_FROM_PHOTO = 9 * 65536 + 3

#: Register capacity touch sensor event callback.
SENSOR_CAPACITY_TOUCH_EVENT_REGISTER = 10 * 65536 + 0 * 10 + 4
#: Unregister capacity touch sensor event callback.
SENSOR_CAPACITY_TOUCH_EVENT_UNREGISTER = 10 * 65536 + 0 * 10 + 5

#: Get sonar sensor value.
SENSOR_SONAR_GET = 10 * 65536 + 1 * 10 + 1
#: Register sonar sensor value callback.
SENSOR_SONAR_REGISTER = 10 * 65536 + 1 * 10 + 2
#: Unregister sonar sensor value callback.
SENSOR_SONAR_UNREGISTER = 10 * 65536 + 1 * 10 + 3
#: Register sonar sensor event callback.
SENSOR_SONAR_EVENT_REGISTER = 10 * 65536 + 1 * 10 + 4
#: Unregister sonar sensor event callback.
SENSOR_SONAR_EVENT_UNREGISTER = 10 * 65536 + 1 * 10 + 5

#: Get neck encoder sensor value.
SENSOR_NECK_ENCODER_GET = 10 * 65536 + 2 * 10 + 1
#: Register neck encoder sensor value callback.
SENSOR_NECK_ENCODER_REGISTER = 10 * 65536 + 2 * 10 + 2
#: Unregister neck encoder sensor value callback.
SENSOR_NECK_ENCODER_UNREGISTER = 10 * 65536 + 2 * 10 + 3
#: Register neck encoder sensor event callback.
SENSOR_NECK_ENCODER_EVENT_REGISTER = 10 * 65536 + 2 * 10 + 4
#: Unregister neck encoder sensor event callback.
SENSOR_NECK_ENCODER_EVENT_UNREGISTER = 10 * 65536 + 2 * 10 + 5

#: Register trigger key event callback.
SENSOR_TRIGGER_KEY_EVENT_REGISTER = 10 * 65536 + 3 * 10 + 4
#: Unregister trigger key event callback.
SENSOR_TRIGGER_KEY_EVENT_UNREGISTER = 10 * 65536 + 3 * 10 + 5

#: Register volume up key event callback.
SENSOR_VOLUME_UP_KEY_EVENT_REGISTER = 10 * 65536 + 4 * 10 + 4
#: Unregister volume up key event callback.
SENSOR_VOLUME_UP_KEY_EVENT_UNREGISTER = 10 * 65536 + 4 * 10 + 5

#: Register volume down key event callback.
SENSOR_VOLUME_DOWN_KEY_EVENT_REGISTER = 10 * 65536 + 5 * 10 + 4
#: Unregister volume down key event callback.
SENSOR_VOLUME_DOWN_KEY_EVENT_UNREGISTER = 10 * 65536 + 5 * 10 + 5

#: Get AC-plug status.
SYSTEM_AC_PLUG_STATUS_GET = 11 * 65536 + 0 * 10 + 1
#: Register AC-plug status callback.
SYSTEM_AC_PLUG_STATUS_REGISTER = 11 * 65536 + 0 * 10 + 2
#: Unregister AC-plug status callback.
SYSTEM_AC_PLUG_STATUS_UNREGISTER = 11 * 65536 + 0 * 10 + 3

#: Get battery status.
SYSTEM_BATTERY_STATUS_GET = 11 * 65536 + 1 * 10 + 1
#: Register battery status callback.
SYSTEM_BATTERY_STATUS_REGISTER = 11 * 65536 + 1 * 10 + 2
#: Unregister battery status callback.
SYSTEM_BATTERY_STATUS_UNREGISTER = 11 * 65536 + 1 * 10 + 3
#: Register battery event callback.
SYSTEM_BATTERY_STATUS_EVENT_REGISTER = 11 * 65536 + 1 * 10 + 4
#: Unregister battery event callback.
SYSTEM_BATTERY_STATUS_EVENT_UNREGISTER = 11 * 65536 + 1 * 10 + 5

#: Get media volume level.
SYSTEM_MEDIA_VOLUME_GET = 11 * 65536 + 2 * 10 + 1
#: Set media volume level.
SYSTEM_MEDIA_VOLUME_SET = 11 * 65536 + 2 * 10 + 2

#: Get text to speech volume level.
SYSTEM_TTS_VOLUME_GET = 11 * 65536 + 3 * 10 + 1
#: Set text to speech volume level.
SYSTEM_TTS_VOLUME_SET = 11 * 65536 + 3 * 10 + 2

#: Register monitor screen touch event.
SYSTEM_SCREEN_TOUCH_EVENT_REGISTER = 11 * 65536 + 4 * 10 + 4
#: Unregister monitor screen touch event.
SYSTEM_SCREEN_TOUCH_EVENT_UNREGISTER = 11 * 65536 + 4 * 10 + 5

#: Take picture.
MEDIA_TAKE_PICTURE = 12 * 65536 + 1
#: Record video.
MEDIA_RECORD_VIDEO = 12 * 65536 + 2
#: Record audio.
MEDIA_RECORD_AUDIO = 12 * 65536 + 3
#: Play media.
MEDIA_PLAY_MEDIA = 12 * 65536 + 4
#: Stop play media.
MEDIA_STOP_MEDIA = 12 * 65536 + 5
#: Get media file list.
MEDIA_GET_FILE_LIST = 12 * 65536 + 6
#: Stop record video.
MEDIA_STOP_RECORD_VIDEO = 12 * 65536 + 7
#: Stop record audio.
MEDIA_STOP_RECORD_AUDIO = 12 * 65536 + 8
