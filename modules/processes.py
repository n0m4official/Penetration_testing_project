import platform
import os
from core.logger import log_action

def simulate_process_discovery(stealth_mode, update_gui_logger):
    try:
        cmd = "tasklist" if platform.system() == "Windows" else "ps -aux"
        processes = os.popen(cmd).read()
        with open("process_discovery.txt", "w") as f:
            f.write(processes)
        log_action("Simulated process discovery.")
    except Exception as e:
        log_action(f"Process discovery failed: {e}")