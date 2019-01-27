import json
from pprint import pprint

with open('data.json') as f:
    raw_data = json.load(f)

data = (raw_data['statuses'][1])
pprint(data)
if ~data["truncated"]:
    print(data["text"])
