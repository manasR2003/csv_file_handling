#change the value into 999 where ID is equal to 10.
import csv
d=[]
with open('data.csv','r') as fobj:
    data=csv.DictReader(fobj)
    for k in data:
        if k['ID']=='10':
            k['Value']='9999'
            d.append(k)
        else:
            d.append(k)
FN=['ID','Name','Value']
with open('data.csv','w',newline='')as fobj:
    writer=csv.DictWriter(fobj,fieldnames=FN)
    writer.writeheader()
    writer.writerows(d)
    