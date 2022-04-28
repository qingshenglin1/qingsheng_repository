import csv

def read_excel(file):
    data_list=[]
    with open(file,'r',encoding='utf-8') as f:
        data=csv.reader(f)
        for i in data:
            data_list.append(i)
    return data_list

