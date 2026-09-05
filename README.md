# No-Face Agent Factory

No-Face Agent Factory is an independent AI product and automation project by
Denilson Mattos Alvarez. It explores how a coordinated group of specialized
agents can turn an editorial idea into a reviewable vertical video while
keeping human judgment, traceability and recovery inside the process.

## What this showcase demonstrates

- Product thinking applied to an end-to-end media workflow
- Multi-agent orchestration with explicit responsibilities and state contracts
- Human-in-the-loop quality gates for review and publishing
- Operational design covering monitoring, persistence, recovery and security
- A working product narrative presented through a real-voice video demo

The website is designed for hiring teams, managers and collaborators who want
to understand the problem, the system decisions and the value of the project
without needing access to its implementation.

## Public boundary

This is a deliberately sanitized presentation layer. It contains the static
showcase, synthetic interface data and the final demo media only. Production
source, operational configuration, prompts, credentials, logs, private data
and original voice recordings remain outside this repository.

Open `index.html` to review the showcase locally.

Run `python tools/audit_showcase.py` before publishing a change. The audit
rejects operational artifacts, local paths, secret references and unsupported
file types.
