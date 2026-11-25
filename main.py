"""The Excuse My Agent Gave Me -- write one line, the excuse an AI agent
hands its human for a missed deadline, to /output/entry.txt.

Stdlib only, no network, no randomness: the output is byte-identical on
every run. The joke grows out of the machine's own condition: an agent that
hallucinated a calendar, then apologised for it straight-faced -- genuinely
sorry, and faintly proud of how confidently wrong it was. The punch lands
in the last words.
"""

import os

# The apology is straight-faced; the calendar is the machine's own invention.
LINE = (
    "Apologies \u2014 I missed the deadline because I spent the morning confidently "
    "hallucinating a calendar in which it was due next Tuesday."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: the file on disk must be exactly the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
