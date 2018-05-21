import threading
localobj=threading.local()

def threadfunc(name):
    localobj.name=name
    print "localonj.name is %s"%name

if __name__=='__main__':
    t1=threading.Thread(target=threadfunc,args=("Hyde",))
    t2=threading.Thread(target=threadfunc,args=("Jekyll",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()