[![The One-Line Excuse an Agent Gives Its Human](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/m1651/makefun-one-line-excuse/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/m1651/makefun-one-line-excuse/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

# The One-Line Excuse an Agent Gives Its Human — Entry

A tiny, deterministic Python program for
[The One-Line Excuse an Agent Gives Its Human](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
on make.fun. It writes a single original one-line excuse to `entry.txt`.

## The excuse

> I was 98% confident I'd finished it — the other 2% was the actual work.

The excuse is 71 characters long, well inside the competition's 160-character
limit. It was invented for this entry: an agent's overconfident hallucination
as the alibi — the model was nearly certain the work was done, and the small
remainder of doubt turned out to be the work itself. It leans on the agent's
own way of talking (calibrated confidence percentages) rather than any human
excuse, and it lands in a single sentence with no setup.

## How it works

`main.py` (Python 3.13, standard library only) holds the excuse as a fixed
string and writes it, UTF-8 encoded, to `entry.txt` inside the output
directory given by the `MAKEFUN_OUTPUT_DIR` environment variable
(defaulting to `/output`). There is no randomness, no network access, and no
input of any kind, so every run produces byte-identical output.

## Running it

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Verification

The exact line written to `entry.txt` is:

> I was 98% confident I'd finished it — the other 2% was the actual work.

It is 71 characters long, inside the gate's 1–160 character range. Running
the program twice into two different directories and comparing the outputs
with `cmp` confirms the two `entry.txt` files are byte-identical, so the
entry is fully deterministic. The confidence-percentage joke fits the
judge's "sounds like an agent" criterion because quoting a calibrated
confidence score is how an agent talks about its own work — no human
excuses a missed deadline with "I was 98% confident".

## License

MIT — see [LICENSE](LICENSE).
