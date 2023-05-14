#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
import matplotlib.pyplot as plt
import numpy as np

def getTemp(data):
    tempList = []
    for i in range(0, 8):
        useless = next(data)

    for row in data:
        row[2] = float(row[2])
        tempList.append(row[2])
    
    return tempList

def main():
    f1 = open("temp_korea.csv")
    f2 = open("temp_seoul.csv")
    f3 = open("temp_busan.csv")
    f4 = open("temp_daejeon.csv")
    f5 = open("temp_jaeju.csv")
    data = csv.reader(f1)
    korea = getTemp(data)
    
    data = csv.reader(f2)
    seoul = getTemp(data)
    
    data = csv.reader(f3)
    busan = getTemp(data)
    
    data = csv.reader(f4)
    daejeon = getTemp(data)
    
    data = csv.reader(f5)
    jaeju = getTemp(data)
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    plt.title("Temperature in Regions of Korea in 2022")
    plt.xlabel("Months")
    plt.ylabel("Tempterature (ºC)")
    plt.plot(months, korea, label = "Korea", marker = "o")
    plt.plot(months, seoul, label = "Seoul", marker = "*")
    plt.plot(months, busan, label = "Busan", marker = "^")
    plt.plot(months, daejeon, label = "Daejeon", marker = "x")
    plt.plot(months, jaeju, label = "Jaeju", marker = "D")
    plt.xticks(months)
    plt.legend()
    plt.show()
    
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    
    
if __name__ == "__main__":
    main()


# In[ ]:




