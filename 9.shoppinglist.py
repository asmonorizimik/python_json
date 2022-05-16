# import json
# dict={
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }

# f=open("9shoping.json","w")
# json.dump(dict,f,indent=5)
# f.close()



import json 
user=input("items u want to buy:")
num=int(input("enter how nany grocereis you want to buy:"))
i=1
dict={}
dict1={}
while i<=num:
    product=input("enter name:")
    prize=int(input("enter the prize"))
    dict1[product]=prize
    i+=1
dict[user]=dict1
print(dict)
f=open("9shoping.json","w")
json.dump(dict,f,indent=5)
f.close()