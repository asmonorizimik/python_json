import json
filename = '7txttojson.txt'
dict1 = {}
with open(filename) as f:
  
    for line in f:
        c, d= line.strip().split(None, 1)###c=>keys,##d=>values
        dict1[c] = d
out_file = open("7txttojson.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()




# import json
# def convert() :
#     f = open('7json.txt', "r")
#     content = f.read()
#     splitcontent = content.splitlines()

#     for line in splitcontent :
#         pipesplit = line.split(' | ')
#         print(pipesplit)
#     with open("7json_log.json", 'w') as file:
#         json.dump(pipesplit, file, indent=4)
        
# convert()





# import json
# filename = '7data.txt'
# dict1 = {}
# with open(filename) as fh:      
  
#     for line in fh:
#         c, d= line.strip().split(None, 1)
  
#         dict1[c] = d.strip()
# out_file = open("7data.json", "w")
# json.dump(dict1, out_file, indent = 4, sort_keys = False)
# out_file.close()






  
# import json
# filename = '7.txt'
# dict1 = {}
# fields =['name', 'designation', 'age', 'salary']
# with open(filename) as fh:
#     l = 1
#     for line in fh:
#         d = list( line.strip().split(None, 4))
#         # print(description) 
#         sno ='emp'+str(l)
#         i = 0
#         dict2 = {}
#         while i<len(d):
#                 dict2[fields[i]]= d[i]
#                 i = i + 1
#         dict1[sno]= dict2
#         l = l + 1     
# out_file = open("7.json", "w")
# json.dump(dict1, out_file, indent = 4)
# out_file.close()





# a = ' \n   1 2 3 4     \n\n 5 \n\n \t'
# b = a.strip().split()
# c = a.split()
# print('b =',b)
# print('c =',c)