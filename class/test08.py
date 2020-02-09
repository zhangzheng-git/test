class Car:  #Car叫类对象
    color = "白色"
    name = "宝马"
    def run(self):
        pass

c1 = Car()  #类的实例化 （） c1 是实例化对象
c2 = Car()

print(c1.name)
c1.run()

#类的构造函数
class Person:
    name=""#类变量被所有该类对象共有，一般不用类变量，全部放在初始化函数中的实例变量
    age=0
    sex="男"
    def __init__(self,name,age,sex):#self永远指向的是实例对象
        self.name=name #实例变量属于每一个单独的实例对象
        self.age=age
        self.sex=sex #若实例变量没有该值就使用类变量中的

        name ="zheng" #局部变量，实例变量必须指向self
        print(self.name,self.age,self.sex)

P1=Person("zhang",24,"男")
P2=Person(sex="女",name="zheng",age=18)


