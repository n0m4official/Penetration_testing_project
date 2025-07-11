from core.logger import log_action
from core.utils import drop_text_file, simulate_privilege_check, show_popup, open_notepad,simulate_network_beacon
from modules.discovery import simulate_discovery
from modules.exfiltration import simulate_exfiltration
from modules.credentials import simulate_credential_harvesting
from modules.persistence import simulate_persistence
from modules.processes import simulate_process_discovery

def run_all_simulations(stealth_mode, update_gui_log):
    drop_text_file(stealth_mode, update_gui_log)
    open_notepad(stealth_mode, update_gui_log)
    simulate_network_beacon(stealth_mode, update_gui_log)
    show_popup(stealth_mode, update_gui_log)
    simulate_persistence(stealth_mode, update_gui_log)
    simulate_credential_harvesting(stealth_mode, update_gui_log)
    simulate_discovery(stealth_mode, update_gui_log)
    simulate_privilege_check(stealth_mode, update_gui_log)
    simulate_process_discovery(stealth_mode, update_gui_log)
    simulate_exfiltration(stealth_mode, update_gui_log)