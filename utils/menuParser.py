import requests
from utils.menu import Menu
import time


def valid_menu_url(menu_url):
    return True  # TODO if there is time


class MenuParser:
    def parse(self, menu_url: str):
        if not valid_menu_url(menu_url):
            raise Exception("bad menu url")

        page = requests.get(menu_url)
        data = page.json()["Data"]

        menu = Menu(menu_url)
        for cat_data in data["categoriesList"]:
            menu.add_category(cat_data["categoryID"], cat_data["categoryName"], cat_data["dishList"])

        menu._update_time = time.time()
        return menu
