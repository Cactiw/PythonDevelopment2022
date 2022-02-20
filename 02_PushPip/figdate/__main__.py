import locale

from argparse import ArgumentParser

from .figdate import figlet_date


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        '--format', type=str
    )
    parser.add_argument(
        '--font', type=str
    )
    args = parser.parse_args()

    locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

    print(figlet_date(args.format, args.font))

