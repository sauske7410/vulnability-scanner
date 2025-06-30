VulnScan - Automated Vulnerability Scanner

VulnScan is a lightweight, Python-based tool for performing basic security assessments on a target domain or IP address. It performs port scanning, SSL certificate inspection, and tests for common web vulnerabilities like XSS and SQL Injection.

---

 Features

-  Scans for open ports (common ports)
-  Checks SSL/TLS certificate (validity, expiry)
-  Tests for:
  - Cross-site Scripting (XSS)
  - SQL Injection (SQLi)
-  Generates HTML report with results

---

##  Tech Stack

- **Python 3.6+**
- Modules used:
  - `socket`
  - `ssl`
  - `requests`
  - `html`
  - `datetime`

---

##  Project Structure

vulnscan/
├── scanner.py
├── output/
│ └── report_<target>_<timestamp>.html
├── modules/
│ ├── init.py
│ ├── port_scanner.py
│ ├── ssl_checker.py
│ ├── vuln_tester.py
│ └── report_generator.py
└── README.md

---

  How to Run

 1. Clone or download the repo
```bash
git clone https://github.com/your-username/vulnscan.git
cd vulnscan

 2. Install dependencies
```bash
pip install requests
```

 3. Run the scanner
```bash
python scanner.py testphp.vulnweb.com
```

>  Replace `testphp.vulnweb.com` with any target domain or IP (use responsibly).

---

##  Sample Output

- HTML report saved in `/output/`
- Report includes:
  - List of open ports
  - SSL certificate info
  - Vulnerability test results

---

##Disclaimer

> **This tool is intended for educational and ethical purposes only. Do not scan unauthorized systems.**

---

## License

MIT License © Pulkit Rathore
"""