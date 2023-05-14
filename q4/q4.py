#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import matplotlib.pyplot as plt

def sort_two(numlist, namelist):
    for i in range(1, len(numlist)):
        for j in range(i, 0, -1):
            if numlist[j-1] > numlist[j]:
                temp = numlist[j-1]
                numlist[j-1] = numlist[j]
                numlist[j] = temp
                   
                temp = namelist[j-1]
                namelist[j-1] = namelist[j]
                namelist[j] = temp              
                    


                    
def main():
    file = open("q4.csv")
    data = csv.reader(file)
    header1 = next(data)
    header2 = next(data)
    in_all_numlist = []
    in_all_namelist = []
    out_all_numlist = []
    out_all_namelist = []
    user_all_numlist = []
    user_all_namelist = []
    

    for row in data:
        for i in range(-4, 0):
            row[i] = int(row[i])
        if row[3] in in_all_namelist:
            in_all_numlist[in_all_namelist.index(row[3])] += row[-4] + row[-2]
        else:
            in_all_numlist.append(row[-4] + row[-2])
            in_all_namelist.append(row[3])
        if row[3] in out_all_namelist:
            out_all_numlist[out_all_namelist.index(row[3])] += row[-3] + row[-1]
        else:
            out_all_numlist.append(row[-3] + row[-1])
            out_all_namelist.append(row[3])
        if row[3] in user_all_namelist:
            user_all_numlist[user_all_namelist.index(row[3])] += row[-4] + row[-3] + row[-2] + row[-1]
        else:
            user_all_numlist.append(row[-4] + row[-3] + row[-2] + row[-1])
            user_all_namelist.append(row[3])
    
    in_numlist = []
    in_namelist = []
    out_numlist = []
    out_namelist = []
    user_numlist = []
    user_namelist = []
    
    for i in range(0, 30):
        in_namelist.append(in_all_namelist.pop(in_all_numlist.index(max(in_all_numlist))))
        in_numlist.append(in_all_numlist.pop(in_all_numlist.index(max(in_all_numlist))))
        
        out_namelist.append(out_all_namelist.pop(out_all_numlist.index(max(out_all_numlist))))
        out_numlist.append(out_all_numlist.pop(out_all_numlist.index(max(out_all_numlist))))
        
        user_namelist.append(user_all_namelist.pop(user_all_numlist.index(max(user_all_numlist))))
        user_numlist.append(user_all_numlist.pop(user_all_numlist.index(max(user_all_numlist))))
    
                
    sort_two(in_numlist, in_namelist)
    sort_two(out_numlist, out_namelist)               
    sort_two(user_numlist, user_namelist)
    
    print(in_namelist[29] + ":", in_numlist[29])
    print(out_namelist[29] + ":", out_numlist[29])
    print(user_namelist[29] + ":", user_numlist[29])
    
    plt.rc('font', family = "Malgun Gothic")
    plt.rcParams['axes.unicode_minus'] = False
    
    fig, ax= plt.subplots()
    plt.subplots_adjust(bottom=0.4)
    ax.set_title("Seoul Metro: Passengers In (7:00 ~ 9:00)")
    ax.bar(in_namelist, in_numlist)
    ax.set_xlabel("Station Name")
    ax.set_ylabel("Number of Passengers")
    ax.set_xticks(in_namelist)
    ax.set_xticklabels(in_namelist,rotation=90)
    fig.show()
    
    fig, ax= plt.subplots()
    plt.subplots_adjust(bottom=0.4)
    ax.set_title("Seoul Metro: Passengers Out (7:00 ~ 9:00)")
    ax.bar(out_namelist, out_numlist)
    ax.set_xlabel("Station Name")
    ax.set_ylabel("Number of Passengers")
    ax.set_xticks(out_namelist)
    ax.set_xticklabels(out_namelist,rotation=90)
    fig.show()
    
    fig, ax= plt.subplots()
    plt.subplots_adjust(bottom=0.4)
    ax.set_title("Seoul Metro: Total Passengers (7:00 ~ 9:00)")
    ax.bar(user_namelist, user_numlist)
    ax.set_xlabel("Station Name")
    ax.set_ylabel("Number of Passengers")
    ax.set_xticks(user_namelist)
    ax.set_xticklabels(user_namelist,rotation=90)
    fig.show()
    
    file.close()

if __name__ == "__main__":
    main()


# In[ ]:




