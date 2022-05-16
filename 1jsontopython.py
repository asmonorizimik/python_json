import json
f=open("data.json","r")
x=json.load(f)
print(x)
f.close()