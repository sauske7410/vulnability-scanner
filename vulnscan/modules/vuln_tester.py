# modules/vuln_tester.py
def test_vulnerabilities(target):
    import requests
    print("[*] Testing for common vulnerabilities...")
    results = {}
    try:
        payload = "<script>alert(1)</script>"
        xss_test = requests.get(f"http://{target}/?q={payload}")
        results['XSS'] = payload in xss_test.text
    except:
        results['XSS'] = False
    try:
        sqli_test = requests.get(f"http://{target}/?id=1' or '1'='1")
        results['SQLi'] = "sql" in sqli_test.text.lower()
    except:
        results['SQLi'] = False
    print(f"[+] Vulnerability results: {results}")
    return results
