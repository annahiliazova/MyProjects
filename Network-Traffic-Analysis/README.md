# Report: Network Traffic Analysis

## Overview
This project contains materials completed as part of a course on network traffic analysis and incident investigation. Specifically, it includes an analysis of an attack on a web server conducted via a **SYN flood (DoS attack)** and a guide on reading **Wireshark logs**.

The project includes:
- **Cybersecurity Incident Report: Network Traffic Analysis** – a completed example of an incident report.
- **How to Read Wireshark TCP/HTTP Log** – a guide explaining how to interpret Wireshark network traffic logs.

## Task Description
The task involved:
1. Analyzing a scenario where a company's client faced difficulties accessing a website due to an attack.
2. Identifying the type of attack (SYN flood DoS attack) and its impact on the web server.
3. Using data obtained via Wireshark to compile an incident report.
4. Answering key questions:
   - What types of network attacks do you know, and how do they differ?
   - What is the difference between a DoS and a DDoS attack?
   - Why is the website unresponsive and showing a timeout error?

A detailed task description is included in the provided materials.

## Project Contents
- **Cybersecurity Incident Report: Network Traffic Analysis.pdf**  
  *A completed report describing the incident, its analysis, and the root cause of the problem. The report includes:*
  - Problem summary.
  - Analysis of network log data.
  - Conclusions and recommendations for preventing similar incidents.

- **How to Read Wireshark TCP HTTP Log.pdf**  
  *A guide explaining how to read and interpret Wireshark logs. It covers:*
  - Log structure (entry numbers, timestamps, source and destination IP addresses, protocol details).
  - Examples of normal traffic vs. attack traffic (SYN flood).
  - Color-coded packet highlighting to distinguish normal traffic from attacks.

## How to Use the Materials
1. **To understand the incident:**  
   Open `Cybersecurity Incident Report: Network Traffic Analysis.pdf` to review a fully completed incident report. It provides a detailed analysis of the attack, log data interpretation, and its impact on the web server.

2. **To learn network traffic analysis methods:**  
   The `How to Read Wireshark TCP HTTP Log.pdf` file will help you understand how to read logs and identify signs of network attacks. This material is useful for understanding TCP traffic behavior and the specifics of SYN flood attacks.

3. **For further use:**  
   These materials can be used for educational purposes, to create your own reports, or as a reference for real-world incident analysis.

## Context & Scenario
The scenario analyzed in this project:
- A company receives reports about issues with its web server.
- Using a packet sniffer (Wireshark), an unusual amount of TCP SYN requests from an unknown IP is detected.
- The suspicion falls on a DoS attack (SYN flood), preventing the server from responding to legitimate traffic.
- The report describes the steps taken to identify the problem, analyze it, and provide recommendations, including blocking the attacker's IP and improving network security.
