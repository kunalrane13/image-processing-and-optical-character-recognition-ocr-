#!/usr/bin/env python
# coding: utf-8

# In[37]:


pip install easyocr


# In[38]:


import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image


# In[39]:


rcParams['figure.figsize'] = 8, 16


# In[40]:


reader = easyocr.Reader(['en', 'hi'])


# In[41]:


file_name = "Mission.jpg"


# In[42]:


Image(file_name)


# In[43]:


output = reader.readtext(file_name, detail = 0)


# In[44]:


output


# In[52]:


# import pandas as pd

# df = pd.DataFrame(columns=['Crs-ID', 'Course tittle', 'Att/Cmp'])

# for entry in output:
#     coordinates = entry[0]
#     text = entry[1]
#     confidence = entry[2]
#     df = df.append({'Crs-ID': coordinates, 'Course tittle': text, 'Att/Cmp': confidence}, ignore_index=True)

# df['Coordinates'] = df['Coordinates'].apply(lambda x: str(x))

import pandas as pd

df = pd.DataFrame(columns=['Crs-ID', 'Course Title', 'Att', 'Cmp'])

for entry in output:
    if 'Crs-ID' in text:
        crs_id = text
    elif 'Course Title' in text:
        course_title = text
    elif 'Att' in text:
        att = text
    elif 'Cmp' in text:
        cmp = text
        vdf = df.append({'Crs-ID': crs_id, 'Course Title': course_title, 'Att': atv, 'Cmp': cmp}, ignore_index=True)


# In[53]:


df


# In[ ]:




