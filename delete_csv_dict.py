import csv
d=[]
with open('data.csv','r') as fobj:
    data=csv.DictReader(fobj)
    for rows in data:
        if rows['ID']!='10':
            d.append(rows)
with open('data.csv','w',newline='') as foj:
    f=['ID','Name','Value']
    writer=csv.DictWriter(foj,fieldnames=f)
    writer.writeheader()
    writer.writerows(d)
    print('deleted okay')