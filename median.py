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
newdata.sort()
if n%2==0:
    m1=float(newdata[n//2])
    m2=float(newdata[n//2-1])
    median=(m1+m2)/2
else:
    median=newdata[n//2]
print(median)       