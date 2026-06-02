import jwt
import time
from config import CLIENT_ID, JWT_SECRET

def fake_login(user_id: str) -> str:
    payload = {
        "sub":       user_id,
        "client_id": CLIENT_ID,
        "iat":       int(time.time()),
        "exp":       int(time.time()) + (30 * 24 * 60 * 60)  # 30 days
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    print(f"[AUTH] Token issued for {user_id}")
    return token


