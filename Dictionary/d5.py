cities = {
    "Pune": 3000000,
    "Mumbai": 20000000,
    "Delhi": 19000000,
    "Nagpur": 2500000
}

city = input("Enter city to remove: ").capitalize()

if city in cities:
    del cities[city]
    print("Updated dictionary:", cities)
else:
    print("City not found")