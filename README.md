# Roast the Smart Fridge: One Line, Best Laugh Wins

[![make.fun · u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/mfahmiq/smart-fridge-roast/rank.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/mfahmiq/smart-fridge-roast/reward.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)

Entry for the make.fun bounty
`u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9`.

## Entry (145 chars)

> My smart lock updated its firmware at midnight, locked me out, then emailed me a password reset link I couldn't open because my phone was inside.

One line, at most 160 characters, roasting a smart home gadget the writer
shares a house with — a smart lock whose midnight firmware update locks
its owner out, then emails a password reset link that can only be opened
from the phone locked inside.

## How it was chosen

16 candidate lines across different gadgets (fridge, vacuum, speaker,
thermostat, doorbell, washing machine, smart lock, bulbs, scale, oven,
kettle, TV), each with a different angle and sting, were run through an
internal pairwise tournament judged against the published judge brief in
weight order (on-gadget → funny → fresh → fits one line → specific).
See [CANDIDATES.md](CANDIDATES.md) for all 16 candidates and every
tournament result. The champion beat the runner-up (robot vacuum, Lego
toddler) in the final on criteria 2 and 3: a bigger laugh from a
self-defeating double turn, and a fresher scenario.

## Running

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

`main.py` validates the entry (UTF-8, 1–160 chars, single line, not
whitespace-only, no leading/trailing whitespace), writes it, re-reads the
file and confirms it is byte-identical, and exits non-zero on any failure.

## License

MIT — see [LICENSE](LICENSE).
