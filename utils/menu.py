# TODO make all keys lower-case?
import time


class Menu:
    def __init__(self, menu_url):
        self._url = menu_url
        self._data = {}
        self._name_to_id = {}
        self._update_time = 0

    def should_update(self, time_per_update=86400):
        time_passed = time.time() - self._update_time
        return time_passed >= time_per_update  # day in seconds (sec*min*hrs, 60*60*24)

    def add_category(self, category_id, category_name, items):
        # For each category, map each dish id to its properties
        items_dict = {}
        item_props = ["dishId", "dishName", "dishDescription", "dishPrice"]
        for item in items:
            items_dict[item["dishId"]] = {prop: item[prop] for prop in item_props}

        self._data[category_id] = items_dict
        self._name_to_id[category_name] = category_id

    def get_dish(self, category_name, dish_id):
        dish_id = int(dish_id)
        category = self.get_category(category_name)
        if dish_id not in category:
            raise Exception("dish not found in category!")

        return category[dish_id]

    def get_category(self, category_name):
        if category_name not in self._name_to_id:
            raise Exception("category name does'nt exists!")

        category_id = self._name_to_id[category_name]
        if category_id not in self._data:
            raise Exception("invalid category id")  # mainly for debugging

        return self._data[category_id]
