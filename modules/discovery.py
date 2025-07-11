import os
import platform
import socket
from datetime import datetime
from core.logger import log_action

def simulate_discovery(stealth_mode=False, gui_callback=None):
    try:
        info = f"System: {platform.system()} {platform.release()}\n"
        info += f"Node: {platform.node()}\n"
        info += f"User: {os.getlogin()}\n"

        try:
            hostname = socket.gethostname()
            ip_addr = socket.gethostbyname(hostname)
            info += f"IP Address: {ip_addr}\n"
        except:
            info += "IP Address: Unknown\n"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"discovery_log_{timestamp}.txt"

        with open(filename, "w") as f:
            f.write(info)

        log_action(f"Simulated system discovery. Info saved to: {filename}", stealth_mode, gui_callback)
    except Exception as e:
        log_action(f"Discovery failed: {e}", stealth_mode, gui_callback)
