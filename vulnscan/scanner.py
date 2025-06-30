# vulnscan/scanner.py
from modules import port_scanner, ssl_checker, vuln_tester, report_generator
import sys
import os

def main(target):
    print(f"[+] Scanning target: {target}\n")

    open_ports = port_scanner.scan_ports(target)
    ssl_info = ssl_checker.check_ssl(target)
    vuln_results = vuln_tester.test_vulnerabilities(target)

    report_generator.generate_report(target, open_ports, ssl_info, vuln_results)
    print("\n[+] Scan complete. Report saved in 'output/' folder.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <target_domain_or_ip>")
        sys.exit(1)
    target = sys.argv[1]
    if not os.path.exists("output"):
        os.mkdir("output")
    main(target)


