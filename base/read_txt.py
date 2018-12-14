import os
import yaml
class ReadTxt():

    def __init__(self,filename):
        self.filename = os.getcwd()+os.sep+"data"+os.sep+filename

    def read_txt(self):
        with open(self.filename,"r",encoding="utf-8")as f :
            list = []
            for a in f:
                list.append(tuple(a.split()))
        return list

    def read_txt_01(self):
        with open("..\data\data.txt","r",encoding="utf-8")as f :

            print(yaml.load(f))


if __name__ == '__main__':
    ReadTxt("..\data\data.txt").read_txt_01()