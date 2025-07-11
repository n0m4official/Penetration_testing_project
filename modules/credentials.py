from core.logger import log_action

def simulate_credential_harvesting(stealth_mode=False, gui_callback=None):
    try:
        fake_creds = "username: admin\npassword: password123\n"

        with open("fake_credentials.txt", "w") as f:
            f.write(fake_creds)

        log_action("Simulated credential harvesting (fake file dropped).", stealth_mode, gui_callback)
    except Exception as e:
        log_action(f"Credential harvesting failed: {e}", stealth_mode, gui_callback)
