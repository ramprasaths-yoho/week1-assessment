#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../data/employees.csv")

print(df.head())
print("Total employees:", len(df))
print("Average salary:", df["salary"].mean())
print("Highest salary:", df["salary"].max())


# In[2]:


summary = df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean")
)

display(summary)


# In[3]:


summary["average_salary"].plot(
    kind="bar",
    legend=False,
    color="skyblue"
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()


# In[4]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')

