import threading

ThrdLock=threading.Lock()
ticket=100

def sell_ticket():
    global ticket
    global ThrdLock
    while True:
        ThrdLock.acquire()
        if ticket>0:
            ticket -= 1
            print(threading.current_thread().getName()+"卖出的票号："+str(ticket+1))
            ThrdLock.release()
            continue
        else:
            print("已售完")
            break
        ThrdLock.release()

if __name__ == '__main__':
    for i in range(3):
        thread = threading.Thread(target=sell_ticket,name="窗口{}".format(i))
        thread.start()