# import numpy as np
# a = np.arange(15).reshape(3,5)
# print(a)
# print(a.ndim)#维度 轴
# print(a.shape)
# print(a.size)
#
# a = np.array([1,2,3,4])
# print(a.dtype)
# a = np.array([2.5,3.9])
# print(a.dtype)
#
# a = np.zeros((5,6))
# print(a)
# a = np.ones((2,3,4),dtype=np.float)
# print(a)
#
# a = np.arange(1,9,4)
# print(a)
# a = np.arange(0,5,0.4)
# print(a)
# a = np.linspace(0,10,11)
# print(a)
# a = np.arange(10000).reshape(100,100)
# print(a)
# a= np.array([[1,1],[0,1]])
# b = np.array([[2,0],[3,4]])
# print(a*b)
#
# a = np.zeros((2,3),dtype=np.int)
# print(a)
# a +=3
# print(a)
#
# a = np.random.random((2,3))
# print(a)
#
# print("最大值{}".format(a.max())+"  最小值{}".format(a.min()) +"总和{}".format(a.sum()))
#
# a = np.arange(12).reshape(3,4)
# print(a)
# print(a.sum(axis=0))
#
# a=np.arange(10)**3
# print(a[2])
# print(a)
# a[:6:2]-=100
# print(a)
# a=np.arange(24).reshape(2,3,4)
# print(a)
# print("/////////////////////////////////////////////////////////////////")
# for row in a:
#     print(row)
# print("///////////////////////////////////")
# for row in a.flat:
#     print(row)
#
#
# def f(x):
#     print(id(x))
# print(id(a))
# print(f(a))
#
# b= a
# print(b is a)
#
# b=a.view()
# print(b is a)
# print(int(False))
#
# a = np.arange(12).reshape(3,4)
# print(a)
#
# b = a>4
# print(b)
#
# a[b]=9
# print(a)
#
#
# # import numpy as np
# # import matplotlib.pyplot as plt
# # def mandelbrot( h,w, maxit=20 ):
# #     """Returns an image of the Mandelbrot fractal of size (h,w)."""
# #     y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
# #     c = x+y*1j
# #     z = c
# #     divtime = maxit + np.zeros(z.shape, dtype=int)
# #
# #     for i in range(maxit):
# #         z = z**2 + c
# #         diverge = z*np.conj(z) > 2**2            # who is diverging
# #         div_now = diverge & (divtime==maxit)  # who is diverging now
# #         divtime[div_now] = i                  # note when
# #         z[diverge] = 2                        # avoid diverging too much
# #
# #     return divtime
# # plt.imshow(mandelbrot(400,400))
# # plt.show()
#
# #
# # import numpy as np
# # import matplotlib.pyplot as plt
# # # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
# # mu, sigma = 2, 0.5
# # v = np.random.normal(mu,sigma,100)
# # print(v)
# # # Plot a normalized histogram with 50 bins
# # plt.hist(v, bins=50, density=1)       # matplotlib version (plot)
# # plt.show()
# #
# # (n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
# # plt.plot(.5*(bins[1:]+bins[:-1]), n)
# # plt.show()
#
#
# a  = np.zeros((3,4),dtype=np.float)
# print(a)
# a.astype(np.intc)
# print(a,a.dtype)
# np.int8(a)
# print(a.dtype)
#
# print(np.iinfo(np.intc))
# print(np.finfo(np.float))
#
#
# #numpy arry创建
# # 将Python array_like对象转换为Numpy数组
# a = np.array([[1,2,4,5],(3,5,3,2),[34,4,2,4]])
# print(a)
# #numpy原生数组创建 0填充 dtype默认float64
#
# a = np.zeros((2,3))
# print(a)
# # 1填充
# a = np.ones((2,3))
# print(a)
# #递增
# a = np.arange(2,10)
# print(a)
# #第三个参数 步长
# a = np.arange(2,10,2)
# print(a)
# a = np.arange(2,10,dtype=np.float)
# print(a)
#
# #linspace() 将创建具有指定数量元素的数组，并在指定的开始值和结束值之间平均间隔。
#
# a = np.linspace(2,10,9)
# print(a)
# #indices
# a = np.indices((3,4))
# print(a)
#
# from io import BytesIO
# import os
# #if not os.path.exists(Dire):
# #   os.mkdir("E:/PythonProject/test")
#
# if os.path.isdir("E:/PythonProject/test") !=True:
#     os.mkdir("E:/PythonProject/test")
# with open("E:/PythonProject/test/data.txt","r") as f:
#     #print(f.read())
#     data_list=f.readlines()
#     print(data_list)
# for i in range(len(data_list)):
#     data_list[i]=data_list[i].rstrip('\n')
# print(data_list)
# data =  "1,2,3\n4,5,6"
# a = np.genfromtxt(BytesIO(data.encode("utf-8")),delimiter=',')
# print(a)

import numpy  as np
x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)], dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
print(x.shape ,x.ndim)
print(x)
print(x['age'])