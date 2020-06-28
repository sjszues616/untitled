import time
from multiprocessing.pool import Pool


def desc(f):
    def wrap(*args,**kwargs):
        start_time = time.time()
        fa =f(*args,**kwargs)
        print('用时:',(time.time()-start_time))
        return fa
    return wrap

@desc
def func(a):
    return a*a*a
l1 = []
l2 =[]

if __name__ == '__main__':


    # with Pool(1) as p:
    #     # p.l1.append(1)
    #
    #     print(1)
    with Pool(50) as p:
    #     p.l2.append(1)
        with open('/untitled/threading_learning/test123.txt','a') as f:
            f.write('1')
    #
    # print('l1:',l1,'\n''l2:',l2)