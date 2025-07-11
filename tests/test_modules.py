from core.utils import drop_text_file
from modules.discovery import simulate_discovery
from modules.exfiltration import simulate_exfiltration
from modules.credentials import simulate_credential_harvesting
from modules.persistence import simulate_persistence
from modules.processes import simulate_process_discovery

def run_all_simulations(stealth_mode=False, gui_callback=None):
    drop_text_file(stealth_mode, gui_callback)
#    open_notepad(stealth_mode, gui_callback)
#    simulate_network_beacon(stealth_mode, gui_callback)
#    show_popup(stealth_mode, gui_callback)
    simulate_persistence(stealth_mode, gui_callback)
    simulate_credential_harvesting(stealth_mode, gui_callback)
    simulate_discovery(stealth_mode, gui_callback)
#    simulate_privilege_check(stealth_mode, gui_callback)
    simulate_process_discovery(stealth_mode, gui_callback)
    simulate_exfiltration(stealth_mode, gui_callback)
