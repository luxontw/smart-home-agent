from requests_cache import CachedSession
from datetime import timedelta
import os

from homeassistant_api import Client

url = os.getenv("HOMEASSISTANT_API_ENDPOINT")
token = os.getenv("HOMEASSISTANT_API_TOKEN")


client = Client(
    url,
    token,
    cache_session=CachedSession(
        backend="filesystem",
        expire_after=timedelta(minutes=5)
    )
)


with client:
    status = client.get_states()
    print(status)