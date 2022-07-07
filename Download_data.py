#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
counter = 1
with open('url.txt') as my_file:
    for line in my_file:
        URL = line.strip()
        FILENAME = str(counter) + '.nc4'
        counter+= 1
        result = requests.get(URL)
        try:
            result.raise_for_status()
            f = open(FILENAME,'wb')
            f.write(result.content)
            f.close()
            print('contents of URL written to '+FILENAME)
        except:
            print('requests.get() returned an error code '+str(result.status_code))
        
       


# In[ ]:




