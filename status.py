import asyncio
import os
import datetime

from homeassistant_api import Entity, State

url = os.getenv("HOMEASSISTANT_API_ENDPOINT")
token = os.getenv("HOMEASSISTANT_API_TOKEN")

object = {
    'object_name': 'person',
    'iot_20230726': Entity(
        slug='iot_20230726',
        state=State(
            entity_id='person.iot_20230726',
            state='home',
            attributes={
                'editable': True,
                'id': 'iot_20230726',
                'latitude': 24.570246,
                'longitude': 120.8111571,
                'gps_accuracy': 14,
                'source': 'device_tracker.in2015',
                'user_id': 'abdd7fe7a32a44258f3a06e29a0ae095',
                'device_trackers': ['device_tracker.in2015'],
                'friendly_name': 'iot_20230726'
            },
            last_changed=datetime.datetime(
                2023, 8, 16, 15, 35, 1, 18543,
                tzinfo=datetime.timezone.utc
            ),
            last_updated=datetime.datetime(
                2023, 8, 16, 16, 12, 45, 458027,
                tzinfo=datetime.timezone.utc
            ),
            context=Context(
                id='01H7ZHXWGJCXQNNNW1QEKS1VE4'
            )
        )
    ),
    'guest': Entity(
        slug='guest',
        state=State(
            entity_id='person.guest',
            state='unknown',
            attributes={
                'editable': True,
                'id': 'guest',
                  'user_id': 'bd9701b3f54843439e5a8aa7f844215b',
                'device_trackers': [],
                'friendly_name': 'guest'
            },
            last_changed=datetime.datetime(
                2023, 8, 16, 15, 35, 1, 19780,
                tzinfo=datetime.timezone.utc
            ),
            last_updated=datetime.datetime(
                2023, 8, 16, 15, 35, 57, 728704,
                tzinfo=datetime.timezone.utc
            ),
            context=Context(
                id='01H7ZFTGH038ZACDFBSK1K3Z2Q'
            )
        )
    )
}

