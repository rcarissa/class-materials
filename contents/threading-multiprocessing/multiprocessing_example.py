import time
import multiprocessing


def is_prime(n):
      if (n <= 1) : 
          return 'not a prime'
      if (n <= 3) : 
          return 'prime'
          
      if (n % 2 == 0 or n % 3 == 0) : 
          return 'not a prime'
    
      i = 5
      while(i * i <= n) : 
          if (n % i == 0 or n % (i + 2) == 0) : 
              return 'not a prime'
          i = i + 6
    
      return 'prime'


def multiprocessing_func(x):
    time.sleep(2)
    print('{} is {} number'.format(x, is_prime(x)))

   
if __name__ == '__main__':

    print('Started')

    # single processing example
    print('Starting... - single-processing')
    starttime = time.time()
    for i in range(1, 10):
        time.sleep(2)
        print('{} is {} number'.format(i, is_prime(i)))
    print()    
    print('Time taken = {} seconds'.format(time.time() - starttime))

    # multiprocessing example (With Process)
    print('Starting... - multi-processing')
    starttime = time.time()
    processes = []
    for i in range(1,10):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
        
    print()    
    print('Time taken = {} seconds'.format(time.time() - starttime))

    # multiprocessing example (with Pool)
    starttime = time.time()
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_func, range(1,10))
    pool.close()
    print()
    print('Time taken = {} seconds'.format(time.time() - starttime))

    print('Ended')