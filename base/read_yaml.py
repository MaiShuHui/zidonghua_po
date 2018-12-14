import yaml
import os

class ReadYaml():

    def __init__(self,filename):
         self.filename = os.getcwd() + os.sep + "data" + os.sep + filename

    def read_yaml(self):
        with open(self.filename,"r",encoding='utf-8') as f:
            return yaml.load(f)

# def get_data():
#     datas = ReadYaml("data_login.yaml").read_yaml()
#     run = []
#     for data in datas.values():
#         run.append((data.get("number"), data.get("password")))
#     return run

    def read_yaml_01(self):

        with open("../data/data_login.yaml","r",encoding='utf-8') as f:

            print(yaml.load(f))



if __name__ == '__main__':
    ReadYaml("../data/data_login.yaml").read_yaml_01()