import time
import numpy as np


def main():
    a = np.random.random(200000000)
    b = np.random.random(200000000)
    tick = time.time()
    c = np.dot(a, b)
    tock = time.time()
    print("Time taken: {} ms".format(1000 * (tock - tick)))
    a = np.random.randn(3, 3)  # a.shape=(3,3)a.shape=(3,3)
    b = np.random.randn(2, 1)
    b = np.random.randn(2, 1)  # b.shape=(2,1)b.shape=(2,1)

    c = a + b
    print(c)

if __name__ == "__main__":
    main()
