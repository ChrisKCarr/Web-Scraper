
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


r = requests.get("http://pythonhow.com/example.html")
c=r.content


# In[5]:


soup=BeautifulSoup(c,"html.parser")


# In[16]:


all=soup.find_all("div",{"class":"cities"})


# In[18]:


for item in all:
    print(item.find_all("h2")[0].text)

