import zipfile
import os
from core.logger import log_action, timestamp_str

def simulate_exfiltration(stealth_mode=False, gui_callback=None):
    exfil_filename = f"exfil_payload_{timestamp_str}.zip"
    with zipfile.ZipFile(exfil_filename, 'w') as exfil_zip:
        for f in ["discovery_log.txt", "process_discovery.txt", "fake_credentials.txt", f"log_{timestamp_str}.txt", f"session_log_{timestamp_str}.json"]:
            if os.path.exists(f):
                exfil_zip.write(f)
    log_action(f"Simulated exfiltration archive created: {exfil_filename}", stealth_mode, gui_callback)
