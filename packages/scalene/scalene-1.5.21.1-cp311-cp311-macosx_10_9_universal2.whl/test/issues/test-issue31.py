#!/usr/bin/env python3.10
import numpy as np
import time

def main1():
    # Before optimization
    # x = np.array(range(10**8))
    time.sleep(10)
    np.random.uniform(0, 100, size=10**8)

def main2():
    # After optimization, spurious `np.array` removed.
    # x = np.array(range(10**5))
    time.sleep(5)
    np.random.uniform(0, 100, size=10**7)

main1()
main2()
main1()



