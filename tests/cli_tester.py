import requests
import os
from collections import defaultdict
import json

# os.environ['NO_PROXY'] = "127.0.0.1"


def print_main_menu():
    print("Choose an option from below:")
    print("1. Pizzas")
    print("2. Drinks")
    print("3. Desserts")
    print("4. Submit order")
    print("-"*10)


def print_menu(menu):
    for item in menu:
        print(f"{item['dishName']}:\t|| id:{item['dishId']} |\tprice:{item['dishPrice']} ||")


def new_order():
    return {"drinks": [], "desserts": [], "pizzas": []}


if __name__ == "__main__":
    order = new_order()

    option = 0
    while True:
        url = "http://127.0.0.1:5000/"
        category = ""

        print(f"{'*'*5}\nYour order: {order}\n{'*'*5}")
        print_main_menu()
        option = int(input())
        if option == 1:
            url = url + "pizzas"
            category = "pizzas"
        elif option == 2:
            url = url + "drinks"
            category = "drinks"
        elif option == 3:
            url = url + "desserts"
            category = "desserts"
        elif option == 4:
            # order_json = json.dumps(order)
            response = requests.post(url + "order", json=order)
            print(response.text)
            order = new_order()
            print("Order submitted!\n" + "-"*20)
            continue

        response = requests.get(url)
        menu = response.json()
        print_menu(menu)
        print("Enter item id:", end=" ")
        option = input()

        order[category].append(option)


