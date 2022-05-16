# import json 
# d={1:"one",2:"two",3:"three",4:"five",5:"five"}
# f=open("2pythontojson.json","w")
# json.dump(d,f,indent=4)
# f.close()



import json
d={"name1":{"name":"manory","lastname":"zimik"},"Q1":{"10th":"savio","12th":"uhss","ba":"pcu"},"place1":{"b":"maku","e":"ukhrul","c":"bangalore"},
   "name2":{"name":"onring","lastname":"awungshi"},"Q2":{"10th":"ktl","12th":"ktl","ba":"modern"},"place2":{"b":"maileng","e":"ukhrul","c":"bangalore"}
  }

f=open("2ptojson.json","w")
json.dump(d,f,indent=5)
f.close()