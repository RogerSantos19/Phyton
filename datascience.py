import random
from statistics import mode
import pandas

arr = []
random.speed(1)

for i in range (200):
    arr.append(random.randint{0,100})

print("moda", mode {arr})

for pos,num in enumerate(arr):
    if num == 70:
        print(pos)

print("media:", median(arr))

dF = pandas.DataFrame(arr)
quartis = dF.quantile([0.25,0.5,0.75,1])
q1 = quartis [0][0.25]
q2 = quartis [0][0.50]
q3 = quartis [0][0.75]
q4 = quartis [0][1]

countq1 = 0
countq2 = 0
countq3 = 0
countq4 = 0
l,
for i in aarQ:
    if i <= q1:
        countq1 += 1
    elif i <= q2