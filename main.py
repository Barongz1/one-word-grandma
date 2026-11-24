"""One Word From Grandma — entry for make.fun.

Writes one word to /output/entry.txt.
The word is exactly one word: the word their grandma would text about AI.
"""
import os

LINE = "Witchcraft!"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
