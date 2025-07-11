import json
from datetime import datetime

session_log = []
timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = f"log_{timestamp_str}.txt"

def log_action(message, stealth_mode=False, gui_callback=None):
    with open(log_filename, "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")
    session_log.append({"timestamp": datetime.now().isoformat(), "event": message})
    
    # Only call GUI callback if provided
    if not stealth_mode and gui_callback:
        gui_callback(f"{datetime.now().strftime('%H:%M:%S')} - {message}")

def write_json_log():
    json_filename = f"session_log_{timestamp_str}.json"
    with open(json_filename, "w") as json_file:
        json.dump(session_log, json_file, indent=4, default=str)
