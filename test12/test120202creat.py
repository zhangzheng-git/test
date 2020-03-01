import numpy as np

print('numpy数组创建的方式')
ZerAry = np.zeros((3,3))
print(ZerAry)
ZerAry = np.zeros((2,3),dtype=np.int32)
print(ZerAry)

EmpAry = np.empty((2,3))
print(EmpAry)

OneAry = np.ones((2,3,4))
print(OneAry)

print('使用arrange生成连续元素的数组')
print(np.arange(12))
print(np.arange(1,12,2)) #可以指定步长

ShapeArry = np.arange(12).reshape(2,3,2) #指定生成数组的维度
print(ShapeArry)

print('运算')
Ary1 = np.array([1,2,3,4,5,6,7])
print(Ary1>2)
print(Ary1[Ary1>2]) #FALSE不取， TRUE相应位置才取

Ary2 = np.array([3,4,2,1,4,1,5])
print(Ary1>Ary2) #对应位置元素做比较