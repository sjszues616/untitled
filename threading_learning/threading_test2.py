import threading
import time


def sing():
    while True:
        time.sleep(2)
        print(time.ctime(),'sing song!')


def dance():
    while True:
        time.sleep(3)
        print(time.ctime(),'dancing!')


if __name__ == '__main__':
    threading1 = threading.Thread(target=sing,name='sing1')
    threading2 = threading.Thread(target=dance,name='dance1')
    threading1.start()
    threading2.start()

    time.sleep(10)
    print('main thread is over')