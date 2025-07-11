import os
import zipfile
from datetime import datetime
from core.logger import log_action

def simulate_exfiltration(stealth_mode=False, gui_callback=None):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_name = f"exfil_payload_{timestamp}.zip"

        files_to_include = [
            "discovery_log.txt",
            "process_discovery.txt",
            "fake_credentials.txt",
            # Add your log files dynamically
        ]

        # Include logs from this session if they exist
        log_files = [f for f in os.listdir('.') if f.startswith("log_") and f.endswith(".txt")]
        json_logs = [f for f in os.listdir('.') if f.startswith("session_log_") and f.endswith(".json")]

        files_to_include.extend(log_files)
        files_to_include.extend(json_logs)

        with zipfile.ZipFile(archive_name, 'w') as zipf:
            for file in files_to_include:
                if os.path.exists(file):
                    zipf.write(file)

        log_action(f"Simulated exfiltration archive created: {archive_name}", stealth_mode, gui_callback)
    except Exception as e:
        log_action(f"Exfiltration failed: {e}", stealth_mode, gui_callback)
