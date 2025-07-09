import os
import subprocess
import platform
import socket
from datetime import datetime

session_log = []

def log_action(message):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")
    session_log.append(message)

def simulate_persistence():
    print("[SIMULATION] Would create startup registry entry or scheduled task to persist.")
    log_action("Simulated persistence mechanism creation.")

def simulate_credential_harvesting():
    fake_creds = "username: admin\npassword: password123\n"
    with open("fake_credentials.txt", "w") as f:
        f.write(fake_creds)
    print("[SIMULATION] Fake credentials file created.")
    log_action("Simulated credential harvesting, fake file dropped.")

def simulate_discovery():
    info = f"System: {platform.system()} {platform.release()}\n"
    info += f"Node: {platform.node()}\n"
    info += f"User: {os.getlogin()}\n"
    try:
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        info += f"IP: {ip_addr}\n"
    except:
        info += "IP: Unknown\n"
    
    with open("discovery_log.txt", "w") as f:
        f.write(info)
    
    print("[SIMULATION] System discovery log created.")
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
    filepath = os.path.join(desktop, filename)

    with open(filepath, "w") as file:
        file.write(message)
    
    print(f"[+] Notice file created at: {filepath}")
    log_action("Dropped breach notice file on Desktop")

def open_notepad():
    subprocess.Popen(["notepad.exe"])
    print("[+] Notepad opened.")
    log_action("Opened Notepad.")

def simulate_network_beacon():
    # Simulated by printing and logging for now
    print("[+] Simulated network beacon to attacker C2 server.")
    log_action("Simulated network beacon.")

def show_popup():
    try:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, "System breached (test message).", "PenTest Sim", 0)
        print("[+] Popup message displayed.")
        log_action("Displayed popup message.")
    except Exception as e:
        print("[-] Popup message failed: ", e)
        log_action(f"Popup failed: {e}")

def simulate_privilege_check():
    try:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin:
            print("[SIMULATION] Running as admin (privilege escalation succeeded).")
            log_action("Privilege check: running as admin.")
        else:
            print("[SIMULATION] Not running as admin (would attempt escalation).")
            log_action("Privilege check: not admin, escalation would be attempted.")
    except:
        print("[SIMULATION] Privilege check unavailable on this OS.")
        log_action("Privilege check: unavailable.")

def simulate_process_discovery():
    try:
        if platform.system() == "Windows":
            cmd = "tasklist"
        else:
            cmd = "ps -aux"

        processes = os.popen(cmd).read()
        with open("process_discovery.txt", "w") as f:
            f.write(processes)
        print("[SIMULATION] Process list written to process_discovery.txt.")
        log_action("Simulated process discovery.")
    except Exception as e:
        print(f"[-] Process discovery failed: {e}")
        log_action(f"Process discovery failed: {e}")

def generate_report():
    with open("final_report.txt", "w") as report:
        report.write("Penetration Test Simulation Report\n")
        report.write("="*40 + "\n")
        for entry in session_log:
            report.write(f"- {entry}\n")
        report.write("\n")
        report.write("\nSummary:\n")
        report.write("This was a simulated test. No harm was done to the system. All actions were educational.\n")
        report.write("Recommendations:\n")
        report.write("- Review logs and detect these activities with EDR or AV solutions.\n")
        report.write("- Regularly audit startup entries and scheduled tasks.\n")
        report.write("- Monitor unexpected network connections.\n")
        report.write("- Educate staff on social engineering and phishing risks.\n")


def main_menu():
    while True:
        print("\n=== Penetration Test Simulation ===")
        print("1. Drop breach notice file")
        print("2. Open Notepad")
        print("3. Simulate network beacon")
        print("4. Show popup message")
        print("5. Simulate persistence")
        print("6. Simulate credential harvesting")
        print("7. Simulate system discovery")
        print("8. Simulate privilege check")
        print("9. Simulate process discovery")
        print("10. Exit and generate final report")
        choice = input("Select an option: ")

        if choice == "1":
            drop_text_file()
        elif choice == "2":
            open_notepad()
        elif choice == "3":
            simulate_network_beacon()
        elif choice == "4":
            show_popup()
        elif choice == "5":
            simulate_persistence()
        elif choice == "6":
            simulate_credential_harvesting()
        elif choice == "7":
            simulate_discovery()
        elif choice == "8":
            simulate_privilege_check()
        elif choice == "9":
            simulate_process_discovery()
        elif choice == "10":
            print("Exiting simulation and generating final report...")
            log_action("Simulation exited by user.")
            generate_report()
            print("Final report saved as final_report.txt")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    print("⚠️  WARNING: This is a harmless simulation tool for authorized educational use only.")
    print("Unauthorized use is unethical and may be illegal.\n")
    main_menu()