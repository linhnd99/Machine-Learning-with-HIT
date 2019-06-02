if __name__ == "__main__":
    a = [[1,4],[9,16],[25,36]]
    b = []
    print(type(a))
    for x in a:
        for y in x: 
            b.append(y)
    print(b)