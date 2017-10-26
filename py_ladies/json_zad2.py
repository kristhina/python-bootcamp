import json

with open('py1.2zd.json') as json_data:
    data = json.load(json_data)

for ship in data:
    if ship['cost_in_credits'] == "unknown":
        ship['cost_in_credits'] = 0

sorted_data = sorted(data, key=lambda k: int(k['cost_in_credits']), reverse=True)

for ship in sorted_data:
    if ship['cost_in_credits'] == 0:
        ship['cost_in_credits'] = "unknown"

file = open("ships", "w")
for ship in sorted_data:
    file.write("{} costs {} credits.\n".format(ship["name"], ship["cost_in_credits"]))

file.close()

