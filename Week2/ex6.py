s = input()
w = int(input())
res = ""
for i in range(len(s)):
    res=res+s[i]
    if ((i+1)%w==0):
        res=res+"\n"
print(res)