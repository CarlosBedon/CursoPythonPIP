import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        cabecera = next(reader)
        data=[]
        for row in reader:
            iterable = zip(cabecera,row)
            CSV_dict = { key:value for key, value in iterable}
            data.append(CSV_dict)
    return data

if __name__ == '__main__':
    read_csv('./data.csv')