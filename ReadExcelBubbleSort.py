import pandas as pd

def bubblesort(BW):
    MTHR = len(BW)
    for i in range(MTHR):
        for j in range(MTHR - 1):
            if BW[j] > BW[j + 1]:
                BW[j], BW[j + 1] = BW[j + 1], BW[j]
    return BW

df = pd.read_excel("C:/Users/harra/Desktop/Python_Assessment/BirthWeight.xlsx")
BW = df['BirthWeight'].tolist()

bubblesort(BW)
print(BW)