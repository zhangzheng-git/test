if __name__== '__main__':
    print(__name__)
    while(True):
        num1=input("请输入第一个数：")
        opr=input("请输入运算符：")
        num2=input("请输入第二个数：")
        while(True):
            if opr=="+":
                print("和为：",int(num1)+int(num2))
                break
            if opr=="-":
                print("差为：",int(num1)-int(num2))
                break
            else:
                print("运算符有误，请重新输入运算符：",end="")
                opr = input()
                continue
        print("是否继续运算，[y/n]")
        flage = input()
        if flage == 'y':
            continue
        else:
            print("程序结束")
            break