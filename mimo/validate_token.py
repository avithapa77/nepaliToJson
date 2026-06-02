
"""
auth.py — runs on the BACKEND SERVER
Called at the start of EVERY request from the mobile app.
 
Flow:
  1. Mobile app sends: JWT token + english command + GPS coords
  2. Backend calls validate_token() FIRST before anything else
  3. If valid → extract user_id and continue pipeline
  4. If invalid/expired → reject immediately, return 401 error
"""
import jwt
from config import JWT_SECRET
 
def validate_token(token: str) -> dict:
    """
    Security gate — nothing runs until this passes.
    Returns the token payload (user_id, client_id) if valid.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        print(f"[AUTH] Valid — user: {payload['sub']}, client: {payload['client_id']}")
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token expired — user must log in again")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token — rejected")