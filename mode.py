import csv
from  collections import Counter
with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    data=list(reader)
data.pop(0)
newdata=[]
for i in range(len(data)):
    numb=data[i][2]
    newdata.append(float(numb))
data1=Counter(newdata)
mode_data_for_range={"100-110":0,"110-120":0,"120-130":0,"130-140":0,"140-150":0,"150-160":0}
for height,occurance in data1.items():
    if 100<float(height)<110:
        mode_data_for_range["100-110"]+=occurance
    elif 110<float(height)<120:
        mode_data_for_range["110-120"]+=occurance 
    elif 120<float(height)<130:
        mode_data_for_range["120-130"]+=occurance   
    elif 130<float(height)<140:
        mode_data_for_range["130-140"]+=occurance
    elif 140<float(height)<150:
        mode_data_for_range["140-150"]+=occurance 
    elif 150<float(height)<160:
        mode_data_for_range["150-160"]+=occurance   
mode_range,mode_occurance=0,0
for range,occurance in mode_data_for_range.items():
    if occurance>mode_occurance:
        mode_range,mode_occurance=[int(range.split("-")[0]),int(range.split("-")[1])],occurance
mode=float((mode_range[0]+mode_range[1])/2)
print(mode)           
