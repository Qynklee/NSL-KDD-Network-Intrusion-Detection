import pandas as pd
import numpy as np
import csv

df = pd.read_csv('Dataset.csv')
df['split'] = np.random.randn(df.shape[0], 1)

msk = np.random.rand(len(df)) <= 0.7

train = df[msk]
test = df[~msk]

train.to_csv('train.csv', index = False)
test.to_csv('test.csv', index = False)

with open("train.csv", 'r') as i, open("train2.csv", 'w', newline= "") as o:
    cr = csv.reader(i)
    cw = csv.writer(o)
    for row in cr:
        cw.writerow(row[0:42])

with open("test.csv", 'r') as i, open("test2.csv", 'w', newline= "") as o:
    cr = csv.reader(i)
    cw = csv.writer(o)
    for row in cr:
        cw.writerow(row[0:42])