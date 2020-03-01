import pandas as pds
from pandas import DataFrame

data = {'a':[1,2,1,2],
        'b':[4,5,6,7],
        'c':[7,8,5,7]}
Fra_data = DataFrame(data)
print(Fra_data)

# print(Fra_data['a'])

#print(Fra_data.loc[0])

#计算每一行的平均值
print(Fra_data[['a','b','c']].mean(axis=1))

#计算每一列的平均值
print(Fra_data[['a','b','c']].mean(axis=0))



