# Penetration Test Simulation Tool

⚠️ WARNING: This tool is for educational and authorized penetration testing simulation purposes only.  
It does not perform harmful actions or replicate actual malware behavior beyond harmless simulation.  
**Unauthorized use is unethical and may be illegal.**

--

## 💡 Overview

This Python-based simulation tool helps IT and security professionals demonstrate common attacker behaviors in a controlled, safe way.  
It simulates several typical "malware-like" actions without harming the system, providing logs and a final report for analysis.

---

## 🚀 Features

- Drop a harmless "breach notice" text file on the Desktop
- Open Notepad as a simulated payload
- Show a popup message box
- Simulate persistence mechanism setup
- Simulate credential harvesting (creates fake credentials file)
- Collect system discovery information
- Check for administrator privileges (simulated escalation check)
- List running processes cross-platform (Windows or Unix)
- Simulate a network beacon (logs only)
- Generate a final professional-style report summarizing activities

---

## 🗂️ Files generated

- `log.txt`: step-by-step log of all simulated actions
- `final_report.txt`: summary report for business or educational review
- `fake_credentials.txt`: example credential file
- `discovery_log.txt`: system info collected
- `process_discovery.txt`: running process list
- `breach_notice_<timestamp>.txt`: harmless breach notice on Desktop

--

## 💻 Usage

```bash
python penetration_sim.py
```
Follow the on-screen menu to select which simulated actions to run.

---

## ⚙️ Requirements
- Python 3.x
- Windows, Linux, or macOS
- On Windows: notepad.exe must be present (default)

---

## ✅ Recommended scenarios
- Educating staff or students on common attack vectors
- Testing incident response visibility
- Demonstrating security awareness to clients or internal teams

---

## 🛡️ Important notes
- This tool does not harm or encrypt files.
- Does not replicate, spread, or exploit real vulnerabilities.
- Always obtain proper authorization before running in a production environment.

## 📝 License

This project is licensed under the [MIT License](LICENSE).


*🎯 For questions or further customization ideas, feel free to contact me or fork and extend the project!*