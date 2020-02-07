# 不换行
# print("你好",end="python")
# print("are you ok")
#类型显示转换
# print(int("4")+4)
# 类型函数type()
# print(type("6"))
# 列表
arry = ["zhagn",1,4.3,True,[1,2,2]]
# 长度函数
print(len(arry))
#列表函数，插入
# arry.insert(2,99)
# arry.append(3)
#列表函数，删除
# del arry[1]
# arry.pop(0)
# print(arry)
#反向打印
# print(arry[0:-2])
#字符串实质 字符序列
# str = "zhanghzrng"
# print(str)
#排序 正向
#list_str  = ["duhei","wnv","wqon","qui","af"]
# list_str.sort()
#排序 反向
# print(sorted(list_str))
# print(list_str)
#集合是无序的
number = (78,90)
print(number)
a = set("abddsd")
b = set("cendjes")
print(a)
print(b)
print(a|b)
list2 = ["32","i",29,392]
print("i" in list2)
print(78 in number)
#if elif
num = 0
if num > 1:
    print(1)
elif num>2:
    print(2)
elif num > 3:
    print(3)
else:
    print(5)

num  = 0
sum =-1
while num<100:
    sum += num
    num +=1
print(sum)

for num in range(10):
    print(num)

list9=["a","b","e","r","t"]
for num in range(len(list9)):
    print(num,end="")

for i in range(6):
    for j in range(i):
        print("*",end="")
    print()
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        # print(j,end="*")
        # print(i,end="=")
        # print(i*j,end=" ")
        print(str(j)+"*"+str(i)+"="+str(i*j),end=" ")
    print()
# 函数
def add(a,b):
    """求和"""
    return (a+b)

print(add(9,8))

def pr(a,b,c):
    for i in range(0,a):
        for j in range(i):
            print(c,end="")
        print()

pr(7,7,"*")
#函数参数,可变参数
def add(*b):
    sum = 0
    for i in b:
        sum += i
    return  sum
print(add(1,2,3,4,6))

#可改变对象与不可改变对象
def printf(b):
    b=9
    print(b)
a=10
printf(a)
print(a)

def printflist(b):
    # b=[1,3,2,4] 只要有等号就产生新对象 里变，外不变
    b.append(3) #里外都变
    print(b)
a=[0,9]
printflist(a)
print(a)

#全局变量  默认只读 函数内要修改加关键字 global
zhang=4
def qure():
    global zhang
    zhang=5
    print(zhang)
qure()
print(zhang)

sum = lambda a,b:a+b
print(sum(1,2))
