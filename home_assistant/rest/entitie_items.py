import asyncio
import os

from homeassistant_api import Client

url = os.getenv("HOMEASSISTANT_API_ENDPOINT")
token = os.getenv("HOMEASSISTANT_API_TOKEN")


async def main():
    client = Client(url, token, use_async=True)
    async with client:
        # data = await client.async_get_rendered_template("{{ areas() }}")
        data = await client.async_get_entities()

        for key, value in enumerate(data):
            print(key)
            print(value.group_id)
            print(value.entities)
            print(value._client)
            print("--------------------------------------------------")
        # print(data[17].entities["forecast_home"])
        # print(data[17].entities)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())