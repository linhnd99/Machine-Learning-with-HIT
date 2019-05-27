import json

fi = open("path.txt","r")
fo = open("path.json","w")
a=[]
dic={}

inp = fi.readlines()
for line in inp :
    name = line.split('/')
    dic["path"] = line
    dic["file_name"] = name[len(name)-1]
    a.append(dic)
json.dump(a,fo)
fi.close()
fo.close()