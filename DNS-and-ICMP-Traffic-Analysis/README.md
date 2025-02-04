# Cybersecurity Incident Report: DNS and ICMP Traffic Analysis

## Overview

This project focuses on analyzing network traffic to diagnose an attack on a web server. Specifically, it investigates a potential SYN flood attack, which is causing the server to become unresponsive and resulting in timeout errors when users attempt to access the website. The analysis uses packet capture data (PCAP) obtained via Wireshark and includes a detailed cybersecurity incident report explaining the findings and impact.

The goal is to analyze network traffic to identify the attack type and understand how it disrupts the web server's functionality.

## Scenario

The website `www.example.com` has been experiencing connectivity issues. Several clients have reported a "connection timeout" error, which indicates that the server is not responding to requests. After further investigation using network logs and Wireshark, it was determined that the root cause of the issue was a Denial of Service (DoS) attack, specifically a SYN flood.

### Key Findings:
- The logs show an excessive number of SYN requests sent to the server.
- The server is unable to respond to legitimate requests due to resource exhaustion caused by the overwhelming SYN requests.
- The connection timeout error occurs as the server fails to complete the TCP handshake with legitimate clients.

The task is to analyze the packet capture data, identify the attack, and document the findings and recommendations in a cybersecurity incident report.

## Files Included

- `Cybersecurity-Incident-Report.md`: A markdown file containing the completed incident report, detailing the analysis and impact of the attack.
- `How-to-read-a-Wireshark-TCP_HTTP-log.pdf`: A PDF document explaining how to read and analyze TCP and HTTP traffic in Wireshark, with a focus on diagnosing issues like SYN floods and timeouts.

## Steps to Reproduce

1. **Load Network Analyzer**: Open the packet capture file in Wireshark.
2. **Inspect the TCP Traffic**: Look for SYN packets that do not complete the handshake and examine the source IPs that are sending them.
3. **Analyze the Logs**: Review the capture to identify patterns of SYN flood behavior, including failed TCP handshakes and timeouts.
4. **Write the Report**: Document your findings in the cybersecurity incident report, detailing the analysis of the logs and the impact on the server.

## Incident Report

### Section 1: Identify the Type of Attack

The incident is caused by a SYN flood attack. A SYN flood is a type of DoS (Denial of Service) attack where an attacker sends a large number of SYN packets to a target server with the intention of consuming server resources. Each SYN request is part of the TCP handshake process, but in a SYN flood, the attacker does not complete the handshake, leaving the server with half-open connections.

In this case, the server becomes overwhelmed with these half-open connections and can no longer respond to legitimate requests, resulting in a timeout error for users trying to connect to the website.

### Section 2: Explain How the Attack Is Causing the Website to Malfunction

TCP connections require a three-step handshake to establish a session between the client and server:
1. The client sends a SYN request to the server.
2. The server replies with a SYN-ACK response.
3. The client acknowledges the server's SYN-ACK with an ACK message.

In a SYN flood, the attacker sends numerous SYN requests without responding to the server's SYN-ACK. As a result, the server's resources are tied up with these incomplete connections. Once the server runs out of resources, it becomes unresponsive, and legitimate users attempting to access the website experience timeout errors.

The network logs show that the server's capacity is exceeded, preventing the completion of normal connections, and leading to service disruptions for users.

## Tools and Technologies Used

- **Wireshark**: A network protocol analyzer used to capture and inspect network traffic.
- **Protocols Analyzed**: TCP, HTTP
- **Data Format**: Packet Capture (PCAP)
  
## Conclusion

This project involved analyzing network traffic to identify the cause of a website's connectivity issue. The issue was traced to a SYN flood attack that overwhelmed the server and caused it to stop responding to legitimate requests. Based on the findings, it is clear that the attack resulted in a denial of service, which prevented normal web operations.

### Recommended Next Steps:
- **Mitigate the Attack**: Implement rate-limiting on the server to limit the number of incoming SYN requests.
- **Deploy SYN Cookies**: Configure SYN cookies to protect against SYN flood attacks by ensuring that incomplete connections do not consume excessive resources.
- **Enhance Network Security**: Monitor network traffic for unusual patterns and investigate the possibility of blocking malicious IP addresses that are involved in the attack.
