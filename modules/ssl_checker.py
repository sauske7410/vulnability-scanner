# modules/ssl_checker.py
def check_ssl(target):
    import ssl, socket
    print("[*] Checking SSL certificate...")
    try:
        context = ssl.create_default_context()
        with socket.create_connection((target, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=target) as ssock:
                cert = ssock.getpeercert()
                print("[+] SSL cert found")
                return cert
    except Exception as e:
        print("[-] SSL check failed:", str(e))
        return {}
