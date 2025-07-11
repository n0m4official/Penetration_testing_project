from core.logger import log_action

def simulate_credential_harvesting(stealth_mode, update_gui_log):
    fake_creds = "username: admin\npassword: password123\n"
    with open("fake_credentials.txt", "w") as f:
        f.write(fake_creds)
    log_action("Simulated credential harvesting (fake file dropped).")