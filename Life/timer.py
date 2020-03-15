import time
import threading

def heart_beat(start):
    elapsed = time.time() - start
    e = time.strftime("%H:%M:%S", time.gmtime(elapsed))
    f = open("time.txt", "w+")
    f.write(str(e))
    f.close()
    
def main():
    s = time.time()
    while(True):
        time.sleep(1)
        heart_beat(s)

if __name__ == "__main__":
    main()



