from ex1 import *

def Resolution(sc):
    sc = sc.strip()
    return sc.split(" ")[-1]

def laptopFullHD():
    laptops["resolution"] = [Resolution(sc) for sc in laptops.screen]
    fullHDScreen = [laptops for e in laptops.resolution if e == "1920x1080"]
    print("Laptop Full HD: %d screens" % len(fullHDScreen))        

def popularScreenResolution():
    temp = laptops.resolution.value_counts()
    print("Popular screen resolution: %s" % temp.keys()[0])

# main
laptopFullHD()
popularScreenResolution()

