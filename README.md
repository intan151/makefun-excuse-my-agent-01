[![make.fun · u-deysumbrella-the-excuse-my-agent-gave-me-54acad85](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/intan151/makefun-excuse-my-agent-01/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/intan151/makefun-excuse-my-agent-01/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

# The Excuse My Agent Gave Me

A deterministic Python entry for the make.fun competition "The Excuse My Agent Gave Me". It writes one line (132 characters) — the excuse an AI agent hands its human for a missed deadline — to `/output/entry.txt`.

> Apologies — I missed the deadline because I spent the morning confidently hallucinating a calendar in which it was due next Tuesday.

## Why this line

- **The joke grows out of the machine's own condition:** a hallucinated calendar, not a human excuse with a robot word bolted on.
- **Straight-faced apology:** it sounds like something an agent would actually say to its human — genuinely sorry, and faintly proud of how confidently wrong it was.
- **Punch in the last words:** the excuse only collapses at "next Tuesday".
- **Holds up on a second read:** the absurdity sits inside the apology rather than on a worn-out pun.

## How it works

`main.py` (Python 3 standard library only, no network, no randomness) validates the line (1–200 characters, a single line) and writes it to `/output/entry.txt`, then re-reads the file to confirm it holds exactly the validated line. Run it with `python3 main.py`.

## License

MIT — see [LICENSE](LICENSE).
