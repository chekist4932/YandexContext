import requests

with open('input.txt', 'r') as file:
    parameters = file.readlines()

uri = parameters[0].strip()
port = int(parameters[1])
a = int(parameters[2])
b = int(parameters[3])

url = f'{uri}:{port}'

response = requests.get(url=url, params={"a": a, "b": b})
res: list = response.json()
res.sort()
with open('output.txt', 'w') as file:
    file.write('\n'.join([str(x) for x in res]).strip())