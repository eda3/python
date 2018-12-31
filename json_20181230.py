import json
string_of_json_data = '{"name": "Zonphie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

json_data_as_python_value = json.loads(string_of_json_data)

print(json_data_as_python_value)
