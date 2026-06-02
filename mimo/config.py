import jwt
import time
import json
from groq import Groq
import os

MIMO_VERSION = "MiMo v0.1"
CLIENT_ID    = "malati_mobile_v1"
JWT_SECRET   = "super-secret-mimo-key-change-me!!"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

FAKE_USER_DB = {
    "user_001": {
        "name": "Hari Prasad",
        "gateways": {
            "gw_kathmandu_home": {
                "label": "Kathmandu Home",
                "devices": [
                    {"id": "dev_01", "name": "Living Room Light", "type": "light",      "state": "on"},
                    {"id": "dev_02", "name": "Front Door Lock",   "type": "lock",       "state": "locked"},
                    {"id": "dev_03", "name": "AC Unit",           "type": "thermostat", "state": "off"},
                ]
            },
            "gw_pokhara_house": {
                "label": "Pokhara House",
                "devices": [
                    {"id": "dev_10", "name": "Garden Light", "type": "light", "state": "off"},
                    {"id": "dev_11", "name": "Main Gate",    "type": "lock",  "state": "locked"},
                ]
            }
        }
    }
}
