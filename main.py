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

for route in routes:
    print(f'{route["from"]} -> {route["to"]}: {route["price"]}')
