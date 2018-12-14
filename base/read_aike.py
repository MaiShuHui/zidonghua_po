import yaml
import os
class ReadAike():

    def __init__(self,filename):
        self.filename = os.getcwd()+os.sep+"data"+os.sep+filename

    def read_aike(self):
        with open(self.filename,"r",encoding="utf-8") as f:
            return yaml.load(f)

    def read_aike_01(self):
        with open("../data/data_aike.yaml","r",encoding="utf-8") as f:
            print(yaml.load(f))


if __name__ == '__main__':
    ReadAike("data_aike.yaml").read_aike_01()