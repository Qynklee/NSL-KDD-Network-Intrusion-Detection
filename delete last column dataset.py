arr = "0,tcp,ftp_data,SF,491,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0.00,0.00,0.00,0.00,1.00,0.00,0.00,150,25,0.17,0.03,0.17,0.00,0.00,0.00,0.05,0.00,normal,20"

arr2 = arr.split(",")

print(len(arr2))

filename = "Dataset.csv"
outname = "Dataset1.csv"
import csv
from turtle import end_fill

with open(filename, 'r') as i, open(outname, 'w', newline= "") as o:
    cr = csv.reader(i)
    cw = csv.writer(o)
    for row in cr:
        cw.writerow(row[0:42])