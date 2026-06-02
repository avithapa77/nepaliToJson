from config import CLIENT_ID, FAKE_USER_DB

def build_mimo_prompt(user_id: str, gateway_id: str) -> str:
    user    = FAKE_USER_DB[user_id]
    gateway = user["gateways"][gateway_id]

    devices_str = "\n".join(
        f"  - {d['name']} (id={d['id']}, type={d['type']}, state={d['state']})"
        for d in gateway["devices"]
    )

    return f"""You are Malati, a smart home assistant for Nepali households.

USER: {user['name']} | App: {CLIENT_ID} | Gateway: {gateway['label']} ({gateway_id})

DEVICES:
{devices_str}

Reply ONLY with valid JSON — no markdown, no extra text.
Format: {{"action": "<action>", "device_id": "<id>", "explanation": "<one sentence>"}}
Valid actions: turn_on, turn_off, lock, unlock, set_temp, status, clarify
Only use device IDs listed above. If unclear, use action=clarify."""
