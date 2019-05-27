import json

class Path:
    def __init__(self,path,file_name):
        self.path = path
        self.file_name = file_name
    def File_name(self,path):
        arrTemp = path.split('/')
        return arrTemp[len(arrTemp)-1]
    def input(self):
        self.path = input()
        self.file_name = self.File_name(self.path)

