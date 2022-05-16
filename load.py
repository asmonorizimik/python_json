
# loads():
# Parse JSON (Convert from JSON to Python)
# json.loads() method can parse a json string and the result will be a Python dictionary.
# Syntax:

# json.loads(json_string)





# Python read JSON file
# json.load() method can read a file which contains a JSON object. Consider a file named employee.json 
# which contains a JSON object.

# Syntax:

# json.load(file_object)


import json
f = open('1data.json',)
data = json.load(f)
for i in data['details']:
    print(i)
f.close()




