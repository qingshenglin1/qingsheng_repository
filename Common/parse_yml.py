import yaml

def read_yaml(file,section,key):
    with open(file,'r',encoding="utf-8") as f:
        data=yaml.load(f,Loader=yaml.FullLoader)
        return data[section][key]


if __name__=="__main__":
    print(read_yaml(r"../Config/redmine.yml","websites","host"))

