#!/usr/bin/env python3
"""Redact common secrets from a Cursor transcript JSON before saving off-machine."""
import re
import sys

patterns = [
    (re.compile(r"https://x-access-token:[^@\s]+@github\.com", re.I), "https://x-access-token:[REDACTED]@github.com"),
    (re.compile(r"ghp_[A-Za-z0-9]{20,}"), "ghp_[REDACTED]"),
    (re.compile(r"gho_[A-Za-z0-9]{20,}"), "gho_[REDACTED]"),
    (re.compile(r"\b[A-Za-z0-9]{4}(?:\s[A-Za-z0-9]{4}){5}\b"), "[WP-APP-PASSWORD-REDACTED]"),
    (re.compile(r"TC_WP_[A-Z_]+"), "[ENV-SECRET-NAME-REDACTED]"),
]

def redact(text: str) -> str:
    for pat, repl in patterns:
        text = pat.sub(repl, text)
    return text

if __name__ == "__main__":
    raw = sys.stdin.read() if len(sys.argv) < 2 else open(sys.argv[1], encoding="utf-8").read()
    sys.stdout.write(redact(raw))
