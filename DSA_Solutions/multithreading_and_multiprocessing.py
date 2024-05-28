import time
import threading
import multiprocessing


def calc_square(numbers):
    if numbers:
        for n in numbers:
            time.sleep(0.2)
            print('square:', n*n)


def calc_cube(numbers):
    if numbers:
        for n in numbers:
            time.sleep(0.2)
            print('cube:', n*n*n)


if __name__ == '__main__':
    arr = [2,3,4,5,6,9]
    t = time.time()
    # print('Starting calculation of number cube:')
    # calc_cube(arr)
    # print('Starting calculation of number square:')
    # calc_square(arr)
    # print('It took', time.time()-t, 'seconds to run the program')
    # When we run the program this way, that is with the delay we have time of 2.4 secs, to improve this time
    # we can apply multithreading(multitasking) so while the cpu is resting we can use the time to process
    # another function. With threading, it took half the time, 1.2secs
    thread1 = threading.Thread(target= calc_square, args= (arr,))
    thread2 = threading.Thread(target= calc_cube, args= (arr,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # If we want to implement multiprocessing instead, the syntax is very similar and is shown below
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()
    p1.join()
    # when we make use of multiprocessing, it executes one process completely before commencing the next

    print('It took', time.time()-t, 'seconds to run the program')
