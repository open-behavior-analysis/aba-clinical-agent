# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in this project, **do not report it via public Issue**.

### How to Report

1. **GitHub Security Advisory** (recommended): Submit a private report via the repository's Security tab
2. **Email**: Send a detailed description to [email to be configured]

### Report Contents

Please include:
- Vulnerability description
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### Response Time

- Acknowledgment: within 48 hours
- Initial assessment: within 7 days
- Fix release: based on severity, critical vulnerabilities within 14 days

## Special Concerns

### Real Case Data Exposure

If you find any suspected real case personal information (such as real names, medical diagnoses, institution names, etc.) in this repository (including historical commits), **please report immediately**. This is our highest priority security incident.

### Skill Security

If you discover that a Skill's execution logic could lead to:
- Unconfirmed file overwrites
- Data fabrication (AI hallucination bypassing safety checks)
- Sensitive information leaking to unintended locations

Please report through the channels above.

## Security Best Practices

When using this system, we recommend:

1. Always use `privacy-filter` to de-identify raw data before importing
2. Never push a Vault containing real case data to a public repository
3. Regularly check `.gitignore` to ensure sensitive files are excluded
4. Use strong passwords to protect your devices and cloud storage accounts
