import json

offers = []
with open('input.txt', 'r') as file:
    offers_count = int(file.readline().strip())
    lines = file.readlines()[0:]
    for line_num in range(offers_count):
        offers += json.loads(lines[line_num].strip())['offers']

res = {'offers': sorted(offers, key=lambda row: (row['price'], row['offer_id'], row["market_sku"]))}
with open('output.txt', 'w') as file:
    json.dump(res, file)