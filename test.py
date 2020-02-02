# print("你好",end="python")
# print("are you ok")
# print(int("4")+4)
# print(type("6"))

arry = ["zhagn",1,4.3,True,[1,2,2]]
print(len(arry))

# arry.insert(2,99)
# arry.append(3)
# del arry[1]
# arry.pop(0)
# print(arry)
# print(arry[0:-2])
# str = "zhanghzrng"
# print(str)
list_str  = ["duhei","wnv","wqon","qui","af"]
# list_str.sort()

print(sorted(list_str))
print(list_str)

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


age = 909
if age == 99:
    print("A")
print("B")



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

for num in range(101):
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
#循环