import json
x = '{"Name": "Jennifer Smith","Contact Number": 7867567898,"Email": "jen123@gmail.com","Hobbies":["Reading", "Sketching", "Horse Riding"]}'
# x = """{
#     "Name": "Jennifer Smith",
#     "Contact Number": 7867567898,
#     "Email": "jen123@gmail.com",
#     "Hobbies":["Reading", "Sketching", "Horse Riding"]
#     }"""

y = json.loads(x)
print(y)
            


