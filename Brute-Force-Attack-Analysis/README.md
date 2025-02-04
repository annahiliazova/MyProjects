# Security Incident Report: Brute Force Attack on yummyrecipesforme.com

## Overview
This repository contains the analysis and documentation of a cybersecurity incident involving a brute force attack on the website **yummyrecipesforme.com**. The attacker, a former employee, gained unauthorized access to the admin panel, embedded malicious JavaScript, and redirected users to a malware-hosting site. This report details the incident, the network protocols involved, and recommendations to prevent future attacks.

---

## Incident Summary
Several customers reported that the website prompted them to download a file, which led to malware infection and browser redirection to **greatrecipesforme.com**. Analysis revealed that a brute force attack was used to compromise the admin panel, allowing the attacker to modify the website's source code.

### Key Findings:
- **Brute Force Attack**: The attacker exploited weak default passwords to gain admin access.
- **Malicious JavaScript**: Embedded code prompted users to download a malicious file.
- **DNS and HTTP Protocols**: Used to redirect users to a fake website.
- **Impact**: Users' devices were infected with malware, and the website's reputation was compromised.

---

## Files Included
- **Security Incident Report.pdf**: Detailed documentation of the incident, including analysis and recommendations.
- **tcpdump Traffic Log.pdf**: Network traffic logs captured during the investigation.
- **How to Read the tcpdump Log.pdf**: A guide for interpreting tcpdump logs and understanding the attack.

---

## Incident Analysis

### 1. Network Protocol Involved
The incident primarily involved the **HTTP/1.1** protocol. Key observations:
- **DNS Requests**: Resolved `yummyrecipesforme.com` and `greatrecipesforme.com`.
- **HTTP Traffic**: Significant data exchange on port 80, indicating the download and redirection process.

### 2. Incident Details
- **Initial Compromise**: The attacker used a brute force attack to guess the admin password.
- **Malicious Activity**: Embedded JavaScript prompted users to download a file, which redirected them to `greatrecipesforme.com`.
- **User Impact**: Customers reported malware infections and browser redirections.
- **Log Analysis**: `tcpdump` logs confirmed DNS and HTTP traffic patterns consistent with the attack.

### 3. Recommendations
To prevent future brute force attacks:
- **Implement a Strong Password Policy**:
  - Minimum length: 12 characters.
  - Use of uppercase, lowercase, numbers, and symbols.
  - Regular password changes (e.g., every 90 days).
- **Enable Multi-Factor Authentication (MFA)**: Adds an additional layer of security.
- **Monitor Login Attempts**: Implement rate-limiting to block repeated failed login attempts.

---

## How to Use This Repository
1. **Review the Report**: Open `Security Incident Report.pdf` for a detailed analysis of the incident.
2. **Analyze the Logs**: Use `tcpdump Traffic Log.pdf` to explore the network traffic captured during the attack.
3. **Learn to Read Logs**: Refer to `How to Read the tcpdump Log.pdf` for guidance on interpreting tcpdump output.

---
# Security Incident Report: Brute Force Attack on yummyrecipesforme.com

## Overview
This repository contains the analysis and documentation of a cybersecurity incident involving a brute force attack on the website **yummyrecipesforme.com**. The attacker, a former employee, gained unauthorized access to the admin panel, embedded malicious JavaScript, and redirected users to a malware-hosting site. This report details the incident, the network protocols involved, and recommendations to prevent future attacks.

---

## Incident Summary
Several customers reported that the website prompted them to download a file, which led to malware infection and browser redirection to **greatrecipesforme.com**. Analysis revealed that a brute force attack was used to compromise the admin panel, allowing the attacker to modify the website's source code.

### Key Findings:
- **Brute Force Attack**: The attacker exploited weak default passwords to gain admin access.
- **Malicious JavaScript**: Embedded code prompted users to download a malicious file.
- **DNS and HTTP Protocols**: Used to redirect users to a fake website.
- **Impact**: Users' devices were infected with malware, and the website's reputation was compromised.

---

## Files Included
- **Security Incident Report.pdf**: Detailed documentation of the incident, including analysis and recommendations.
- **tcpdump Traffic Log.pdf**: Network traffic logs captured during the investigation.
- **How to Read the tcpdump Log.pdf**: A guide for interpreting tcpdump logs and understanding the attack.

---

## Incident Analysis

### 1. Network Protocol Involved
The incident primarily involved the **HTTP/1.1** protocol. Key observations:
- **DNS Requests**: Resolved `yummyrecipesforme.com` and `greatrecipesforme.com`.
- **HTTP Traffic**: Significant data exchange on port 80, indicating the download and redirection process.

### 2. Incident Details
- **Initial Compromise**: The attacker used a brute force attack to guess the admin password.
- **Malicious Activity**: Embedded JavaScript prompted users to download a file, which redirected them to `greatrecipesforme.com`.
- **User Impact**: Customers reported malware infections and browser redirections.
- **Log Analysis**: `tcpdump` logs confirmed DNS and HTTP traffic patterns consistent with the attack.

### 3. Recommendations
To prevent future brute force attacks:
- **Implement a Strong Password Policy**:
  - Minimum length: 12 characters.
  - Use of uppercase, lowercase, numbers, and symbols.
  - Regular password changes (e.g., every 90 days).
- **Enable Multi-Factor Authentication (MFA)**: Adds an additional layer of security.
- **Monitor Login Attempts**: Implement rate-limiting to block repeated failed login attempts.

---

## How to Use This Repository
1. **Review the Report**: Open `Security Incident Report.pdf` for a detailed analysis of the incident.
2. **Analyze the Logs**: Use `tcpdump Traffic Log.pdf` to explore the network traffic captured during the attack.
3. **Learn to Read Logs**: Refer to `How to Read the tcpdump Log.pdf` for guidance on interpreting tcpdump output.

---

## Lessons Learned
- **Importance of Strong Passwords**: Default or weak passwords are easily exploited.
- **Proactive Monitoring**: Regular monitoring of network traffic can help detect anomalies early.
- **User Education**: Educating users about phishing and malware risks can reduce the impact of such attacks.

---

## Resources
- [NIST Password Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
- [OWASP Brute Force Attack Prevention](https://owasp.org/www-community/attacks/Brute_force_attack)

