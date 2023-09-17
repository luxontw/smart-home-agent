
import asyncio
import os

from homeassistant_api import Client

url = os.getenv("HOMEASSISTANT_API_ENDPOINT")
token = os.getenv("HOMEASSISTANT_API_TOKEN")


async def main():
    client = Client(url, token, use_async=True)
    async with client:
        data = await client.async_check_api_config()
        print(data)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())