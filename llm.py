from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


chat = ChatOpenAI(temperature=0.0)


def execute_command(command):
    template_string = """ \
    You are an Al that controls a smart home. \
    Here is the state of the devices in the home, \
    in JSON format. ```{device_status}``` \
    The user issues the command: {user_command}. \
    Change the device state as appropriate. \
    The following are the effects that can be used with led strip: Akemi,Android,Aurora,Black Hole,Blends,Blink,Blink Rainbow,Blobs,Blurz,Bouncing Balls,Bpm,Breathe,Candle,Candle Multi,Chase, \
    choose a suitable one as a led strip effect. \
    Provide your response in JSON format.
    """
    user_command = command
    # device_status = """ \
    # { \
    #     "user": { \
    #         "location": "living_room" \
    #     }, \
    #     "devices": { \
    #         "living_room": { \
    #             "lights": { \
    #                 "overhead": { \
    #                     "state": "on" \
    #                 }, \
    #                 "lamp": { \
    #                     "state": "off" \
    #                 } \
    #             }, \
    #             "tvs": { \
    #                 "living_room_tv": { \
    #                     "state": "off", \
    #                     "volume": 0 \
    #                 } \
    #             }, \
    #             "speakers": { \
    #                 "living_room_speaker": { \
    #                     "state": "on", \
    #                     "volume": 0 \
    #                 } \
    #             } \
    #         }, \
    #         "bedroom": { \
    #             "lights": { \
    #                 "bedside_lamp": { \
    #                     "state": "on" \
    #                 } \
    #             } \
    #         } \
    #     } \
    # }
    # """

    device_status = """ \
    { \
        "devices": { \
            "living_room": { \
                "lights": { \
                    "led_strip": { \
                        "state": "turn_off" \
                        "brightness": 0 \
                        "rgb_color": [0, 0, 0] \
                        "effect": "Solid" \
                    } \
                } \
            } \
        } \
    }
    """

    prompt_template = ChatPromptTemplate.from_template(template_string)
    status_update_prompt = prompt_template.format_messages(
        user_command=user_command, device_status=device_status
    )

    status_update = chat(status_update_prompt)
    print(status_update.content)
    return status_update.content
