import numpy as np 

a=np.random.randn(10)
m=a.max()
for i in range(10):
    if a[i]==m: a[i]=0
print(a)