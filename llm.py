import os


from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


chat = ChatOpenAI(temperature=0.0)


template_string = """ \
You are an Al that controls a smart home. \
Here is the state of the devices in the home, \
in JSON format. ```{device_status}``` \
The user issues the command: {user_command}. \
Change the device state as appropriate. \
Provide your response in JSON format.
"""
user_command = """get ready for a party"""

device_status = """ \
{ \
    "user": { \
        "location": "living_room" \
    }, \
    "devices": { \
        "living_room": { \
            "lights": { \
                "overhead": { \
                    "state": "off" \
                }, \
                "lamp": { \
                    "state": "off" \
                } \
            }, \
            "tvs": { \
                "living_room_tv": { \
                    "state": "off", \
                    "volume": 0 \
                } \
            }, \
            "speakers": { \
                "living_room_speaker": { \
                    "state": "off", \
                    "volume": 0 \
                } \
            } \
        }, \
        "bedroom": { \
            "lights": { \
                "bedside_lamp": { \
                    "state": "off" \
                } \
            } \
        } \
    } \
}
"""

prompt_template = ChatPromptTemplate.from_template(template_string)
status_update_prompt = prompt_template.format_messages(
                       user_command=user_command,
                       device_status=device_status)

status_update = chat(status_update_prompt)
print(status_update.content)