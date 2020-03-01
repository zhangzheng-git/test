import pandas as pd
from pandas import DataFrame

file = pd.read_excel("students.xlsx")
#获取最大行和列
nrows = file.shape[0]
ncols = file.columns.size

print("一共{}行".format(nrows))
print('一共{}列'.format(ncols))

#打印所有列名
print(file.columns)
#打印所有列名和对应索引
for iCol in range(ncols):
    print(str(iCol)+":"+file.columns[iCol])

#获取指定行列的值
print(file.iloc[0,2])#不包含表头行

#显示某一列的值
print("显示某一列的值")
print(file['math'])

#索引 获取某一列的值 索引从0开始
index = file.columns[2]
print("索引 获取某一列的值 索引从0开始")
print(file[index])

#查看某行iRow的值
iRow=1
for i in range(ncols):
    print(file.iloc[iRow,i])
#逐行遍历
for iRow in range(nrows):
    for iCol in range(ncols):
        print(file.iloc[iRow,iCol])

data = file.head(nrows)#读取表头 指定行
# data = file.ix[:]
# print(data)
# data = file.values#不读取表头，所有行
print(data)
FraData=DataFrame(data)
print(data)
print(FraData.shape)

#列
AvrgMath = FraData[['math','Chinese','article','PE']].mean(axis=0)
print(AvrgMath)
#行
AvrgSubject = FraData[['math','Chinese','article','PE']].mean(axis=1)
print(AvrgSubject)

FraData['Max'] = FraData[['math','Chinese','article','PE']].max(axis=1)
print(FraData)