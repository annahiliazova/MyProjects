# Cybersecurity Incident Report: DNS and ICMP Traffic Analysis

## Overview

This project focuses on analyzing network traffic and diagnosing issues related to DNS and ICMP protocols using packet capture data from a network protocol analyzer tool (tcpdump). The incident involves a "destination port unreachable" error related to port 53, which is commonly used for DNS services, and the associated ICMP "port unreachable" error. 

In this exercise, a cybersecurity analyst inspects network traffic to identify which protocol is causing the disruption. The result is documented in a comprehensive cybersecurity incident report.

## Scenario

Several clients reported that they could not access the website `www.yummyrecipesforme.com`, seeing the error "destination port unreachable." After attempting to visit the website, the issue was confirmed, and the analysis began. Using a network analyzer tool (tcpdump), the following key points were found in the log:

- **UDP packets** sent to the DNS server for IP address resolution (port 53).
- **ICMP error responses**: "UDP port 53 unreachable," indicating a failure to reach the DNS server.

The task is to analyze the packet data, identify the impacted network protocol, and write a report to explain the findings and propose possible solutions.

## Files Included

- `Cybersecurity-Incident-Report.md`: A markdown file containing the completed incident report, detailing the analysis and suggested solutions.
- `tcpdump-logs.txt`: A file containing the sample packet capture data for review and analysis.

## Steps to Reproduce

1. **Load Network Analyzer**: Open the network analyzer tool (`tcpdump`) and begin capturing network traffic.
2. **Generate Network Traffic**: Simulate browsing the website `www.yummyrecipesforme.com`, which triggers DNS queries to the DNS server.
3. **Analyze Logs**: Review the tcpdump logs to identify UDP packets sent to the DNS server, along with the associated ICMP error messages indicating that port 53 is unreachable.
4. **Document Findings**: Summarize the results in a cybersecurity incident report that includes analysis of the protocols used, error messages received, and suggested remediation steps.

## Incident Report

### Section 1: Identify the type of attack that may have caused this network interruption
The incident is caused by a failure to reach the DNS server at port 53. Analyzing the tcpdump log and the associated ICMP error messages, the issue appears to stem from a disruption in DNS communication due to unreachable port 53. The analysis suggests that this may have been caused by a misconfiguration or network-level issue rather than a typical cyber attack.

### Section 2: Explain how the attack is causing the website to malfunction
The failure to resolve the domain name into an IP address causes the website to be inaccessible. The underlying issue is the "UDP port 53 unreachable" ICMP error, which signifies that the DNS server could not be reached due to the port being unavailable.

## Tools and Technologies Used

- **Network Protocol Analyzer**: tcpdump
- **Protocols Analyzed**: DNS (UDP), ICMP
- **Data Format**: Packet Capture (PCAP)
  
## Conclusion

This report outlines the process of analyzing a network issue involving DNS and ICMP traffic. The problem was identified as an unreachable DNS port, and possible solutions were discussed, including verifying DNS server configurations and troubleshooting network paths to ensure proper communication with DNS servers.

## Future Work

Further investigation may involve verifying firewall settings, examining server logs, and checking for external factors that may have caused the disruption of DNS services.
