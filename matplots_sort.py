import pandas as pd
import matplotlib.pyplot as plt

def selection_sort(datalist):
    totalnum = len(datalist)
    for j in range(totalnum - 1):
        i_min = j
        for i in range(j + 1, totalnum):
            if(datalist[i] < datalist[i_min]):
                i_min = i
        if(i_min != j):
            datalist[j], datalist[i_min] = datalist[i_min], datalist[j]
    return datalist

dataframe = pd.read_excel("C:/Users/harra/Desktop/Python_Assessment/BirthWeight.xlsx")
datalist = dataframe['BirthWeight'].tolist()

x_axis = range(len(datalist))
plt.subplot(1,2,1)
plt.bar(x_axis, datalist)
plt.title("Unsorted Plot")

selection_sort(datalist)
plt.subplot(1,2,2)
plt.bar(x_axis, datalist, color="red")
plt.title("Selection Sort")
print(datalist)

plt.show()