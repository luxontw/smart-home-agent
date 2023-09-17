import asyncio
import os

from homeassistant_api import Client

url = os.getenv("HOMEASSISTANT_API_ENDPOINT")
token = os.getenv("HOMEASSISTANT_API_TOKEN")


async def main():
    client = Client(url, token, use_async=True)
    async with client:
        service = await client.async_get_domain("light") 
        print(service.services.keys())
        await service.toggle(entity_id="light.midesklamp1s_4e36")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
