import pandas as pd
import matplotlib.pyplot as plt

def selectsort(datalist):
    totalnum = len(datalist)
    for j in range(totalnum - 1):
        i_min = j
        for i in range(j + 1, totalnum):
            if(datalist[i] < datalist[i_min]):
                i_min = i
        if(i_min != j):
            datalist[j], datalist[i_min] = datalist[i_min], datalist[j]
    return datalist

df = pd.read_excel("C:/Users/harra/Desktop/Python_Assessment/BirthWeight.xlsx")
datalist = df['BirthWeight'].tolist()


x_val = range(len(datalist))
plt.subplot(1,2,1)
plt.bar(x_val, datalist)
plt.title("Unsorted")


selectsort(datalist)
plt.subplot(1,2,2)
plt.bar(x_val, datalist, color="green")
plt.title("Sorted")
