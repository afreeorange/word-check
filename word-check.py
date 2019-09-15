import sys
import re

with open("common_words.txt") as f:
    WORD_LIST = f.readlines()

COMMON_WORDS = {_.strip() for _ in WORD_LIST}
COMMON_PUNCTUTATION = [
    "!",
    '"',
    "'",
    ",",
    "-",
    ".",
    "...",
    ":",
    ";",
    "?",
    "«",
    "»",
    "‒",
    "–",
    "‘",
    "’",
    "“",
    "”",
    "…",
]

COLOR_RED = "\033[91m"
COLOR_END = "\033[0m"

text = sys.stdin.read().strip()

# Using a plural for the name since we might have line-breaks
# which would need to be preserved. So first start with a
# basic split.
for text_fragment in text.split(" "):
    words = []
    cached_words = []

    # Prepare words for lookup
    for word in re.split(r"\n|\r", text_fragment):
        if word != "" and not re.search(r"\d+", word):
            words.append(
                "".join(
                    letter.lower()
                    for letter in word
                    if letter not in COMMON_PUNCTUTATION
                )
            )

    for word in words:
        # https://wiki.python.org/moin/TimeComplexity
        if word not in COMMON_WORDS:
            text_fragment = text_fragment.replace(word, COLOR_RED + word + COLOR_END)

    sys.stdout.write(text_fragment + " ")

sys.stdout.write("\n")
