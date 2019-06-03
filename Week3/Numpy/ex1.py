import numpy as np

if __name__ == "__main__":
    a = np.array(list(map(int,input().split(" "))))
    print(a)
    a = [-x-1 if x<=8 and x>=3 else x for x in a]
    print(a)

        