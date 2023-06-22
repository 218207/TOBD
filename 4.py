import math
import time
import multiprocessing
# %%time
def find_pairs(start, end):
    result = []
    for x in range(start, end):
        for y in range(x, 3001):
            if math.sin(x * y) > 0.9999999:
                result.append((x, y, math.sin(x * y)))
    return result

if __name__ == '__main__':
    start_time = time.time()
    pool = multiprocessing.Pool(processes=4)
    result = pool.starmap(find_pairs, [(1, 751), (751, 1501), (1501, 2251), (2251, 3001)])
    pool.close()
    pool.join()
    results = [item for sublist in result for item in sublist]
    print("Время выполнения программы: {:.2f} секунд".format(time.time() - start_time))
    print(results)