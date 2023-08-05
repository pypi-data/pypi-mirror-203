from .client import get_client
from .diary import get_diary, print_diary
from rich.prompt import Prompt


def create_meal(client, diary):
    meals = diary["meals"]
    order = max([meal["order"] for meal in meals]) + 1

    name = Prompt.ask("Enter meal name", default=f"Meal {order}")
    return client.create_meal(diary_id=diary["id"], name=name, order=order)


def select_meal(diary):
    meals = diary["meals"]

    if len(meals) == 1:
        meal = meals[0]
    else:
        print_diary(diary)
        meal_order = Prompt.ask(
            "Choose meal",
            default=meals[0]["order"],
            choices=[str(m["order"]) for m in meals],
        )
        meal = [meal for meal in meals if meal["order"] == int(meal_order)][0]

    return meal


if __name__ == "__main__":
    client = get_client()
    diary = get_diary(client)
    create_meal(client, diary)
    print_diary(get_diary(client))
