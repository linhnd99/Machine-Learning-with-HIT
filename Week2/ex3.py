if __name__ == "__main__" :
    my_dict = {'a':9 , 'b':1 , 'c':12 , 'd':7}
    new_dict = {}
    for element in my_dict:
        new_dict[my_dict[element]] = element 
    for element in sorted(new_dict): 
        print(new_dict[element])