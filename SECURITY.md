# Security Policy

## Supported Versions

Security updates are provided for the latest active version of Agentic Assistants.

| Version | Supported |
|---|---|
| Latest release | Yes |
| Older releases | No |
| Development branches | No guarantee |

Users should upgrade to the most recent published version before reporting a security issue.

## Reporting a Vulnerability

Please do not report security vulnerabilities through public GitHub issues, discussions, pull requests, or social media.

To report a potential vulnerability, contact the project maintainer privately at:

**kevin@tapinvest.com**

Include as much of the following information as possible:

- A clear description of the vulnerability
- The affected version or commit
- Steps to reproduce the issue
- The potential impact
- Any proof-of-concept code or screenshots
- Suggested remediation, when available

Please avoid accessing, modifying, or deleting data that does not belong to you while investigating a potential issue.

## Response Process

After a report is received, the project maintainers will attempt to:

1. Confirm receipt of the report.
2. Review and reproduce the issue.
3. Assess severity and impact.
4. Develop and test a remediation.
5. Publish an update or mitigation when appropriate.
6. Credit the reporter, unless anonymity is requested.

Response times may vary based on the complexity and severity of the issue.

## Scope

Security reports may include vulnerabilities involving:

- Command-line input handling
- File-system access
- Path traversal
- Unsafe assistant metadata parsing
- Dependency vulnerabilities
- Prompt export or documentation generation
- Package installation and distribution
- Continuous integration workflows
- Exposure of secrets, credentials, or private data

General bugs, feature requests, and documentation issues should be submitted through the normal GitHub issue process.

## Responsible Disclosure

Please provide the maintainers a reasonable amount of time to investigate and address a reported vulnerability before making it public.

The project maintainers will make a good-faith effort to communicate progress and coordinate disclosure when necessary.

## Security Best Practices for Users

Users should:

- Install Agentic Assistants only from trusted sources.
- Review assistant definitions before running or exporting them.
- Avoid storing secrets or credentials in assistant files.
- Keep Python and project dependencies current.
- Review generated output before using it in production systems.
- Run the framework with the minimum file-system permissions required.
- Use isolated environments for testing untrusted assistant definitions.

## Disclaimer

Agentic Assistants is provided without warranty. Users are responsible for evaluating whether the framework is appropriate for their environment and security requirements.