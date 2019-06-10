from ex1 import *

def extract(st,type):
    a = st.strip().split(' ')
    return a[type]

def create3Column():
    laptops["storage_db"] = [extract(e,0) for e in laptops.storage]
    laptops["storage_ssd"] = [True if extract(e,1)=="SSD" else False for e in laptops.storage]
    laptops["storage_hdd"] = [True if extract(e,1)=="HDD" else False for e in laptops.storage]

def countTypeOfStorage():
    print("Storage sdd : %d " % laptops.storage_ssd.sum())
    print("storage hdd : %d " % laptops.storage_hdd.sum())

create3Column()
countTypeOfStorage()