Cybersecurity URL Risk Scanner

A beginner-friendly Python security utility that analyzes URLs for a few
common warning signs and assigns a simple risk level.


Built as a practical cybersecurity portfolio project to demonstrate
Python programming, basic security analysis, input handling, JSON data
persistence, and automated testing.


What it checks

The scanner currently looks for:



HTTPS usage --- flags URLs that do not use HTTPS.

IP-address hosts --- identifies URLs that use an IP address instead of a domain name.

Suspicious keywords --- checks the URL for terms such as login, verify, account, password, secure, and update.

Risk scoring --- converts detected warnings into a simple score out of 9.

Scan history --- saves scan results with timestamps in JSON format.

Automated tests --- includes tests for clean URLs, flagged URLs, and history persistence.


Example

For a URL such as:


http://192.168.1.25/login

the scanner can identify:



No HTTPS

IP address used as the host

Suspicious word: login


It then reports the corresponding risk score and risk level.


Project structure

cybersecurity-url-scanner/
├── scanner.py          # Main URL analysis and scan-history logic
├── test_scanner.py     # Automated tests
├── scan_history.txt    # Sample scan report
├── requirements.txt    # Dependency information
└── README.md           # Project documentation

Getting started

1. Clone the repository

git clone https://github.com/sreeblue06-arch/cybersecurity-url-scanner.git
cd cybersecurity-url-scanner

2. Run the scanner

python scanner.py

Enter a URL when prompted and review the warnings, risk score, and
result.


3. Run the tests

python -m unittest test_scanner.py

Technologies used


Python 3

Python Standard Library

urllib.parse

ipaddress

json

datetime

unittest


No external Python packages are required.


Skills demonstrated

This project demonstrates practical experience with:



Python programming

URL parsing and validation

Basic cybersecurity risk analysis

Input processing

File and JSON handling

Persistent scan history

Unit testing

Writing technical documentation


Limitations

This is an educational security-analysis project, not a full
vulnerability scanner.


It does not perform:



Penetration testing

Exploitation

Malware analysis

Full website vulnerability assessment

Reputation or threat-intelligence verification

A definitive determination of whether a website is malicious


A URL receiving a low-risk result should therefore not be treated as
proof that the destination is safe.


Purpose

The project was created as part of my cybersecurity learning journey to
practice turning security concepts into a working Python tool.


Future improvements could include additional URL heuristics, stronger
validation, structured reporting, and integration with trusted
threat-intelligence sources.



Author: Sreelakshmi Pallikkara
GitHub: https://github.com/sreeblue06-arch

