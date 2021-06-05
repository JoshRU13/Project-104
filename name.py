import csv
with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    data=list(reader)
data.pop(0)
newdata=[]
for i in range(len(data)):
    numb=data[i][2]
    newdata.append(float(numb))
n=len(newdata)
total=0
for x in newdata:
    total+=x
mean=total/n
print(mean)        
