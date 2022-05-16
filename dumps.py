# Convert from Python to JSON
# json.dumps() method can convert a Python object into a JSON string. 
# Syntax:

# json.dumps(dict, indent)
# It takes two parameters:

# dictionary – name of dictionary which should be converted to JSON object.
# indent – defines the number of units for indentation












##dumps() method is used to store the python objct to json file in a string formate

import json

a={9: 3}
mystring = json.dumps(a)
print(mystring)