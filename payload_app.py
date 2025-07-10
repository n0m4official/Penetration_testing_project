import os
import subprocess
import platform
import socket
import json
import zipfile
import sys
import time
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime

# ---------------- Setup ----------------
session_log = []
stealth_mode = False
timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = f"log_{timestamp_str}.txt"

def update_gui_log(message):
    if log_text:
        log_text.config(state="normal")
        log_text.insert(tk.END, message + "\n")
        log_text.see(tk.END)
        log_text.config(state="disabled")

def log_action(message):
    with open(log_filename, "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")
    session_log.append({"timestamp": datetime.now().isoformat(), "event": message})
    if not stealth_mode:
        update_gui_log(f"{datetime.now().strftime('%H:%M:%S')} - {message}")

def write_json_log():
    json_filename = f"session_log_{timestamp_str}.json"
    with open(json_filename, "w") as json_file:
        json.dump(session_log, json_file, indent=4, default=str)

# ---------------- Simulations ----------------
def simulate_exfiltration():
    exfil_filename = f"exfil_payload_{timestamp_str}.zip"
    with zipfile.ZipFile(exfil_filename, 'w') as exfil_zip:
        for f in ["discovery_log.txt", "process_discovery.txt", "fake_credentials.txt", log_filename, f"session_log_{timestamp_str}.json"]:
            if os.path.exists(f):
                exfil_zip.write(f)
    log_action(f"Simulated exfiltration archive created: {exfil_filename}")

def simulate_persistence():
    log_action("Simulated persistence mechanism creation.")

def simulate_credential_harvesting():
    fake_creds = "username: admin\npassword: password123\n"
    with open("fake_credentials.txt", "w") as f:
        f.write(fake_creds)
    log_action("Simulated credential harvesting (fake file dropped).")

def simulate_discovery():
    info = f"System: {platform.system()} {platform.release()}\nNode: {platform.node()}\nUser: {os.getlogin()}\n"
    try:
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        info += f"IP: {ip_addr}\n"
    except:
        info += "IP: Unknown\n"
    with open("discovery_log.txt", "w") as f:
        f.write(info)
    log_action("Simulated system discovery.")

def drop_text_file():
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

def open_notepad():
    try:
        subprocess.Popen(["notepad.exe"])
        log_action("Opened Notepad.")
    except Exception as e:
        log_action(f"Failed to open Notepad: {e}")

def simulate_network_beacon():
    log_action("Simulated network beacon.")

def show_popup():
    try:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, "System breached (test message).", "PenTest Sim", 0)
        log_action("Displayed popup message.")
    except Exception as e:
        log_action(f"Popup failed: {e}")

def simulate_privilege_check():
    try:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin:
            log_action("Privilege check: running as admin.")
        else:
            log_action("Privilege check: not admin, would attempt escalation.")
    except:
        log_action("Privilege check: unavailable.")

def simulate_process_discovery():
    try:
        cmd = "tasklist" if platform.system() == "Windows" else "ps -aux"
        processes = os.popen(cmd).read()
        with open("process_discovery.txt", "w") as f:
            f.write(processes)
        log_action("Simulated process discovery.")
    except Exception as e:
        log_action(f"Process discovery failed: {e}")

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

def run_all_simulations():
    drop_text_file()
    open_notepad()
    simulate_network_beacon()
    show_popup()
    simulate_persistence()
    simulate_credential_harvesting()
    simulate_discovery()
    simulate_privilege_check()
    simulate_process_discovery()
    simulate_exfiltration()
    log_action("All simulations run (GUI).")

# ---------------- GUI ----------------
def toggle_stealth():
    global stealth_mode
    stealth_mode = not stealth_mode
    stealth_btn.config(text=f"Stealth Mode: {'ON' if stealth_mode else 'OFF'}")
    log_action(f"Stealth mode toggled to {'ON' if stealth_mode else 'OFF'}.")

def run_action_threaded(action_func):
    t = threading.Thread(target=action_func)
    t.start()

# Dark mode colors
DARK_BG = "#2e2e2e"
DARK_BTN_BG = "#3c3f41"
DARK_BTN_ACTIVE = "#505357"
LIGHT_TEXT = "#e1e1e1"
ACCENT_COLOR = "#61afef"

root = tk.Tk()
root.title("PenTest Simulation")
root.geometry("750x600")
root.configure(bg=DARK_BG)

header = tk.Label(root, text="PenTest Simulation", font=("Courier", 16, "bold"),
                  bg=DARK_BG, fg=ACCENT_COLOR)
header.pack(pady=10)

btn_frame = tk.Frame(root, bg=DARK_BG)
btn_frame.pack()

actions = [
    ("Drop Notice File", drop_text_file),
    ("Open Notepad", open_notepad),
    ("Network Beacon", simulate_network_beacon),
    ("Show Popup", show_popup),
    ("Persistence", simulate_persistence),
    ("Credential Harvest", simulate_credential_harvesting),
    ("Discovery", simulate_discovery),
    ("Privilege Check", simulate_privilege_check),
    ("Process Discovery", simulate_process_discovery),
    ("Exfiltration", simulate_exfiltration),
    ("Run All", run_all_simulations)
]

for text, func in actions:
    b = tk.Button(btn_frame, text=text, width=20,
                  command=lambda f=func: run_action_threaded(f),
                  bg=DARK_BTN_BG, fg=LIGHT_TEXT, activebackground=DARK_BTN_ACTIVE,
                  activeforeground=LIGHT_TEXT, relief="flat")
    b.pack(pady=2)

stealth_btn = tk.Button(root, text="Stealth Mode: OFF", width=20,
                       command=toggle_stealth,
                       bg=DARK_BTN_BG, fg=LIGHT_TEXT, activebackground=DARK_BTN_ACTIVE,
                       activeforeground=LIGHT_TEXT, relief="flat")
stealth_btn.pack(pady=5)

report_btn = tk.Button(root, text="Generate Report & Exit", width=25,
                       command=lambda: [generate_report(), root.destroy()],
                       bg=ACCENT_COLOR, fg=DARK_BG, activebackground="#5190e3",
                       activeforeground=DARK_BG, relief="flat")
report_btn.pack(pady=10)

log_text = scrolledtext.ScrolledText(root, state="disabled", height=15,
                                     bg="#1e1e1e", fg=LIGHT_TEXT, insertbackground=LIGHT_TEXT,
                                     relief="flat", borderwidth=0)
log_text.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()