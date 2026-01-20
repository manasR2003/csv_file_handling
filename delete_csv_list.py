import csv
d=[]
with open('data1.csv','r') as fobj:
    data=csv.reader(fobj)
    for rows in data:
        if rows[0]!='10':
            d.append(rows)
with open('data1.csv','w',newline='') as fobj:
    writer=csv.writer(fobj)
    writer.writerows(d)
    print('deleted okay')