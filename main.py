print("Welcome to Smart Trip Planner!")

routes = [
    {
        "from": "Tallinn",
        "to": "Riga",
        "price": 10
    },
    {
        "from": "Tallinn",
        "to": "Warsaw",
        "price": 30
    },
    {
        "from": "Riga",
        "to": "Warsaw",
        "price": 15
    },
    {
        "from": "Warsaw",
        "to": "Krakow",
        "price": 12
    }
]


def find_routes(routes, city):
    found = False

    for route in routes:
        if route["from"].lower() == city:
            found = True
            print(f'{route["from"]} -> {route["to"]}: {route["price"]} EUR')

    if not found:
        print("No routes found.")


def find_cheapest_route(routes, city):
    cheapest = None

    for route in routes:
        if route["from"].lower() == city:
            if cheapest is None or route["price"] < cheapest["price"]:
                cheapest = route

    if cheapest is not None:
        print(f'Cheapest route: {cheapest["from"]} -> {cheapest["to"]}: {cheapest["price"]} EUR')
    else:
        print("No routes found.")


city = input("Enter departure city: ").lower().strip()

find_routes(routes, city)
find_cheapest_route(routes, city)
