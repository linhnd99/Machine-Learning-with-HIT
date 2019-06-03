import numpy as np

def bs(x, left, right, aa):
    while (left<=right):
        mid = (left+right)//2
        if x == aa[mid] : return mid
        if x<aa[mid] : right=mid-1
        else: left=mid+1
    return -1

if __name__ == "__main__":
    a = np.array(list(map(int,input().strip().split(" "))))
    b = np.array(list(map(int,input().strip().split(" "))))
    b = np.sort(b,axis=0)
    for x in a:
        if bs(x,0,len(a)-1,b) != -1 : print(x,end=" ")
    
