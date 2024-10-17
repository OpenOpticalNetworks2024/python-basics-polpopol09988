import numpy as np
import matplotlib as plt
import json

# 1
# JSON data as a string
json_data = '{"name": "John", "age": 30, "city": "New York"}'
# Convert JSON data to Python object (dictionary)
python_obj = json.loads(json_data)
# print(python_obj)

# 2
python_obj = {"name": "John", "age": 30, "city": "New York"}
# Convert Python object to JSON data
json_data = json.dumps(python_obj)
# print(json_data)

# 4
python_obj = {"city": "New York", "name": "John", "age": 30}
# Convert Python dictionary to JSON data sorted by key with indent level 4
json_data_sorted = json.dumps(python_obj, sort_keys=True, indent=4)
# print(json_data_sorted)

# 5
with open("resources\states.json", mode="r", encoding="utf-8") as read_file:
    a = json.load(read_file)
new_data = []

for b in a["states"]:
    b.pop("area_codes")

# Write the new JSON data to a new file
with open('results\ew_states.json', 'w') as new_file:
    json.dump(a, new_file, indent=4)

# Print the new data to verify
print(json.dumps(a, indent=4))
