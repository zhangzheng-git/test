import numpy as np
DataArray = np.array([1,2,3])
print(DataArray)
print(DataArray[0])#1 获取元素
print(DataArray[1:])#[2]切片不影响类型
print('花式索引',DataArray[[1,2]])


print('================2d============================')
DataArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(DataArray)
DataPart = DataArray[0][2]
DataPart1 = DataArray[0,2] #上面两个是等价的
print('[0][2]=',DataPart,'[0,2]=',DataPart1)
Section  = DataArray[:2]
Section1 = DataArray[:2,2]#逗号表示分别作用于前面切片结果的每一个元素  不等价[:2][2]
Section2 = DataArray[:2,:2]#也可以连续切片
Section3 = DataArray[:2][0]#先切片在对切片结果整体取[0]
print('[:2]=',Section,"\n[:2,2]",Section1)
print(Section2)
nRow = DataArray.shape[0] #可以获取多少行
nCol = DataArray.shape[1] #可以获取多少列
print('行',nRow,'列',nCol)

#花式索引 数组做索引 形式x[[1,2,3]] 不论x是一维二维三维
FlIndex = DataArray[[1,2]] #主要是一次获取多个元素 与切片的功能相似
Section4 = DataArray[1:]
print('花式索引', FlIndex)
print('切片',Section4)
#布尔索引 索引要与原数组维度个数元素个数一致
BoolArry = np.array([[True,False,True],[True,True,False],[False,False,False]])
print('布尔索引',DataArray[BoolArry]) #最后成了一维数组

print('==========================3d=============================')
ThrArray = np.array([[[1,2,3],[3,2,1]],[[4,5,6],[6,5,4]]])
print(ThrArray,ThrArray.shape)
ThrArrayIndex = ThrArray[0]
print(ThrArrayIndex)
ThrArrayIndex = ThrArray[1][1][1]
print(ThrArrayIndex)
ThrArrayIndex = ThrArray[1,1,1]  #与[1][1][1]等价的 可以得出只用作索引[]里面的，与[]是等价的
print(ThrArrayIndex)

Section5 = ThrArray[:2]
print('切片',Section5)
Section5 = ThrArray[:2,1]
Section5 = ThrArray[:2,1,1]

FlIndex = ThrArray[[0,1],[0,1]]
print('花式索引',FlIndex)#数组做索引 形式x[[1,2,3]] 不论x是一维二维三维

FlIndex = ThrArray[[[0,1]],[[0,1]]]#与上面的结果完全一致
print('花式二',FlIndex)

#布尔索引
BAry = np.array([[[True,False,True],[True,False,True]],[[True,False,True],[True,False,True]]])
print(ThrArray[BAry])

import numpy as np

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[[[0, 0], [3, 3]], [[0, 2], [0, 2]]]
y = x[rows,cols]#行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]。
print('这个数组的四个角元素是：')
print(y)
