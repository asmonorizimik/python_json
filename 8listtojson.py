import json
filename = '8.txt'
dict1 = {}
fields =['name', 'designation', 'age', 'salary']
with open(filename) as fh:
    l = 1
    for line in fh:
        d = list( line.strip().split(None, 4))
        print(d) 
        sno ='employee'+str(l)
        i = 0
        dict2 = {}
        while i<len(fields):
                dict2[fields[i]]= d[i]
                i = i + 1
        dict1[sno]= dict2
        l = l + 1      
out_file = open("8.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()