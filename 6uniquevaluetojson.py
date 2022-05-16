import json
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original Python object:\n",python_obj)
json_obj = json.loads(python_obj)
print("\nUnique Key in a JSON object:")
print(json_obj) 
f=open("6unique.json","w")
json.dump(json_obj,f,indent=5)
f.close()



