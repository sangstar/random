#!/usr/bin/env python
# coding: utf-8

# In[151]:


import numpy as np


# In[152]:


def find_total_column(table):
    returnArray = []
    for i in np.arange(np.shape(table)[1]):
        summand=0
        for j in np.arange(np.shape(table)[0]):
            summand += table[j][i]
        returnArray.append(summand)
    return returnArray
    


# In[153]:


def find_expected(table):
    returnArray = []
    for j in range(np.shape(table)[1]):
        expect_col = table[j][-1]
        intermediate=[]
        for i in range(np.shape(table)[0]-1):
            expect_row = table[-1][i]
            expected = expect_col * (expect_row/table[-1][-1])
            intermediate.append(expected)
        returnArray.append(intermediate)
    return returnArray
        
        


# In[154]:


def Z_table(table,exp_table,n,m):
    Z_table = np.zeros([n,m])
    for i in range(n):
        for j in range(m):
            Z_table[i,j] = (table[i][j] - exp_table[i][j])**2 / exp_table[i][j]
    return Z_table


# In[155]:


def chisquare(table):
    n = np.shape(table)[0]
    m = np.shape(table)[1]
    total_column = find_total_column(table)
    table = table + [total_column]
    total_row = [np.sum(table[i]) for i in range(len(table))]
    table = [np.append(table[i],total_row[i]) for i in range(len(table))]
    exp_table = find_expected(table)
    Z_Table = Z_table(table,exp_table,n,m)
    return np.sum(Z_Table)
    


# In[156]:


mat=[[90,30,30],[60,50,40],[104,51,45],[95,20,35]]


# In[157]:


chisquare(mat)


# In[ ]:




