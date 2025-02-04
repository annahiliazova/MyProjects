# DNS and ICMP Traffic Analysis

## Overview
This project involves analyzing network traffic to investigate a cybersecurity incident affecting DNS and ICMP protocols. The investigation focuses on identifying issues that prevented users from accessing the website **yummyrecipesforme.com**.

## Incident Summary
A network traffic analysis using `tcpdump` revealed an issue with **DNS and ICMP protocols**. The **DNS server on port 53** was found to be **unreachable**, which prevented domain name resolution. The log analysis showed repeated **ICMP error messages** stating **"udp port 53 unreachable"**, indicating a failure in the DNS query process.

### Key Findings:
- The website **yummyrecipesforme.com** was inaccessible to users.
- **ICMP error messages** indicated that UDP port **53 was unreachable**.
- The **DNS service failure** suggests a possible **Denial of Service (DoS) attack** affecting port 53.

## Methodology
1. Captured network traffic using `tcpdump`.
2. Analyzed logs to identify DNS and ICMP errors.
3. Determined the root cause of the service disruption.

## Tools and Technologies Used
- **tcpdump**: For capturing and analyzing network traffic.
- **Wireshark**: For visualizing packet data (optional).
- **ICMP/DNS Protocols**: Key protocols involved in the incident.

## Recommendations
1. **Monitor Network Traffic** – Use intrusion detection systems (IDS) to track unusual traffic patterns.
2. **Check DNS Server Logs** – Identify if the server was overloaded or experiencing malicious traffic.
3. **Implement Rate Limiting** – Prevent excessive requests to DNS services from overwhelming the system.
4. **Enable Firewall Rules** – Block malicious IP addresses and restrict unauthorized access.

## Files Included
`Cybersecurity incident report.pdf`: Detailed report of the analysis.
`How to read a Wireshark TCP_HTTP log.pdf`: Guide for interpreting network logs.
