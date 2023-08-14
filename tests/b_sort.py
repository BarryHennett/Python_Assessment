import pandas as pd
import matplotlib.pyplot as plt


def bubblesort(datalist):
    totalnum = len(datalist)
    for i in range(totalnum):
        for j in range(totalnum - 1):
            if datalist[j] > datalist[j + 1]:
                datalist[j], datalist[j + 1] = datalist[j + 1], datalist[j]
    return datalist

df = pd.read_excel("C:/Users/harra/Desktop/Python_Assessment/BirthWeight.xlsx")
datalist = df['BirthWeight'].tolist()

x_val = range(len(datalist))
plt.subplot(1,2,1)
plt.bar(x_val, datalist)
plt.title("Unsorted Plot")

bubblesort(datalist)
plt.subplot(1,2,2)
plt.bar(x_val, datalist, color="green")
plt.title("Bubble Sort Plot")