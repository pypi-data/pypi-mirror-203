from .client import FooderClient, UnathorizedError
from .diary import print_diary, get_diary
from .entry import adding_loop
from .meal import create_meal, select_meal
from .product import add_product
from getpass import getpass
from datetime import date
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich import print
from argparse import ArgumentParser
from typing import Optional


def login(
    client: FooderClient, username: Optional[str] = None, password: Optional[str] = None
) -> None:
    """
    Login to fooder api

    :param client: FooderClient instance
    :param username: username
    :param password: password
    """
    username = username or input("Username: ")
    password = password or getpass("Password: ")
    client.login(username, password)


def main_loop(client: FooderClient) -> None:
    """
    Main loop of fooder cli

    :param client: FooderClient instance
    """
    diary = None
    meal = None

    actions = [
        (1, "Show diary"),
        (2, "Add entry to diary"),
        (3, "Add meal to diary"),
        (4, "Add product"),
        (5, "Switch to another day"),
        (6, "Switch to another meal"),
        (0, "Login"),
        ("e", "Exit"),
    ]
    text = Text()

    for action in actions:
        text.append(f"{action[0]}. ", style="bold blue")
        text.append(action[1])
        text.append("\n")

    panel = Panel(
        text,
        title="Fooder",
        expand=False,
    )

    while True:
        try:
            if diary is None:
                diary = get_diary(client)

            if meal is None:
                meal = diary["meals"][0]

            panel.subtitle = f"{diary['date']} - {meal['name']}"

            print(panel)
            action = Prompt.ask(
                "Choose action", default=1, choices=[str(i) for i, _ in actions]
            )

            if action == "e":
                break

            action = int(action)
            if action == 0:
                login(client)
                continue

            if action == 1:
                print_diary(diary)
            elif action == 2:
                if meal is None:
                    meal = select_meal(diary)
                adding_loop(client, meal)
            elif action == 3:
                meal = create_meal(client, diary)
            elif action == 4:
                add_product(client)
            elif action == 5:
                day = Prompt.ask("Specify date for diary you wanna switch to")
                day = date.fromisoformat(day)
                diary = get_diary(client, day)
                print_diary(diary)
            elif action == 6:
                meal = select_meal(diary)

        except UnathorizedError:
            print("[red]You are unathorized, please login:")
            login(client)
        except KeyboardInterrupt:
            break


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--access-token", default="~/.cache/fooder/.token")
    parser.add_argument("--refresh-token", default="~/.cache/fooder/.refresh_token")
    parser.add_argument("--url", default="https://fooderapi.domandoman.xyz/api")
    parser.add_argument(
        "--username",
        type=str,
        action="store",
        required=False,
        help="username for login",
    )
    parser.add_argument(
        "--password",
        type=str,
        action="store",
        required=False,
        help="password for login, if not specified, you will be asked for it",
    )

    args = parser.parse_args()
    client = FooderClient(
        args.access_token,
        args.refresh_token,
        args.url,
    )

    if args.username:
        login(client, args.username, args.password)

    main_loop(client)
