import asyncio
import os
import json
import websockets

index = 0


def auth():
    return json.dumps(
        {"type": "auth", "access_token": os.getenv("HOMEASSISTANT_WEBSOCKET_TOKEN")}
    )


def get_states():
    global index
    index += 1
    return json.dumps({"id": index, "type": "get_states"})


def call_service(brightness,  rgb_color, effect):
    global index
    index += 1
    return json.dumps(
        {
            "id": 67,
            "type": "call_service",
            "domain": "light",
            "service": "turn_on",
            "service_data": {
                "brightness": brightness,
                "rgb_color": rgb_color,
                "effect": effect,
            },
            "target": {"entity_id": "light.wled"},
        }
    )


async def main():
    uri = os.getenv("HOMEASSISTANT_WEBSOCKET_ENDPOINT")
    async with websockets.connect(uri) as websocket:
        response = await websocket.recv()
        print(f"HA Info: {response}")
        await websocket.send(auth())
        response = await websocket.recv()
        print(f"HA Info: {response}")

        await websocket.send(get_states())
        states = await websocket.recv()
        states = json.loads(states)
        print(states["result"][32]["attributes"]["effect_list"])

        await websocket.send(call_service("80",  ["255", "100", "100"], "Soap"))

asyncio.get_event_loop().run_until_complete(main())
