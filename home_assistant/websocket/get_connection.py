import asyncio
import os
import json
import websockets


def auth():
    return json.dumps(
        {"type": "auth", "access_token": os.getenv("HOMEASSISTANT_WEBSOCKET_TOKEN")}
    )


def settings():
    return json.dumps(
        {
            "id": 26,
            "type": "call_service",
            "domain": "light",
            "service": "turn_off",
            "target": {"entity_id": "light.midesklamp1s_4e36"},
        }
    )


async def hello():
    uri = os.getenv("HOMEASSISTANT_WEBSOCKET_ENDPOINT")
    async with websockets.connect(uri) as websocket:
        greeting = await websocket.recv()
        print(f"< {greeting}")
        await websocket.send(auth())
        greeting = await websocket.recv()
        print(f"< {greeting}")
        await websocket.send(settings())
        greeting = await websocket.recv()
        print(f"< {greeting}")


asyncio.get_event_loop().run_until_complete(hello())
