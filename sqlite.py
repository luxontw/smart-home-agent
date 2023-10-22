import logging
import sqlite3
import asyncio
import json

import hass

LOGGER = logging.getLogger()


def init():
    global conn, cursor
    conn = sqlite3.connect("hass.db")
    cursor = conn.cursor()


def create_state_table():
    cursor.execute(
        "CREATE TABLE if not exists states(entity_id, friendly_name, state, attributes json)"
    )


def insert_state():
    states = asyncio.get_event_loop().run_until_complete(hass.get_all_states())
    data = []
    for state in states:
        friendly_name = state["attributes"]["friendly_name"] if "friendly_name" in state["attributes"] else None
        data.append(
            (state["entity_id"], state["state"], json.dumps(state["attributes"]))
        )
    print(data)
    cursor.executemany("INSERT INTO states VALUES(?, ?, ?, ?)", data)
    conn.commit()


def update_all_states():
    states = asyncio.get_event_loop().run_until_complete(hass.get_all_states())
    for state in states:
        cursor.execute(
            "UPDATE states SET state = ?, attributes = ? WHERE entity_id = ?",
            (state["state"], json.dumps(state["attributes"]), state["entity_id"]),
        )
    conn.commit()


def get_state(entity_id):
    cursor.execute(
        "SELECT state, attributes FROM states WHERE entity_id = ?", (entity_id,)
    )
    state, attributes = cursor.fetchone()
    return state, json.loads(attributes)


if __name__ == "__main__":
    from dotenv import load_dotenv
    import os

    load_dotenv()
    config = {
        "hass_endpoint": os.getenv("HOMEASSISTANT_WEBSOCKET_ENDPOINT"),
        "hass_token": os.getenv("HOMEASSISTANT_WEBSOCKET_TOKEN"),
        "debug": os.getenv("LOGGING_DEBUG"),
    }
    hass.init(config)
    init()
    create_state_table()
    update_all_states()
    print(get_state("light.led_strip"))
