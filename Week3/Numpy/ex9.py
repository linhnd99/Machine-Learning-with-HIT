import numpy as np 

if __name__ == "__main__":
    a = np.array(np.zeros((3,3)))
    row = np.ones(5).reshape(1,5)
    col = np.ones(3).reshape(1,3)
    a=np.insert(a,len(a[0]),col,axis=1)
    a=np.insert(a,0,col,axis=1)
    a=np.insert(a,0,row,axis=0)
    a=np.insert(a,len(a),row,axis=0)
    print(a)
    

