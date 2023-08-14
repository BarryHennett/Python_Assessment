import pandas as pd

def selectsort(BW):
    MTHR = len(BW)
    for j in range(MTHR - 1):
        i_min = j
        for i in range(j + 1, MTHR):
            if(BW[i] < BW[i_min]):
                i_min = i
        if(i_min != j):
            BW[j], BW[i_min] = BW[i_min], BW[j]
    return BW

df = pd.read_excel("C:/Users/harra/Desktop/Python_Assessment/BirthWeight.xlsx")
BW = df['BirthWeight'].tolist()

selectsort(BW)
print(BW)