from core.logger import log_action, write_json_log, session_log
import os
import subprocess
from datetime import datetime

def simulate_privilege_check(stealth_mode, update_gui_log):
    try:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin:
            log_action("Privilege check: running as admin.")
        else:
            log_action("Privilege check: not admin, would attempt escalation.")
    except:
        log_action("Privilege check: unavailable.")

def show_popup(stealth_mode, update_gui_log):
    try:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, "System breached (test message).", "PenTest Sim", 0)
        log_action("Displayed popup message.")
    except Exception as e:
        log_action(f"Popup failed: {e}")

def drop_text_file(stealth_mode, update_gui_log):
    message = (
        "This was a test.\n"
        "If you're reading this, a vulnerability was discovered in your system.\n"
        "This is the log documenting how the program compromised the system.\n"
        "Had this been a real threat, this system would be compromised.\n"
    )
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"breach_notice_{timestamp}.txt"

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    if not os.path.exists(desktop):
        desktop = os.getcwd()
    filepath = os.path.join(desktop, filename)
    with open(filepath, "w") as file:
        file.write(message)

    log_action(f"Dropped breach notice file at: {filepath}")

def open_notepad(stealth_mode, update_gui_log):
    try:
        subprocess.Popen(["notepad.exe"])
        log_action("Opened Notepad.")
    except Exception as e:
        log_action(f"Failed to open Notepad: {e}")

def simulate_network_beacon(stealth_mode, update_gui_log):
    log_action("Simulated network beacon.")

def generate_report():
    with open("final_report.txt", "w") as report:
        report.write("Penetration Test Simulation Report\n")
        report.write("="*40 + "\n")
        for entry in session_log:
            report.write(f"- {entry}\n")
        report.write("\nSummary:\nThis was a simulated test. No harm was done to the system. All actions were educational.\n")
        report.write("Recommendations:\n- Review logs and detect these activities with EDR or AV solutions.\n- Regularly audit startup entries.\n- Monitor unexpected network connections.\n- Educate staff on phishing risks.\n")
    write_json_log()
    log_action("Final report generated.")