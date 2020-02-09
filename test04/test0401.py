class Anmail:
    def __init__(self,color,weghit):
        self.color=color
        self.weghit=weghit
    def eat(self):
        print("eat")

class Dog(Anmail):
    def wacth_door(self):
        print("watch door")

dog = Dog("wait",23)
dog.eat()
print(dog.color,dog.weghit)

class A:
    a=1
    b=2
class B:
    a=3
    b=4
class C(A,B):
    b=5
    c=6

print(C.a,C.b,C.c) #1,2,6

#私有变量
class Nmu:
    a=1
    b=2
    __c=3  #私有变量只能在本类中使用，本类的实例也不能直接访问

    def __pr(self):
        print(self.a,self.b,self.__c)
    def fun(self):
        self.__pr()
    def get_c(self):
        return self.__c
    def set_c(self,num):
        if num>self.__c:
            print("内存已满")
        else:
            self.__c -=num
            print("内存剩余：",self.__c)


nmu=Nmu()
#print(nmu.__c)  报错，本类实例不能直接使用，只能通过接口访问
nmu.fun()
print(nmu.get_c())
nmu.set_c(3)


class Parent:
    def fun(self):
        print("父类方法")

class Child(Parent):
    def fun(self):
        print("子类方法")

child = Child()
child.fun()
#参数 （类，实例）
super(Child,child).fun()

#运算符重载

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        print("name:"+self.name+"    age:"+str(self.age))

person=Person("zhzng",12)
print(person)#不重载str的话打印的是内存地址

