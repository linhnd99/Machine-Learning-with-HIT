import numpy as np 

if __name__ == "__main__":
    a = np.array([1,2,0,0,4,0])
    [print(i) for i in range(len(a)) if a[i]==0]