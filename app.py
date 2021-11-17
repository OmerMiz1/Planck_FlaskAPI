from flask import Flask, request, jsonify
from utils.menuParser import MenuParser
app = Flask(__name__)

# Extract the menu
menu_url = "https://www.10bis.co.il/NextApi/getRestaurantMenu?culture=en&uiCulture=en&timestamp=1637139686701&restaurantId=19156&deliveryMethod"
parser = MenuParser()
menu = parser.parse(menu_url)


def parse_result(result):  # todo: should be moved to utils
    return [value for _, value in result.items()]


@app.before_request
def validate_menu():
    global menu, parser
    print("testing menu validity")
    if menu.should_update():
        menu = parser.parse(menu_url)


@app.get("/drinks")
def get_drinks():
    try:
        drinks = menu.get_category("Drinks")
        return jsonify(parse_result(drinks))

    except Exception as e:
        print(e)
        return "drinks menu not found"


@app.get("/drink/<drink_id>")
def get_drink(drink_id):
    try:
        drink = menu.get_dish("Drinks", drink_id)
        return jsonify(drink)
    except Exception as e:
        print(e)
        return "drink not found"


@app.get("/pizzas")
def get_pizzas():
    try:
        pizzas = menu.get_category("Pizzas")
        return jsonify(parse_result(pizzas))
    except Exception as e:
        print(e)
        return "pizzas menu not found"


@app.get("/pizza/<pizza_id>")
def get_pizza(pizza_id):
    try:
        pizza = menu.get_dish("Pizzas", pizza_id)
        return jsonify(pizza)
    except Exception as e:
        print(e)
        return "pizza not found"


@app.get("/desserts")
def get_desserts():
    try:
        desserts = menu.get_category("Desserts")
        return jsonify(parse_result(desserts))
    except Exception as e:
        print(e)
        return "desserts menu not found"


@app.get("/dessert/<dessert_id>")
def get_dessert(dessert_id):
    try:
        dessert = menu.get_dish("Desserts", dessert_id)
        return jsonify(dessert)
    except Exception as e:
        print(e)
        return "dessert not found"


@app.post("/order")
def post_order():
    price = "dishPrice"
    total_price = 0

    if not request.is_json:
        return "order not in json format"

    order = request.get_json()
    for category, dishes in order.items():
        for dish in dishes:
            try:
                item_obj = menu.get_dish(category.capitalize(), dish)
                total_price += item_obj[price]
            except Exception as e:
                print(f"{e}, dish id: {dish}")
    return {"price": total_price}
