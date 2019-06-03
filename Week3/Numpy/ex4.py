import numpy as np 

if __name__ == "__main__":
    a = np.array(list(map(int,input().strip().split(" "))))
    a = np.flip(a,axis=0)
    print(a)
    
