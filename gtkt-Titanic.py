#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#Load the two datasets as pandas DataFrames
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# #Combine them into a single DataFrame
# titanic = pd.DataFrame(train.append(test))

# #Obtain basic information of variables
# titanic.head()


# In[24]:


train.keys()


# In[9]:


titanic.describe()


# In[26]:


titanic.hist()


# In[6]:


titanic_age = titanic.drop(['Pclass', 'SibSp', 'Embarked', 'Sex', 'Ticket', 'PassengerId', 'Parch', 'Name', 'Fare'], axis=1, inplace=True)


# In[2]:


print(np.corrcoef(train['Age'], train['Survived'])[0, 1])


# In[16]:


young = titanic[titanic['Age'] <= 30]
young.describe()


# In[17]:


mature = titanic[(titanic['Age'] <= 60)]
mature = titanic[(titanic['Age'] > 30)]
mature.describe()


# In[18]:


elder = titanic[(titanic['Age'] <= 80)]
elder = titanic[(titanic['Age'] > 60)]
elder.describe()


# In[ ]:





# In[34]:


plt.title("Fare")
plt.plot(titanic['Survived'], titanic['Fare'], 'b.')
plt.xlabel("Survived")
plt.ylabel("Fare")
plt.show()


# In[42]:


plt.title("Parch")
plt.plot(titanic['Parch'], titanic['Survived'], 'b.')
plt.xlabel("Survived")
plt.ylabel("Parch")
plt.show()


# In[39]:


plt.title("PassengerId")
plt.plot(titanic['Survived'], titanic['PassengerId'], 'b.')
plt.xlabel("Survived")
plt.ylabel("PassengerId")
plt.show()


# In[40]:


plt.title("Pclass")
plt.plot(titanic['Survived'], titanic['Pclass'], 'b.')
plt.xlabel("Survived")
plt.ylabel("Pclass")
plt.show()


# In[41]:


plt.title("SibSp")
plt.plot(titanic['Survived'], titanic['SibSp'], 'b.')
plt.xlabel("Survived")
plt.ylabel("SibSp")
plt.show()


# In[44]:


plt.title("Ticket")
plt.plot(titanic['Survived'], titanic['Ticket'], 'b.')
plt.xlabel("Survived")
plt.ylabel("Ticket")
plt.show()

