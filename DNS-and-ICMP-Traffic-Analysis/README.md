# Cybersecurity Incident Report: DNS and ICMP Traffic Analysis

### Overview

This project focuses on analyzing network traffic to diagnose issues caused by a **SYN flood attack**, which led to a **Denial of Service (DoS)** for a website. Using packet capture data from a network protocol analyzer (Wireshark), the investigation reveals how the SYN flood overwhelmed the server's resources, causing it to be unresponsive to legitimate requests.

The incident involves a website that became unreachable due to the server being flooded with an excessive number of half-open TCP connections. The report documents the findings, explains the attack mechanism, and provides recommendations for mitigation.

### Scenario

A website experienced significant downtime, with users encountering a connection timeout error. The issue was traced back to a SYN flood attack, where the attacker flooded the server with a large volume of SYN packets, overwhelming its ability to process legitimate requests.

Key points discovered from the packet capture data include:
- **TCP SYN packets** sent from a single source IP address to the server.
- **No ACK responses** received from the clients, indicating incomplete connections (half-open connections).
- **Resource exhaustion** at the server, which led to a failure in handling legitimate user connections.

The task is to analyze the packet data, identify the attack type, and explain how it disrupted the server's normal operation in a detailed cybersecurity incident report.

### Files Included

- `Cybersecurity-Incident-Report.md`: A markdown file containing the completed incident report, including analysis of the attack and the impact on the server.
- `How-to-read-a-Wireshark-TCP_HTTP-log.pdf` : A PDF document that provides detailed instructions on how to read and interpret Wireshark logs, focusing on TCP and HTTP traffic analysis.

### Steps to Reproduce

1. **Open Packet Capture in Wireshark**: Load the `wireshark-log.pcap` file into Wireshark for analysis.
2. **Apply Filters**: Use the Wireshark filter `tcp.flags.syn == 1 && tcp.flags.ack == 0` to locate SYN packets that are part of the flood.
3. **Analyze the Traffic**: Review the SYN packets to determine the source IP address, the volume of packets, and any signs of resource exhaustion on the server side.
4. **Document Findings**: Write a cybersecurity incident report detailing the type of attack, its effect on the server, and potential mitigation strategies.

### Incident Report

#### Section 1: Identify the type of attack that may have caused this network interruption

The network disruption was caused by a **SYN flood attack**. The attacker sent a large number of SYN packets to the server without completing the TCP handshake. This resulted in the server's resources being exhausted as it tried to establish connections, preventing it from handling legitimate requests.

#### Section 2: Explain how the attack is causing the website to malfunction

The server's inability to complete the three-way TCP handshake due to an overwhelming number of incoming SYN packets caused it to become unresponsive. As a result, legitimate users were unable to establish a connection, leading to the timeout errors they encountered. The attack effectively consumed server resources, blocking access to the website.

### Tools and Technologies Used

- **Network Protocol Analyzer**: Wireshark
- **Protocols Analyzed**: TCP (SYN flood)
- **Data Format**: Packet Capture (PCAP)

### Conclusion

This report provides an in-depth analysis of a **SYN flood attack** and its impact on the server's ability to process connections. The investigation showed that the server became overwhelmed by a large number of incomplete TCP handshakes, preventing normal operations and causing a Denial of Service. Possible mitigation strategies, such as SYN cookies or rate-limiting incoming connections, are discussed in the report.
