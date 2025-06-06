import argparse
from modules import whois_lookup, dns_enum, subdomain_enum, port_scan, banner_grab, tech_detect
from datetime import datetime
import os

def main():
    parser = argparse.ArgumentParser(description="ReconMate - Custom Recon Tool")
    parser.add_argument("--target", required=True, help="Target domain or IP")
    parser.add_argument("--whois", action="store_true", help="Run WHOIS Lookup")
    parser.add_argument("--dns", action="store_true", help="Run DNS Enumeration")
    parser.add_argument("--subdomains", action="store_true", help="Run Subdomain Enumeration")
    parser.add_argument("--portscan", action="store_true", help="Run Port Scan")
    parser.add_argument("--banner", action="store_true", help="Run Banner Grabbing")
    parser.add_argument("--tech", action="store_true", help="Run Technology Detection")
    parser.add_argument("--report", choices=["txt", "html"], default="txt", help="Report format (txt or html)")
    parser.add_argument("--port", type=int, help="Port number for banner grabbing")  # <-- Added this line

    args = parser.parse_args()
    target = args.target
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results = f"Recon Report for {target}\nTimestamp: {timestamp}\n\n"

    if args.whois:
        results += "\n[WHOIS Info]\n" + whois_lookup.run_whois(target)
    if args.dns:
        results += "\n[DNS Records]\n" + dns_enum.run_dns(target)
    if args.subdomains:
        results += "\n[Subdomains]\n" + subdomain_enum.run_subdomain_enum(target)
    if args.portscan:
        results += "\n[Port Scan]\n" + port_scan.run_port_scan(target)
    if args.banner:
        port = args.port if args.port else 80  # <-- Use --port if given, else default to 80
        results += f"\n[Banner Grabbing - Port {port}]\n" + banner_grab.run_banner_grab(target, port)
    if args.tech:
        results += "\n[Tech Detection]\n" + tech_detect.run_tech_detect(target)

    os.makedirs("reports", exist_ok=True)
    report_path = f"reports/{target}_report.{args.report}"
    with open(report_path, "w") as f:
        f.write(results)

    print(f"\n✅ Report saved to: {report_path}")

if __name__ == "__main__":
    main()
