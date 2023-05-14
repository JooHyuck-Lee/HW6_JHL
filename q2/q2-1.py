#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
import random as rand

def dice(rolls):
    result = [0] * 6
    for i in range(0, rolls):
        k = rand.randrange(0, 6)
        result[k] += 1
      
    return result


def main():
    file = open("q2.csv", 'w')
    file.write("Rolls,")
    for i in range(1, 7):
        file.write(str(i) + ",")
    file.write("\n")
    
    rolls = 100
    result = dice(rolls)
    file.write(str(rolls) + ",")
    for i in result:
        file.write(str(i) + ",")
    file.write("\n")
        
    rolls = 1000
    result = dice(rolls)
    file.write(str(rolls) + ",")
    for i in result:
        file.write(str(i) + ",")
    file.write("\n")    
    
    rolls = 10000
    result = dice(rolls)
    file.write(str(rolls) + ",")
    for i in result:
        file.write(str(i) + ",")    
    file.write("\n")
    
    rolls = 100000
    result = dice(rolls)
    file.write(str(rolls) + ",")
    for i in result:
        file.write(str(i) + ",")    
        
    file.close()
    

    
if __name__ == "__main__":
    main()


# In[ ]:




