# modules/report_generator.py
def generate_report(target, ports, ssl_data, vulns):
    from datetime import datetime
    import html

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"output/report_{target}_{now}.html"

    safe_ssl = html.escape(str(ssl_data))
    ports_list = ''.join([f'<li>{p}</li>' for p in ports])
    vulns_list = ''.join([f'<li>{html.escape(k)}: {v}</li>' for k, v in vulns.items()])

    html_lines = [
        "<html>",
        f"<head><title>VulnScan Report for {target}</title></head>",
        "<body>",
        "<h1>VulnScan Report</h1>",
        f"<p><strong>Target:</strong> {target}</p>",
        f"<p><strong>Date:</strong> {now}</p>",
        "<h2>Open Ports</h2>",
        f"<ul>{ports_list}</ul>",
        "<h2>SSL Certificate Info</h2>",
        f"<pre>{safe_ssl}</pre>",
        "<h2>Vulnerability Results</h2>",
        f"<ul>{vulns_list}</ul>",
        "</body>",
        "</html>"
    ]

    with open(report_name, "w") as f:
        f.write('\n'.join(html_lines))

    print(f"[+] Report saved to {report_name}")
