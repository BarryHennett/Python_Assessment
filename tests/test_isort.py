import pandas as pd
import i_sort
import time

#pytest -s

df = pd.read_excel("C:/Users/harra/Desktop/Python_Assessment/BirthWeight.xlsx")
DL = df["BirthWeight"].tolist()
SDL = sorted(DL)   
 
def test_sorted():
    #sorted == sorted
    start = time.time()
    assert i_sort.insertsort(SDL) == SDL
    end = time.time()
    print("Processing Time: ", round(end - start, 3), "seconds")

def test_unsorted():
    #function(unsorted) == sorted
    start = time.time()
    assert i_sort.insertsort(DL) == SDL
    end = time.time()
    print("Processing Time: ", round(end - start, 3), "seconds")
    
def test_empty():
    nolist = []
    start = time.time()
    assert i_sort.insertsort(nolist) == []
    end = time.time()
    print("Processing Time: ", round(end - start, 3), "seconds")

def test_reversed():
    #a reversed sorted data == sorted
    reverse_list = sorted(DL)
    reverse_list.reverse()
    start = time.time()
    assert i_sort.insertsort(reverse_list) == SDL
    end = time.time()
    print("Processing Time: ", round(end - start, 3), "seconds")

def test_duplicate():
    #duplicate unsorted == duplicate sorted
    duplicate = DL * 2
    start = time.time()
    assert i_sort.insertsort(duplicate) == sorted(duplicate)
    end = time.time()
    print("Processing Time: ", round(end - start, 3), "seconds")
