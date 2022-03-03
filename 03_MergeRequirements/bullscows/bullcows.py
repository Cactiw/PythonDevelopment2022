import random

import textdistance


def bullscows(guess: str, secret: str) -> (int, int):
    return textdistance.hamming.similarity(guess, secret), textdistance.overlap.similarity(guess, secret) * len(secret)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = random.choice(words).lower()
    # print(f"Чит - загадал {secret}")
    guess = None
    attempts = 0

    while guess != secret:
        guess = ask("Введите слово: ", words).lower()
        inform("Быки: {}, Коровы: {}", *bullscows(guess, secret))
        attempts += 1
    return attempts


def ask(prompt: str, valid: list[str] = None) -> str:
    guess = input(prompt).lower()
    while guess not in tuple(map(lambda s: s.lower(), valid)):
        guess = input(prompt).lower()
    return guess


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

