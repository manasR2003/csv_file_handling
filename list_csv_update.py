import csv 
l=[]
with open('data1.csv','r') as fobj:
    data=csv.reader(fobj)
    for rows in data:
        if rows[0]=='10':
            rows[2]='100'
        l.append(rows)
with open('data1.csv','w',newline='') as fobj:
    writer=csv.writer(fobj)
    writer.writerows(l)
    print('data updated')