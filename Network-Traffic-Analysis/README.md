# Network Traffic Analysis: Cybersecurity Incident Report  

## Overview  

This project involves analyzing network traffic to investigate a cybersecurity incident affecting DNS and ICMP protocols. The investigation focuses on identifying issues that prevented users from accessing the website **yummyrecipesforme.com**.  

## Incident Summary  

A network traffic analysis using \`tcpdump\` revealed an issue with **DNS and ICMP protocols**. The **DNS server on port 53** was found to be **unreachable**, which prevented domain name resolution. The log analysis showed repeated **ICMP error messages** stating **"udp port 53 unreachable"**, indicating a failure in the DNS query process.  

### Key Findings:  
- The website **yummyrecipesforme.com** was inaccessible to users.  
- **ICMP error messages** indicated that UDP port **53 was unreachable**.  
- The **DNS service failure** suggests a possible **Denial of Service (DoS) attack** affecting port 53.  

## TCPDump Log Analysis  

Example log entries from \`tcpdump\` confirm the issue:  

\`\`\`
13:24:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com. (24)  
13:24:36.098564 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2 udp port 53 unreachable length 254  
13:26:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com. (24)  
13:27:15.934126 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2 udp port 53 unreachable length 320  
\`\`\`  

These logs show repeated **failed DNS queries** followed by **ICMP error responses**, confirming that **port 53 was unresponsive**.  

## Root Cause and Next Steps  

The investigation suggests that a **Denial of Service (DoS) attack** may have targeted the **DNS server**, rendering port 53 unavailable.  

### Recommended Actions:  
1. **Monitor Network Traffic** – Use intrusion detection systems (IDS) to track unusual traffic patterns.  
2. **Check DNS Server Logs** – Identify if the server was overloaded or experiencing malicious traffic.  
3. **Implement Rate Limiting** – Prevent excessive requests to DNS services from overwhelming the system.  
4. **Enable Firewall Rules** – Block malicious IP addresses and restrict unauthorized access.  
5. **Contact Hosting Provider** – If the DNS server is externally hosted, notify the provider about the potential attack.  
