from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]

ALLOWED_SUFFIXES = {
    ".css",
    ".html",
    ".js",
    ".md",
    ".png",
    ".py",
    ".yml",
}

FORBIDDEN_FILENAMES = {
    ".env",
    "compose.yaml",
    "docker-compose.yml",
    "dockerfile",
}

FORBIDDEN_PATTERNS = {
    "repository link": re.compile(r"(?:github\.com|git@|\.git(?:\s|$))", re.I),
    "local network": re.compile(r"(?:localhost|127\.0\.0\.1|0\.0\.0\.0)", re.I),
    "local path": re.compile(r"(?:[a-z]:\\users\\|/home/|documents\\codex)", re.I),
    "secret reference": re.compile(r"(?:x-api-key|api[_ -]?key|password\s*=|secret\s*=)", re.I),
    "operational file": re.compile(r"(?:\.env|docker\s+compose|\.csv(?:\s|$))", re.I),
}

TEXT_SUFFIXES = {".css", ".html", ".js", ".md", ".py", ".yml"}


def iter_public_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    )


def main() -> int:
    errors: list[str] = []

    for path in iter_public_files():
        relative = path.relative_to(ROOT)
        lower_name = path.name.lower()

        if lower_name in FORBIDDEN_FILENAMES:
            errors.append(f"forbidden filename: {relative}")

        if path.suffix.lower() not in ALLOWED_SUFFIXES and path.name not in {".gitignore", "LICENSE"}:
            errors.append(f"unexpected file type: {relative}")

        if relative.as_posix() == "tools/audit_showcase.py":
            continue

        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue

        content = path.read_text(encoding="utf-8")

        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(content):
                errors.append(f"{label} found in {relative}")

    if errors:
        print("Public boundary audit: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Public boundary audit: OK | files={len(iter_public_files())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
