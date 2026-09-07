# 🔐 Log Analyzer — Brute-Force Detection Tool

A Python-based security tool that parses authentication logs, detects
brute-force attack patterns, and outputs a prioritized triage queue —
replicating core SIEM correlation logic.

## 🎯 What it does
- **Ingest** — reads authentication log files
- **Parse** — extracts source IPs from failed-login entries
- **Count** — aggregates failed attempts per source IP
- **Detect** — flags IPs exceeding a configurable alert threshold
- **Prioritize** — sorts offenders by failure count (worst first)

## 🚀 How to run
\`\`\`bash
python analyzer.py
\`\`\`

## 📊 Sample output
\`\`\`
{'1.2.3.4': 3, '9.9.9.9': 1, '2.6.4.5': 1}
Alert : Brute force suspected 1.2.3.4
Ok 9.9.9.9 -only 1 failure(s), ignore

=== TRIAGE QUEUE ===
1.2.3.4 → 3 failed logins
9.9.9.9 → 1 failed logins
2.6.4.5 → 1 failed logins
\`\`\`

## 🛠 Skills demonstrated
Log parsing · Python automation · Threshold-based detection ·
Alert triage · SIEM correlation concepts

## 🔭 Roadmap
- [ ] Timestamp correlation (failures within N minutes)
- [ ] Export alerts to CSV for ticketing
- [ ] GeoIP lookup on flagged IPs

