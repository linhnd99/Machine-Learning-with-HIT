
if __name__=="__main__":
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    aa = set(a)
    bb = set(b)
    aa.union(bb)
    res = []
    for element in aa:
        res.append(element)
    print(res)