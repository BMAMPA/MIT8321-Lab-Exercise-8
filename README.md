# MIT 8321 - Forensics and Ethical Hacking (Virtual Lab)
## Lab Exercise 8: Anti-Forensics Analysis and Log Integrity Verification

### Project Overview
This repository contains the infrastructure configurations, multi-vector attack simulation scripts, and SIEM pipeline parsing definitions engineered during the security audit of the **SecureBank Cyber Fortress** platform. This project evaluates how web vulnerabilities transition into measurable log footprints and isolates targeted anti-forensic record-poisoning attempts.

### Environment Specifications
* **Investigator Account Profile:** `wnwelih`
* **Target Host Name (Hostname):** `mit8321`
* **Operating System Deck:** Ubuntu 26.04 64-bit Virtual Machine (VMware Workstation)
* **Chronological Alignment:** West Africa Time (WAT Context)
* **Network Infrastructure Scope:** Host-Isolated Docker Bridge Subnet (`172.18.0.0/16`)

### Repository Manifest & Structure
1. `app.py` - Core Python Flask application containing known vulnerabilities (CWE-89, CWE-78, CWE-79).
2. `docker-compose.yml` - Infrastructure deployment blueprint and multi-container runtime settings.
3. `logstash.conf` - SIEM pipeline processing configurations and automated Grok filter definitions.
4. `attack.sh` - Automated red-team simulation utility mimicking multi-vector web exploitation.

---
© Copyright 2026 MIVA Open University All Rights Reserved | 2026/2027 Academic Session
