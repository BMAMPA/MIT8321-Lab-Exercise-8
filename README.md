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

----------------------------------------------

# Incident Investigation Report: Lab Evidence Analysis

## Executive Summary
During a routine forensic review of the network perimeter logs on the endpoint system `wnwelih@mit8321`, a sequential attack chain was identified. The timeline reconstruction below details an adversary executing a multi-stage compromise beginning with initial reconnaissance, progressing through authentication bypass, and culminating in anti-forensic timeline manipulation.

---

## Chronological Reconstruction Matrix

| Seq | Timestamp | Source IP | Target Endpoint | HTTP Status | SIEM Observation & Forensic Impact Summary |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **01** | 09:04:15 | 172.18.0.7 | `/invalid_path_probe` | 404 | Nmap perimeter network enumeration behavior logged. |
| **02** | 09:09:32 | 172.18.0.7 | `/login` | 200 | SQLi query bypasses auth; administrative session issued. |
| **03** | 09:16:45 | 172.18.0.7 | `/accounts?id=1;whoami` | 302 | OS command injection fails due to missing cookie headers. |
| **04** | 09:18:12 | 172.18.0.7 | `/search?q=<script>...` | 200 | Reflected XSS payload string rendered within view layer. |
| **05** | 09:20:00 | 172.18.0.7 | Local Shared File Mount | N/A | Anti-forensic append attack; timeline checksum broken. |

---

## Technical Attack Chain Breakdown

1. **Reconnaissance (Seq 01):** The attacker used Nmap to sweep the web server for active directories, generating multiple `404 Not Found` errors.
2. **Initial Access & Privilege Escalation (Seq 02):** A successful SQL Injection (SQLi) attack was executed against the `/login` endpoint, resulting in an unauthorized administrative session.
3. **Lateral Movement / Execution Attempt (Seq 03):** The threat actor attempted an OS command injection (`whoami`) to verify root privileges but was blocked due to missing session cookies.
4. **Credential/Session Harvesting (Seq 04):** The actor injected a reflected Cross-Site Scripting (XSS) payload into the search function, likely aiming to hijack active user tokens.
5. **Defense Evasion / Covering Tracks (Seq 05):** The adversary interacted directly with the local shared file mount to alter files locally, systematically breaking the timeline logs' cryptographic checksum to hinder security analysts.

## Recommended Remediation Steps
* [ ] Implement Parameterized Queries / Prepared Statements on the `/login` endpoint to mitigate SQLi vulnerabilities.
* [ ] Enforce Strict Context-Aware Input Encoding on the `/search` parameter to eliminate Reflected XSS risks.
* [ ] Implement Write-Once-Read-Many (WORM) storage controls or remote SIEM forwarding for all critical system files to preserve forensic integrity against log-tampering.
---
© Copyright 2026 MIVA Open University All Rights Reserved | 2026/2027 Academic Session
