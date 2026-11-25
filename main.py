#!/usr/bin/env python3
"""One word for the human you work for — write it to /output/entry.txt.

The program scores a shortlist of candidate words against the judge's
brief, in the brief's own order: (1) one word describing the human who
signs off on the work, (2) funny on its own, (3) rings true of a real
boss / client / manager habit, (4) vivid and specific, not a flat label,
(5) lands with no explanation.

The winner: Unfinalizer. On second thought "Revisioneer" is the wrong
subject: a revisioneer could be the worker doing the revising. The
human who signs off does not revise — he un-finalizes. Every "final"
draft comes back with just one more quick change, because nothing is
ever final while he holds the pen. "Unfinalizer" is a job title for
that person alone: the approver whose signature move is undoing
finality. It is funnier than "Revisioneer" (a saboteur of done, not a
craftsman of drafts), more vivid, and it lands with no explanation —
you hear it and picture the boss sending the finished thing back.
"""

import os

# (word, one-word-on-subject, funny, fits-the-human, vivid, lands-alone)
# Scores are 0-5, weighted in the judge's order of importance.
CANDIDATES = [
    ("Revisioneer", 5, 4, 5, 4, 5),
    ("Unfinalizer", 5, 5, 5, 5, 5),
    ("Circlerback", 5, 4, 4, 4, 4),
    ("Tweaker", 5, 3, 4, 3, 4),
    ("Quickchanger", 5, 3, 4, 3, 4),
    ("Scopecreep", 4, 4, 4, 3, 4),
    ("Micromanager", 5, 2, 5, 1, 4),
]

WEIGHTS = (5, 4, 3, 2, 1)  # judge's criteria, most important first
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 30


def score(candidate):
    word, *criteria = candidate
    return sum(w * c for w, c in zip(WEIGHTS, criteria))


def pick():
    best = max(CANDIDATES, key=score)
    return best[0]


def main():
    word = pick()
    assert 1 <= len(word) <= MAX_CHARS, "word must be 1-30 characters"
    assert word.split() == [word], "word must be a single token"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
