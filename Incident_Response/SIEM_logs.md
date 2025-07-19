SIEM & Log Parsing
 Tasks:
- Parsed `/var/log/auth.log` in Parrot OS
- Identified failed and successful SSH logins
- Analyzed suspicious IPs
- Wrote detection rules in Wazuh

 Response Plan:
1. Detect brute force with alert rule
2. Contain by blocking IPs
3. Investigate affected user accounts
4. Recover by enforcing stronger passwords
