import os
import subprocess
from datetime import datetime
from core.logger import log_action, write_json_log

def generate_report(stealth_mode=False, gui_callback=None):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"final_report_{timestamp}.txt"

    with open(report_filename, "w") as report:
        report.write("Penetration Test Simulation Report\n")
        report.write("=" * 50 + "\n")
        # In a full design, you'd loop over session logs or events
        report.write("This is a summary report of simulated actions.\n")
        report.write("Review logs and consider recommendations for hardening.\n")
    
    write_json_log()
    log_action(f"Final report generated: {report_filename}", stealth_mode, gui_callback)

def drop_text_file(stealth_mode=False, gui_callback=None):
    message = (
        "This is a simulated breach notice.\n"
        "Had this been a real scenario, your system would have been compromised.\n"
        "Review your defenses carefully.\n"
    )
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"breach_notice_{timestamp}.txt"

    # Try dropping to Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    if not os.path.exists(desktop_path):
        desktop_path = os.getcwd()

    filepath = os.path.join(desktop_path, filename)
    with open(filepath, "w") as file:
        file.write(message)
    
    log_action(f"Breach notice file dropped at: {filepath}", stealth_mode, gui_callback)