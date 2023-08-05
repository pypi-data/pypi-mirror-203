from argparse import ArgumentParser
from datetime import date


def get_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--date",
        action="store",
        type=date.fromisoformat,
        default=date.today(),
        help="date of diary to view",
    )
    return parser
