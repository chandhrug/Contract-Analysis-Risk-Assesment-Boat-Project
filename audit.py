
import json
from datetime import datetime

def log_action(action, data):
    entry = {
        "timestamp": str(datetime.now()),
        "action": action,
        "data": data
    }
    with open("audit_log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
