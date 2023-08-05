import requests
import os
from datetime import date
from typing import Optional, Dict
import json
from getpass import getpass
from pydantic import validate_arguments
from pathlib import Path


class UnathorizedError(Exception):
    pass


class FooderClient:
    """FooderClient."""

    def __init__(
        self,
        token_cache="~/.cache/fooder/.token",
        refresh_token_cache="~/.cache/fooder/.refresh_token",
        url="https://fooderapi.domandoman.xyz/api",
    ) -> None:
        """__init__.

        :param token_cache:
        :param url:
        :rtype: None
        """
        self.url = url
        self.session = requests.Session()
        self.refresh_token_cache = os.path.expanduser(refresh_token_cache)
        self.token_cache = os.path.expanduser(token_cache)
        self.session.headers["Accept"] = "application/json"

    def read_token_cache(self) -> None:
        """read_token_cache.

        :rtype: None
        """
        if os.path.exists(self.token_cache):
            with open(self.token_cache, "r") as f:
                self.session.headers["Authorization"] = f.read()
        else:
            raise UnathorizedError(
                "Token cache not found, please run `python client.py --login` first"
            )

    def save_token_cache(self) -> None:
        """save_token_cache.

        :rtype: None
        """
        folder = os.path.dirname(self.token_cache)
        Path(folder).mkdir(parents=True, exist_ok=True)

        with open(self.token_cache, "w") as f:
            f.write(self.session.headers["Authorization"])

    def save_refresh_token_cache(self, token: str) -> None:
        """save_refresh_token_cache.

        :param token:
        :type token: str
        :rtype: None
        """
        folder = os.path.dirname(self.refresh_token_cache)
        Path(folder).mkdir(parents=True, exist_ok=True)

        with open(self.refresh_token_cache, "w") as f:
            f.write(token)

    def read_refresh_token_cache(self) -> str:
        """read_refresh_token_cache.

        :rtype: str
        """
        if os.path.exists(self.refresh_token_cache):
            with open(self.refresh_token_cache, "r") as f:
                return f.read()
        else:
            raise UnathorizedError(
                "Token cache not found, please run `python client.py --login` first"
            )

    def set_token(self, token: str) -> None:
        """set_token.

        :param token:
        :type token: str
        :rtype: None
        """
        self.session.headers["Authorization"] = "Bearer " + token

    @validate_arguments
    def login(self, username: str, password: str) -> None:
        """login.

        :param username:
        :type username: str
        :param password:
        :type password: str
        :rtype: None
        """
        data = {"username": username, "password": password}
        response = self.session.post(self.url + "/token", data=data)
        if response.status_code != 200:
            raise UnathorizedError(
                "Invalid username or password, please check your username and password"
            )
        response = response.json()
        self.set_token(response["access_token"])
        self.save_token_cache()
        self.save_refresh_token_cache(response["refresh_token"])

    def refresh_token(self) -> None:
        """refresh_token.

        :rtype: None
        """
        data = {"refresh_token": self.read_refresh_token_cache()}
        response = self.session.post(self.url + "/token/refresh", json=data)
        if response.status_code != 200:
            raise UnathorizedError("Refresh token expired!")
        response = response.json()
        self.set_token(response["access_token"])
        self.save_token_cache()
        self.save_refresh_token_cache(response["refresh_token"])

    def get(self, path: str, params: Optional[Dict] = None) -> Optional[Dict]:
        """get.

        :param path:
        :type path: str
        :param params:
        :type params: Optional[Dict]
        :rtype: Optional[Dict]
        """
        if self.session.headers.get("Authorization") is None:
            self.read_token_cache()

        if params is None:
            params = {}

        response = self.session.get(self.url + path, params=params)
        if response.status_code == 401:
            self.refresh_token()
            response = self.session.get(self.url + path, params=params)

        response.raise_for_status()
        return response.json()

    def delete(self, path: str) -> None:
        """delete.

        :param path:
        :type path: str
        :rtype: None
        """
        if self.session.headers.get("Authorization") is None:
            self.read_token_cache()

        response = self.session.delete(self.url + path)

        if response.status_code == 401:
            self.refresh_token()
            response = self.session.delete(self.url + path)

        response.raise_for_status()

    def post(self, path: str, data: Optional[Dict] = None) -> Optional[Dict]:
        """post.

        :param path:
        :type path: str
        :param data:
        :type data: Optional[Dict]
        :rtype: Optional[Dict]
        """
        if self.session.headers.get("Authorization") is None:
            self.read_token_cache()

        if data is None:
            data = {}

        response = self.session.post(self.url + path, json=data)

        if response.status_code == 401:
            self.refresh_token()
            response = self.session.post(self.url + path, json=data)

        response.raise_for_status()
        return response.json()

    def patch(self, path: str, data: Optional[Dict] = None) -> Optional[Dict]:
        """patch.

        :param path:
        :type path: str
        :param data:
        :type data: Optional[Dict]
        :rtype: Optional[Dict]
        """
        if self.session.headers.get("Authorization") is None:
            self.read_token_cache()
        if data is None:
            data = {}
        response = self.session.patch(self.url + path, json=data)
        response.raise_for_status()
        return response.json()

    @validate_arguments
    def list_products(
        self,
        query: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict:
        """list_products.

        :param query:
        :type query: Optional[str]
        :param limit:
        :type limit: Optional[int]
        :param offset:
        :type offset: Optional[int]
        :rtype: Dict
        """
        params = {}
        if query:
            params["q"] = query
        response = self.get("/product", params=params)
        return response

    @validate_arguments
    def create_product(
        self,
        name: str,
        protein: float,
        carb: float,
        fat: float,
    ) -> Dict:
        """create_product.

        :param name:
        :type name: str
        :param protein:
        :type protein: float
        :param carb:
        :type carb: float
        :param fat:
        :type fat: float
        :rtype: Dict
        """
        data = {"name": name, "protein": protein, "carb": carb, "fat": fat}
        return self.post("/product", data=data)

    @validate_arguments
    def get_diary(self, date_: Optional[date] = None) -> Dict:
        """get_diary.

        :param date:
        :type date: Optional[str]
        :rtype: Dict
        """
        if date_ is None:
            date_ = date.today()
        params = {"date": date_.strftime("%Y-%m-%d")}
        response = self.get("/diary", params=params)
        return response

    @validate_arguments
    def create_meal(
        self,
        diary_id: int,
        name: str,
        order: int,
    ) -> Dict:
        """create_meal.

        :param diary_id:
        :type diary_id: int
        :param name:
        :type name: str
        :param order:
        :type order: int
        :rtype: Dict
        """
        data = {"diary_id": diary_id, "name": name, "order": order}
        return self.post("/meal", data=data)

    @validate_arguments
    def add_entry(
        self,
        product: int,
        grams: float,
        meal: Optional[int] = None,
    ) -> Dict:
        """add_entry.

        :param product:
        :type product: int
        :param grams:
        :type grams: float
        :param meal:
        :type meal: Optional[int]
        :rtype: Dict
        """
        if meal is None:
            meal = self.get_diary()["meals"][0]["id"]

        data = {"product_id": product, "grams": grams, "meal_id": meal}
        response = self.post("/entry", data=data)

        return response

    @validate_arguments
    def edit_entry(
        self,
        entry: int,
        grams: Optional[float] = None,
        product: Optional[int] = None,
        meal: Optional[int] = None,
    ) -> Dict:
        """edit_entry.

        :param entry:
        :type entry: int
        :param product:
        :type product: Optional[int]
        :param grams:
        :type grams: Optional[float]
        :param meal:
        :type meal: Optional[int]
        :rtype: Dict
        """
        if meal is None:
            meal = self.get_diary()["meals"][0]["id"]

        data = {}
        if product is not None:
            data["product_id"] = product
        if grams is not None:
            data["grams"] = grams
        if meal is not None:
            data["meal_id"] = meal

        response = self.patch(f"/entry/{entry}", data=data)
        return response

    @validate_arguments
    def delete_entry(
        self,
        entry: int,
    ) -> None:
        """delete_entry."""
        self.delete(f"/entry/{entry}")


def get_client() -> FooderClient:
    client = FooderClient()
    return client


def pprint(response: str) -> None:
    print(json.dumps(response, indent=2))


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("ARGS", nargs="*")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l", "--login", action="store_true", help="login to fooder")
    group.add_argument(
        "-p",
        "--products",
        action="store_true",
        help="list products with params: q limit offset",
    )
    group.add_argument(
        "-a",
        "--add-product",
        action="store_true",
        help="add product with params: name protein carb fat",
    )
    group.add_argument(
        "-d", "--diary", action="store_true", help="get diary with params: date"
    )
    group.add_argument(
        "-e",
        "--entry",
        action="store_true",
        help="create entry with params: product quantity meal",
    )
    group.add_argument(
        "--delete-entry", action="store_true", help="delete entry with param: entry"
    )
    group.add_argument(
        "--edit-entry",
        action="store_true",
        help="edit entry with params: entry grams product meal",
    )
    group.add_argument(
        "-m",
        "--meal",
        action="store_true",
        help="create meal with params: diary name order",
    )
    args = parser.parse_args()

    c = FooderClient()

    if args.login:
        username = input("Username: ")
        password = getpass("Password: ")
        c.login(username, password)

    if args.products:
        pprint(c.list_products(*args.ARGS))

    if args.add_product:
        pprint(c.create_product(*args.ARGS))

    if args.diary:
        pprint(c.get_diary(*args.ARGS))

    if args.entry:
        pprint(c.add_entry(*args.ARGS))

    if args.delete_entry:
        pprint(c.delete_entry(*args.ARGS))

    if args.edit_entry:
        pprint(c.edit_entry(*args.ARGS))

    if args.meal:
        pprint(c.create_meal(*args.ARGS))
