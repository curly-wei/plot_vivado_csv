import csv

with open('c7.csv', newline='') as f:
  reader = csv.reader(f)
  data = list(reader)

iter_start = 0;
while(data[iter_start][0] != 'Scan Start'):
  iter_start+=1

iter_end = 0;
while(data[iter_end][0] != 'Scan End'):
  iter_end+=1

vals = []
for i in range(iter_start+1,iter_end):
  vals.append(data[i])
vals[0].pop(0)

for i in vals:
  for j in i:
    j = float(j)


print(vals)       
