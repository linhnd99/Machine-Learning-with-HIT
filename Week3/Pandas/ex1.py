import pandas as pd 
import numpy as np

laptops = pd.read_csv("/Users/linhnd/Downloads/week4_pandas/laptops.csv", encoding="latin-1")

def cleanName(name):
    name = name.strip()
    name = name.lower()
    s = name.split('(')
    s = s[0].strip()
    s = s.replace(" ","_")
    return s

def convertRAM(ram):
    return int(ram[:len(ram)-2])
def convertWeight(weight):
    weight = weight.replace("kgs","kg").replace("kg","")
    return float(weight.replace("kg",""))
def convertPrice(price):
    price = price.strip().replace(",",".")
    return float(price[:len(price)-2])
def CPUspeedFromCPU(cpu):
    cpu = cpu.split(' ')[-1]
    return cpu

def function1():
    laptops.columns = [cleanName(col) for col in laptops.columns]
    laptops.model_name = [cleanName(name) for name in laptops.model_name]

def function2():
    laptops["ram_num"] = [convertRAM(numRam) for numRam in laptops["ram"]]
    laptops["weight_num"] = [convertWeight(numWeight) for numWeight in laptops["weight"]]
    laptops["price_num"] = [convertPrice(numPrice) for numPrice in laptops["price"]]

def function3():
    laptops["cpu_speed"] = [CPUspeedFromCPU(csp) for csp in laptops["cpu"]]

def function4():
    # arr = laptops.operating_system
    # arr = ["Mac OS" if element == "macOS" else element for element in arr ]
    # laptops.operating_system = arr
    Map = {
        "Windows":"Windows",
        "No OS":"No OS",
        "Linux":"Linux",
        "Chrome OS":"Chrome OS",
        "macOS":"Mac OS",
        "Mac OS":"Mac OS",
        "Android":"Android"
    }
    laptops.operating_system = laptops.operating_system.map(Map)


def function5():
    laptops
    laptops.loc[laptops.operating_system.isnull(), "operating_system"] = "No OS"

# main
function1()
function2()
function3()
function4()
function5()
    