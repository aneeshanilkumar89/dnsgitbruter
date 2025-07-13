import argparse
import socket
import requests
import sys

def load_wordlist(filepath=None, url=None):
    try:
        if filepath:
            with open(filepath, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        elif url:
            response = requests.get(url)
            response.raise_for_status()
            return [line.strip() for line in response.text.splitlines() if line.strip()]
        else:
            print("[!] Either a wordlist file (-w) or URL (--url) must be provided.")
            sys.exit(1)
    except Exception as e:
        print(f"[!] Failed to load wordlist: {e}")
        sys.exit(1)

def resolve_subdomain(domain, subdomain):
    fqdn = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(fqdn)
        return fqdn, ip
    except socket.gaierror:
        return None, None

def brute_force_subdomains(domain, wordlist):
    print(f"[*] Starting brute-force on domain: {domain}\n")
    found = []

    for sub in wordlist:
        fqdn, ip = resolve_subdomain(domain, sub)
        if fqdn and ip:
            print(f"[+] Found: {fqdn} -> {ip}")
            found.append((fqdn, ip))

    print(f"\n[✓] Done. {len(found)} subdomains found.")
    return found

def main():
    parser = argparse.ArgumentParser(description="Subdomain brute-forcer with resolver")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g. example.com)")
    parser.add_argument("-w", "--wordlist", help="Path to subdomain wordlist file")
    parser.add_argument("--url", help="URL to subdomain wordlist")

    args = parser.parse_args()

    # Require at least one: -w or --url
    if not args.wordlist and not args.url:
        parser.error("You must provide either a wordlist file (-w) or a URL (--url)")

    wordlist = load_wordlist(filepath=args.wordlist, url=args.url)
    brute_force_subdomains(args.domain, wordlist)

if __name__ == "__main__":
    main()
