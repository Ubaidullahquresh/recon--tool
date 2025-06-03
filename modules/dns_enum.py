import dns.resolver

def run_dns(target):
    records = ['A', 'AAAA', 'NS', 'MX', 'TXT']
    results = ""
    for record in records:
        try:
            answers = dns.resolver.resolve(target, record)
            results += f"\n{record} Records:\n"
            for rdata in answers:
                results += f"- {rdata}\n"
        except Exception:
            continue
    return results if results else "No DNS records found or domain doesn't resolve."

