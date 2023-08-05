from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich.console import Console
from rich.table import Table


def select_product(client):
    console = Console()
    query = Prompt.ask("Enter product name")
    products = client.list_products(query=query)["products"]

    table = Table(title="Found products")
    table.add_column("Number")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Protein", justify="right", style="green")
    table.add_column("Carb", justify="right", style="blue")
    table.add_column("Fat", justify="right", style="red")
    table.add_column("Kcal", justify="right", style="yellow")

    for i, product in enumerate(products):
        table.add_row(
            str(i),
            product["name"],
            str(round(product["protein"], 2)),
            str(round(product["carb"], 2)),
            str(round(product["fat"], 2)),
            str(round(product["calories"], 2)),
        )

    console.print(table, justify="left")

    if len(products) == 0:
        add_new = Confirm.ask("No products found, create new one?", default=True)
        if not add_new:
            return
        return add_product(client)
    elif len(products) == 1:
        product = products[0]
        response = Confirm.ask("Found only one entry, proceed with it?", default=True)
        if not response:
            return
    else:
        product_id = Prompt.ask(
            "Choose product", default=0, choices=[str(i) for i in range(len(products))]
        )
        product = products[int(product_id)]

    return product


def add_product(client):
    console = Console()
    name = Prompt.ask("Enter product name")
    protein = float(Prompt.ask("Enter protein"))
    carb = float(Prompt.ask("Enter carb"))
    fat = float(Prompt.ask("Enter fat"))

    calories = protein * 4 + carb * 4 + fat * 9

    table = Table(title="Product")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Protein", justify="right", style="green")
    table.add_column("Carb", justify="right", style="blue")
    table.add_column("Fat", justify="right", style="red")
    table.add_column("Kcal", justify="right", style="yellow")

    table.add_row(
        name,
        str(round(protein, 2)),
        str(round(carb, 2)),
        str(round(fat, 2)),
        str(round(calories, 2)),
    )

    console.print(table, justify="left")

    proceed = Confirm.ask("Add this product?", default=True)
    if not proceed:
        return

    product = client.create_product(
        name=name,
        protein=protein,
        carb=carb,
        fat=fat,
    )

    console.print(Text("Product added", style="bold green"))
    return product


if __name__ == "__main__":
    from .client import get_client

    add_product(get_client())
