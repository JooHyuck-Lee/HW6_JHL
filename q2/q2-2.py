#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv
import matplotlib.pyplot as plt


def main():
    file = open("q2.csv")
    data = csv.reader(file)
    header = next(data)
    nums = []
    for i in range(1, 7):
        nums.append(i)
    
    for row in data:
        result = []
        k = row[0]
        plt.figure(k)
        plt.title("Dice Simulation: " + str(k) + " Rolls")
        for i in range(1, 7):
            row[i] = int(row[i])
            result.append(row[i])
        plt.bar(nums, result)
        plt.xlabel("Result")
        plt.ylabel("Times Rolled")
    
    plt.show()
    
    file.close()
    
    
if __name__ == "__main__":
    main()


# In[ ]:




