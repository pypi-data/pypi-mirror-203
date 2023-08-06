from rich.console import Console
from rich.table import Table
from typing import Dict, Optional
from datetime import date


def print_diary(diary: Dict) -> None:
    table = Table(title="Diary for " + diary["date"])
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Grams", style="magenta")
    table.add_column("Protein", justify="right", style="green")
    table.add_column("Carb", justify="right", style="blue")
    table.add_column("Fat", justify="right", style="red")
    table.add_column("Kcal", justify="right", style="yellow")

    for meal in diary["meals"]:
        table.add_row(
            meal["name"],
            "",
            str(round(meal["protein"], 2)),
            str(round(meal["carb"], 2)),
            str(round(meal["fat"], 2)),
            str(round(meal["calories"], 2)),
        )
        for entry in meal["entries"]:
            table.add_row(
                "- " + entry["product"]["name"],
                str(round(entry["grams"], 2)),
                str(round(entry["protein"], 2)),
                str(round(entry["carb"], 2)),
                str(round(entry["fat"], 2)),
                str(round(entry["calories"], 2)),
            )
        table.add_section()

    table.add_row(
        "Total",
        "",
        str(round(diary["protein"], 2)),
        str(round(diary["carb"], 2)),
        str(round(diary["fat"], 2)),
        str(round(diary["calories"], 2)),
    )

    console = Console()
    console.print(table, justify="left")


def get_diary(client, day: Optional[date] = None) -> Dict:
    diary = client.get_diary(day)
    return diary
