import time 
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import Pool
import os

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'



if __name__ == '__main__':
    
    
    with ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        for result in results:
            print(result)
        

    # with Pool(processes=10) as pool:
    #     results = [pool.apply_async(do_something, args=(1,)) for _ in range(10)]

    #     for f in results:
    #         print(f.get())
        

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')