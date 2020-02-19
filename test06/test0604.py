import threading

def threadjob1():
    for i in range(10):
        print("job1", i)
        if i==5:
            thread2=threading.Thread(target=threadjob2,name="job2")
            thread2.start()
            thread2.join()


def threadjob2():
    for i in range(10,20):
        print("job2**********************",i)

if __name__ == '__main__':
    thread = threading.Thread(target=threadjob1,name="job1")
    thread.start()