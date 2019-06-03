import numpy as np 

if __name__=="__main__":
    a = [[],[],[]]
    for i in range(9):
        a[i//3].append(i)
    res = np.array(a)
    print(res)