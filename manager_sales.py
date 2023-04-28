import json

with open('manager_sales.json', 'r') as file:
    data = json.load(file)

    manager = []
    money = 0

    for i in data:
        total = 0

        for j in i['cars']:
            total += j['price']

        if total > money:
            money = total
            manager = i['manager']

    print(manager['first_name'], manager['last_name'], money)
