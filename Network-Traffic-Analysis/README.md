# Network Traffic Analysis: SYN Flood Attack

## Overview
This project focuses on analyzing network traffic to diagnose a SYN flood attack on a web server. The attack caused the server to become unresponsive, resulting in timeout errors for users attempting to access the website.

## Incident Summary
The website `www.example.com` experienced connectivity issues due to a SYN flood attack. The server was overwhelmed with half-open TCP connections, preventing it from responding to legitimate requests.

### Key Findings:
- Excessive SYN requests from multiple IP addresses.
- Server resources exhausted, leading to timeout errors.
- No legitimate TCP handshakes completed during the attack.

## Methodology
1. Captured network traffic using Wireshark.
2. Analyzed TCP packets to identify SYN flood patterns.
3. Documented the impact on server performance.

## Tools and Technologies Used
- **Wireshark**: For packet capture and analysis.
- **TCP Protocol**: Key protocol affected by the attack.

## Recommendations
1. **Implement Rate Limiting** – Restrict the number of SYN requests per IP address.
2. **Enable SYN Cookies** – Protect against SYN flood attacks by reducing resource consumption.
3. **Monitor Network Traffic** – Use IDS/IPS to detect and block malicious traffic.

## Files Included
- `Cybersecurity Incident Report.pdf`: Detailed report of the analysis.
- `tcpdump-logs.png`: Screenshot of network traffic logs.
