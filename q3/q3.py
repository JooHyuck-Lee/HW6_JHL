#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
import matplotlib.pyplot as plt


                    
def main():
    year = []
    male = []
    female = []
    
    f1 = open("q3-1.csv")
    text = csv.reader(f1)
    header = next(text)
    data = next(text)
    k = 2008
    for i in range(0, len(data)):
        if i % 6 == 4:
            data[i] = int(data[i])
            male.append(data[i])
            year.append(k)
            k += 1
        if i % 6 == 5:
            data[i] = int(data[i])
            female.append(data[i])
            
    f2 = open("q3-2.csv")
    text = csv.reader(f2)
    header = next(text)
    data = next(text)
    for i in range(0, len(data)):
        if i % 6 == 4:
            data[i] = int(data[i])
            male.append(data[i])
            year.append(k)
            k += 1
        if i % 6 == 5:
            data[i] = int(data[i])
            female.append(data[i])
    
#     print(year)
#     print(male)
#     print(female)
    
    ratio = []
    for i in range(0, len(year)):
        ratio.append(male[i] / female[i])
        
#     print(ratio)
    
    plt.title("Male vs. Female Population in Jeju")
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.plot(year, male, "gray", label = "Male", marker = "o")
    plt.plot(year, female, "darkred", label = "Female", marker = "^")
    plt.xticks(year, rotation=60)
    plt.legend()
    plt.show()
    
    f1.close()
    f2.close()

    
    
    

if __name__ == "__main__":
    main()


# In[ ]:




