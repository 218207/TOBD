from collections import Counter
import multiprocessing as mp


def count_letters(file):
    with open(file, encoding="windows-1251") as fp:
        text = fp.read().lower()
        return Counter(text)

if __name__ == '__main__':
    files = ["Dostoevskiy Fedor. Igrok - BooksCafe.Net.txt"]
    with mp.Pool(processes=len(files)) as pool:
        counters = pool.map(count_letters, files)
    print(counters)