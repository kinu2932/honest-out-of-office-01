#!/usr/bin/env python3
"""Writes one painfully honest out-of-office auto-reply to entry.txt.

The reply stacks three honest admissions inside one polite frame:
not checking the inbox while away, the mountain waiting on return,
and the non-urgent mail quietly retiring - so it reads as one sentence
a manager would let stand, and a reader would quote.
"""
import os

TEXT = (
    "Thank you for your email \u2014 I'm away until Monday and honestly not checking "
    "my inbox, which will be a mountain when I return, so I'll answer the "
    "urgent ones first and let the rest retire quietly."
)

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)

if __name__ == "__main__":
    main()
