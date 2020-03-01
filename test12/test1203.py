import numpy as np

a= np.array([[[1,3,4],[2,9,2],[3,3,4]],[[9,8,7],[99,66,77],[4,3,2]]])
print(a,a.shape,a.ndim)
print(a[0,1,1])

a= np.array([[[1]]])
print(a,a.shape,a.ndim)


#布尔型索引
print('布尔型索引')
a = np.array([2,3,4,5,5])
b = np.array([True,False,True,False,True])
print(a[b])#True取 False不取
print(a[b==False])
print(a>6)
print((a==3)|(a==5))
print(a[(a==3)|(a==5)])