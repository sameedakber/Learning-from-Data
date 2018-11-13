
# coding: utf-8

# In[35]:


coins = range(0,1000)


# In[36]:


import random
c_1 = 0
c_rand = random.randint(0,1000)
c_min=11


# In[37]:


def coin_flip_1000():
    coin_data = []
    c_min_flips = []
    for coin in coins:
        flips = []
        for i in range(10):
            flips.append(random.randint(0,1))
        head_count = sum([x for x in flips if x==1])
        if head_count < c_min:
            c_min==head_count
            c_min_flips = flips
        if coin==c_1:
            coin_data.append(flips)
        if coin==c_rand:
            coin_data.append(flips)
    coin_data.append(c_min_flips)
    return coin_data


# In[81]:


import numpy as np
total_coin_flip_data = np.zeros((1000,3))
for i in range(1000):
    coin_data = coin_flip_1000()
    total_coin_flip_data[i] = np.mean(coin_data,axis=1)


# In[82]:


import matplotlib.pyplot as plt
import pandas as pd


# In[83]:


data = pd.DataFrame(total_coin_flip_data,columns=pd.Index(['v1','vrand','vmin']))


# In[84]:


data.hist(figsize=(12,8))


# In[86]:


e = np.linspace(0,0.1,200)


# In[87]:


mu = 0.5


# In[92]:


data['v1-mu'] = abs(data.v1-mu)


# In[94]:


data['vrand-mu'] = abs(data.vrand-mu)


# In[93]:


data['vmin-mu'] = abs(data.vmin-mu)


# In[95]:


data.head()


# In[106]:


probabilities = []
for i in e:
    count = 0
    for j in data['v1-mu']:
        if j-mu>i:
            count+=1
    probabilities.append(count/data.shape[0])   


# In[107]:


probabilities


# In[108]:


data.shape


# In[109]:


data.shape[0]


# In[110]:


45/50


# In[111]:


900/1000