object = {
    'kong_qi_jing_hua_qi_buzzer': Entity(
        slug='kong_qi_jing_hua_qi_buzzer',
        state=State(
            entity_id='switch.kong_qi_jing_hua_qi_buzzer',
            state='off',
            attributes={
                  'icon': 'mdi:volume-high',
                'friendly_name':
                      '空氣淨化器 Buzzer'
            },
            last_changed=datetime.datetime(
                2023, 8, 16, 15, 35, 55, 986432,
                tzinfo=datetime.timezone.utc
            ),
            last_updated=datetime.datetime(
                2023, 8, 16, 15, 35, 55, 986432,
                tzinfo=datetime.timezone.utc
            ),
            context=Context(
                id='01H7ZFTETJFCS836DRMGVW5Q7X'
            )
        )
    ),
    'kong_qi_jing_hua_qi_child_lock': Entity(
        slug='kong_qi_jing_hua_qi_child_lock',
        state=State(
            entity_id='switch.kong_qi_jing_hua_qi_child_lock',
            state='off',
            attributes={
                'icon': 'mdi:lock',
                'friendly_name': '空氣淨化器 Child lock'
            },
            last_changed=datetime.datetime(
                2023, 8, 16, 15, 35, 55, 987580,
                tzinfo=datetime.timezone.utc
            ),
            last_updated=datetime.datetime(
                2023, 8, 16, 15, 35, 55, 987580,
                tzinfo=datetime.timezone.utc
            ),
            context=Context(
                id='01H7ZFTETK3YTYMZDEBCW3ZK0G'
            )
        )
    ), 'kong_qi_jing_hua_qi_led': Entity(
        slug='kong_qi_jing_hua_qi_led',
        state=State(
            entity_id='switch.kong_qi_jing_hua_qi_led',
            state='off',
            attributes={
                'icon': 'mdi:led-outline',
                'friendly_name': '空氣淨化器 LED'
            },
            last_changed=datetime.datetime(
                2023, 8, 16, 15, 35, 55, 988711,
                tzinfo=datetime.timezone.utc
            ),
            last_updated=datetime.datetime(
                2023, 8, 16, 15, 35, 55, 988711,
                tzinfo=datetime.timezone.utc
            ),
            context=Context(
                id='01H7ZFTETMMA0GGHC97E9K2193'
            )
        )
    ),
    'kong_qi_jing_hua_qi_learn_mode': Entity(
        slug='kong_qi_jing_hua_qi_learn_mode',
        state=State(
            entity_id='switch.kong_qi_jing_hua_qi_learn_mode',
            state='off',
            attributes={
                'icon': 'mdi:school-outline',
                'friendly_name': '空氣淨化器 Learn mode'
            },
            last_changed=datetime.datetime(
                2023, 8, 16, 15, 35, 55, 989890,
                tzinfo=datetime.timezone.utc
            ),
            last_updated=datetime.datetime(
                2023, 8, 16, 15, 35, 55, 989890,
                tzinfo=datetime.timezone.utc
            ),
            context=Context(
                id='01H7ZFTETN8HEAGBPMFQG40G2R'
            )
        )
    ),
    'dian_feng_shan_socket_1': Entity(
        slug='dian_feng_shan_socket_1',
        state=State(
            entity_id='switch.dian_feng_shan_socket_1',
            state='on',
            attributes={
                'device_class': 'outlet',
                'friendly_name': '電風扇'
            },
            last_changed=datetime.datetime(
                2023, 8, 16, 15, 35, 57, 84905,
                tzinfo=datetime.timezone.utc
            ),
            last_updated=datetime.datetime(
                2023, 8, 16, 15, 35, 57, 84905,
                tzinfo=datetime.timezone.utc
            ),
            context=Context
            (id='01H7ZFTFWWRSX0G8XY1EQPRR00'
             )
        )
    ),
    'espresense_wo_shi_auto_update': Entity(
        slug='espresense_wo_shi_auto_update',
        state=State(
            entity_id='switch.espresense_wo_shi_auto_update',
            state='off',
            attributes={
                'friendly_name': 'ESPresense 臥室 Auto Update'
            },
            last_changed=datetime.datetime(
                2023, 8, 16, 15, 36, 1, 355105,
                tzinfo=datetime.timezone.utc
            ),
            last_updated=datetime.datetime(
                2023, 8, 16, 15, 36, 1, 355105,
                tzinfo=datetime.timezone.utc
            ),
            context=Context(
                id='01H7ZFTM2BM6EZA4YYQ0E9H214'
            )
        )
    ),
    'espresense_wo_shi_arduino_ota': Entity(
        slug='espresense_wo_shi_arduino_ota',
        state=State(
            entity_id='switch.espresense_wo_shi_arduino_ota',
            state='off',
            attributes={
                'friendly_name': 'ESPresense 臥室 Arduino OTA'
            },
            last_changed=datetime.datetime(
                2023, 8, 16, 15, 36, 1, 356131,
                tzinfo=datetime.timezone.utc
            ),
            last_updated=datetime.datetime(
                2023, 8, 16, 15, 36, 1, 356131,
                tzinfo=datetime.timezone.utc
            ),
            context=Context(
                id='01H7ZFTM2CEN2GDPVHV55R0X4P'
            )
        )
    ),
    'espresense_wo_shi_prerelease': Entity(
        slug='espresense_wo_shi_prerelease',
        state=State(
            entity_id='switch.espresense_wo_shi_prerelease',
            state='off',
            attributes={
                'friendly_name': 'ESPresense 臥室 Prerelease'
            },
            last_changed=datetime.datetime(
                2023, 8, 16, 15, 36, 1, 366631,
                tzinfo=datetime.timezone.utc
            ), last_updated=datetime.datetime(
                2023, 8, 16, 15, 36, 1, 366631,
                tzinfo=datetime.timezone.utc
            ), context=Context(
                id='01H7ZFTM2PSJJP7KQ4VGKZDSVG'
            )
        )
    ),
    'gpu_server': Entity(
        slug='gpu_server',
        state=State(
            entity_id='switch.gpu_server',
            state='unavailable',
            attributes={
                'restored': True,
                'friendly_name': 'Linux PC',
                'supported_features': 0
            },
            last_changed=datetime.datetime(
                2023, 8, 16, 15, 35, 57, 724265,
                tzinfo=datetime.timezone.utc
            ),
            last_updated=datetime.datetime(
                2023, 8, 16, 15, 35, 57, 724265,
                tzinfo=datetime.timezone.utc
            ),
            context=Context(
                id='01H7ZFTGGWNSQ52PBDZ35CTWTB'
            )
        )
    )
}
