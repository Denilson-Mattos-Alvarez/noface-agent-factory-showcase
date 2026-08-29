# No-Face Agent Factory - Project Showcase

Public, standalone portfolio site for the No-Face Agent Factory project.

This repository contains only:

- a high-level product and architecture narrative;
- synthetic interface data;
- a purpose-generated hero image;
- the static files required to render the showcase.

It intentionally contains no production source, operational configuration,
workflow exports, API surface, prompts, logs, analytics or links to private
repositories.

Open `index.html` to review the site locally.

Run `python tools/audit_showcase.py` before publishing any change. The audit
fails when the public bundle contains operational files, local paths, secret
references or repository links.
