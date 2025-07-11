import os
import platform
from core.logger import log_action

def simulate_process_discovery(stealth_mode=False, gui_callback=None):
    try:
        cmd = "tasklist" if platform.system() == "Windows" else "ps aux"
        processes = os.popen(cmd).read()

        # Save to file
        with open("process_discovery.txt", "w") as f:
            f.write(processes)

        log_action("Simulated process discovery.", stealth_mode, gui_callback)
    except Exception as e:
        log_action(f"Process discovery simulation failed: {e}", stealth_mode, gui_callback)
