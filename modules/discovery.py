import platform
import socket
import os
from core.logger import log_action

def simulate_discovery(stealth_mode=False, gui_callback=None):
    info = f"System: {platform.system()} {platform.release()}\nNode: {platform.node()}\nUser: {os.getlogin()}\n"
    try:
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        info += f"IP: {ip_addr}\n"
    except:
        info += "IP: Unknown\n"
    with open("discovery_log.txt", "w") as f:
        f.write(info)
    log_action("Simulated system discovery.", stealth_mode, gui_callback)
