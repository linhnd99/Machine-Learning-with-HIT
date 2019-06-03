import numpy as np 

if __name__ == "__main__":
    a = np.array(np.random.randint(0,10000,30))
    print(a)
    s=a.sum()
    print(s/len(a))
