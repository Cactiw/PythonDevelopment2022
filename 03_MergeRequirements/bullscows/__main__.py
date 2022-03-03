import urllib
from argparse import ArgumentParser

import requests as requests

from .bullcows import gameplay, ask, inform


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        '--dict', type=str
    )
    parser.add_argument(
        '--length', type=int
    )
    args = parser.parse_args()

    text = requests.get(args.dict).text
    words = list(filter(bool, map(
        lambda word: word[:args.length] if len(word) >= args.length else None, text.splitlines()
    )))
    gameplay(ask, inform, words)

