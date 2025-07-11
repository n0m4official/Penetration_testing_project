import tkinter as tk
from tkinter import scrolledtext
from core.logger import write_json_log
from core.utils import generate_report, drop_text_file
from modules.discovery import simulate_discovery
from modules.exfiltration import simulate_exfiltration
from modules.credentials import simulate_credential_harvesting
from modules.persistence import simulate_persistence
from modules.processes import simulate_process_discovery
from tests.test_modules import run_all_simulations

stealth_mode = False

def update_gui_log(message):
    log_text.config(state="normal")
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)
    log_text.config(state="disabled")

def toggle_stealth():
    global stealth_mode
    stealth_mode = not stealth_mode
    stealth_btn.config(text=f"Stealth Mode: {'ON' if stealth_mode else 'OFF'}")
    update_gui_log(f"Stealth mode toggled to {'ON' if stealth_mode else 'OFF'}.")

def run_action_threaded(func):
    import threading
    t = threading.Thread(target=func, args=(stealth_mode, update_gui_log))
    t.start()

def run_gui():
    global log_text, stealth_btn

    DARK_BG = "#2e2e2e"
    DARK_BTN_BG = "#3c3f41"
    DARK_BTN_ACTIVE = "#505357"
    LIGHT_TEXT = "#e1e1e1"
    ACCENT_COLOR = "#61afef"

    root = tk.Tk()
    root.title("PenTest Simulation")
    root.geometry("750x600")
    root.configure(bg=DARK_BG)

    header = tk.Label(root, text="PenTest Sim", font=("Courier", 16, "bold"),
                      bg=DARK_BG, fg=ACCENT_COLOR)
    header.pack(pady=10)

    btn_frame = tk.Frame(root, bg=DARK_BG)
    btn_frame.pack()

    actions = [
        ("Drop Notice File", drop_text_file),
    #    ("Open Notepad", open_notepad),                            [IMPLEMENT ASAP]
    #    ("Network Beacon", simulate_network_beacon),               [IMPLEMENT ASAP]
    #    ("Show Popup", show_popup),                                [IMPLEMENT ASAP]
        ("Persistence", simulate_persistence),
        ("Credential Harvest", simulate_credential_harvesting),
        ("Discovery", simulate_discovery),
    #    ("Privilege Check", simulate_privilege_check),             [IMPLEMENT ASAP]
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
                           command=lambda: [generate_report(), write_json_log(), root.destroy()],
                           bg=ACCENT_COLOR, fg=DARK_BG, activebackground="#5190e3",
                           activeforeground=DARK_BG, relief="flat")
    report_btn.pack(pady=10)

    log_text = scrolledtext.ScrolledText(root, state="disabled", height=15,
                                         bg="#1e1e1e", fg=LIGHT_TEXT, insertbackground=LIGHT_TEXT,
                                         relief="flat", borderwidth=0)
    log_text.pack(fill="both", expand=True, padx=10, pady=10)

    root.mainloop()
