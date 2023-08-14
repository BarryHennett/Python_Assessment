import pandas as pd

def insertsort(BW):
    MTHR = len(BW)
    for i in range(MTHR):
        j = i
        while j > 0 and BW[j - 1] > BW[j]:
            BW[j], BW[j - 1] = BW[j - 1], BW[j]
            j = j - 1
    return BW

df = pd.read_excel("C:/Users/harra/Desktop/Python_Assessment/BirthWeight.xlsx")
BW = df['BirthWeight'].tolist()

insertsort(BW)
print(BW)