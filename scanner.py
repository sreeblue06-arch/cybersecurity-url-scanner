import ipaddress
import json
from datetime import datetime
from urllib.parse import urlparse

HISTORY_FILE = "scan_history.json"
SUSPICIOUS_WORDS = {"login", "verify", "account", "password", "secure", "update"}


def analyze_url(url):
    """Analyze a URL for a few basic security indicators."""
    warnings = []
    parsed = urlparse(url)

    if parsed.scheme != "https":
        warnings.append("No HTTPS")

    hostname = parsed.hostname or ""
    try:
        ipaddress.ip_address(hostname)
        warnings.append("IP address used")
    except ValueError:
        pass

    lower_url = url.lower()
    found_words = sorted(word for word in SUSPICIOUS_WORDS if word in lower_url)
    if found_words:
        warnings.append("Suspicious words: " + ", ".join(found_words))

    risk = len(warnings)
    if risk == 0:
        result = "LOW RISK"
    elif risk <= 3:
        result = "MEDIUM RISK"
    else:
        result = "HIGH RISK"

    return {
        "url": url,
        "domain": hostname,
        "risk": f"{risk}/9",
        "result": result,
        "warnings": warnings,
    }


def save_scan(record, filename=HISTORY_FILE):
    """Append a scan record to persistent JSON history."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            history = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []

    record = {
        "time": datetime.now().isoformat(timespec="seconds"),
        **record,
    }
    history.append(record)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=2)

    return record


def main():
    print("Cybersecurity URL Risk Scanner")
    print("-" * 32)

    while True:
        url = input("Enter a URL (or 'q' to quit): ").strip()
        if url.lower() == "q":
            break
        if not url:
            print("Please enter a URL.")
            continue

        report = analyze_url(url)
        saved = save_scan(report)

        print(f"\nRisk: {saved['risk']}")
        print(f"Result: {saved['result']}")
        print(f"Domain: {saved['domain']}")
        print("Warnings:", ", ".join(saved["warnings"]) or "None")
        print()


if __name__ == "__main__":
    main()
