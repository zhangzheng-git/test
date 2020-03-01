import numpy as  np
a = np.arange(7)
print(a,a.dtype,a.ndim,a.shape)

a = np.array(np.arange(7))
print(a,a.dtype,a.ndim,a.shape,len(a.shape))

a = np.array([1,2,3,4])
print(a.shape)

#数组的创建zero ones empty
a = np.ones((2,3))
print(a)
a = np.zeros((2,3))
print(a)
a= np.empty((2,3))
print(a)

#数组的类型转换
a = np.array(np.array(9),dtype=np.float64)
print(a.dtype)
b = a.astype(dtype=np.int32)
print(b.dtype)

y = np.array(np.arange(9),dtype=np.float32)
y = y.astype(a.dtype)
print(y.dtype)

#数组与标量、数组的运算

a = np.array([1,2,3])
print(a>2)
b = np.array([4,5,6])
print(a*b)
print(a@b)
print(a+b)
print(2*a)
