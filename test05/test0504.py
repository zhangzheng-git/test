
print(__name__)
import os,shutil

if __name__=='__main__':
    path ="E:/PythonProject/test/test05/1.log"
    Dire, fname = os.path.split(path) #fname 无用返回值可以用 _ 代替
    print(Dire)
    if not os.path.exists(Dire):
        os.makedirs(Dire)
    fp=open(path,"w")
    fp.write("hello word ")
    fp.close()
    # src_file = 'D:\\etc\\test\\1.log'
    # dst_file = 'D:\\etc\\1.log'
    shutil.copyfile("E:/PythonProject/test/test05/1.log","E:/PythonProject/test/1.log")#复制加重命名

