import threading,time

lock = threading.Lock()

def thread_job(dec):
    for i in range(10):
        time.sleep(dec)
        print("这是线程{}".format(threading.current_thread().getName()),i)

def main():
    thread1= threading.Thread(target=thread_job,name="线程一",args=(0.5,))#args 参数是元组类型，当只有一个时要加逗号
    thread2= threading.Thread(target=thread_job,name="线程二",args=(0.8,))#否则默认为int类型

    thread1.start()
    thread2.start()

# if __name__ == '__main__':
#     main()



class myThread(threading.Thread):
    def __init__(self,name,dec):
        threading.Thread.__init__(self)
        self.name=name
        self.dec=dec
    def run(self):
        thread_job(self.dec)

if __name__ == '__main__':
    thread1=myThread("线程一",0.7)
    thread2=myThread("线程二",0.5)

    thread1.start()#先创建再运行 run()
    thread2.start()