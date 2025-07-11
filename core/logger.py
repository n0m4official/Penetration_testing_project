import json
from datetime import datetime
import threading
import logging

session_log = []
lock = threading.Lock()

timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = f"log_{timestamp_str}.txt"
json_filename = f"session_log_{timestamp_str}.json"

logger = logging.getLogger("PenTestSim")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_filename)
formatter = logging.Formatter('%(asctime)s - %(message)s')
logger.addHandler(file_handler)

def log_action(message, stealth_mode=False, gui_callback=None):
    with lock:
        logger.info(message)
        session_log.append({"timestamp": datetime.now().isoformat(), "event": message})
        if not stealth_mode and gui_callback:
            gui_callback(f"{datetime.now().strftime('%H:%M:%S')} - {message}")

def write_json_log():
    with lock:
        with open(json_filename, "w") as json_file:
            json.dump(session_log, json_file, indent=4, default=str)