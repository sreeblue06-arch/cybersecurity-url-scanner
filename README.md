# Cybersecurity URL Risk Scanner

A beginner-friendly Python cybersecurity project that analyzes URLs for basic security indicators and maintains a persistent scan history.

## Features

- Checks whether a URL uses HTTPS.
- Detects when an IP address is used instead of a domain name.
- Flags selected suspicious words such as `login`, `verify`, `account`, `password`, `secure`, and `update`.
- Produces a simple risk score out of 9.
- Saves scan results to a JSON history file.
- Includes automated unit tests.

## Example

The project was tested with examples including:

```text
https://google.com
Risk: 0/9
Result: LOW RISK

http://192.168.1.25/login
Risk: 3/9
Result: MEDIUM RISK
Warnings: No HTTPS, IP address used, Suspicious words: login
```

## How to Run

Python 3 is required.

```bash
python scanner.py
```

Enter a URL when prompted. Type `q` to quit.

## Run the Tests

```bash
python -m unittest test_scanner.py
```

## Important Note

This is an educational URL-analysis tool. It does not perform a full vulnerability assessment, penetration test, or malicious-site verification. A low-risk result does not guarantee that a URL is safe.

## Skills Demonstrated

- Python
- URL parsing
- Basic security checks
- Risk scoring
- JSON file handling
- Automated testing
- Security-oriented problem solving
