import json
from config import MIMO_VERSION
from fake_login import fake_login
from validate_token import validate_token
from build_mimo_prompt import build_mimo_prompt
from mimo import mimo

def run_pipeline(english_command: str, gateway_id: str = "gw_kathmandu_home"):
    print(f"\n{'='*50}\n  {MIMO_VERSION} | {english_command}\n{'='*50}")

    token         = fake_login("user_001")
    claims        = validate_token(token)
    system_prompt = build_mimo_prompt(claims["sub"], gateway_id)

    print(f"[PROFILE] Loaded {gateway_id}")
    result = mimo(system_prompt, english_command)
    print(f"[ACTION]\n{json.dumps(result, indent=2)}")
    return result

if __name__ == "__main__":
    run_pipeline("Turn off the living room light")
    run_pipeline("Is the front door locked?")
    run_pipeline("Turn on the garden light", gateway_id="gw_pokhara_house")
    run_pipeline("Turn everything off")
    run_pipeline("Set the AC to 22 degrees")

