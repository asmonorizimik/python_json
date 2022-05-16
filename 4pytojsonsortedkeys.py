import json
d={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
a=[]
b=[]
for i,j in d.items():
    a.append(int(i))
    b.append(j)
x=a.sort()
y=b.sort()
c={}
i=0
while i<len(a):
    c[a[i]]=b[i]
    i+=1

f=open("4pytojsonsortkeys.json","w")
json.dump(c,f,indent=5)
f.close()