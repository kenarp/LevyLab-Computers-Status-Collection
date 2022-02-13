#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import socket
import platform
import uuid
import psycopg2 as db


# In[11]:


cmd = 'ipconfig'
res = os.popen(cmd)


# In[16]:


sys_info = platform.uname()


# In[19]:


print(sys_info)


# In[25]:


operating_system = sys_info.system + sys_info.version
print(operating_system)


# In[24]:


hostname = sys_info.node
print(hostname)


# In[49]:


processor_model = sys_info.processor
print(processor_model)


# In[50]:


ipv4_addr = socket.gethostbyname_ex(hostname)[2]
print(ipv4_addr)


# In[42]:


ping_test_ip = 'pitt.edu'
ping_result = os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + ping_test_ip)
internet_connection = ''

if ping_result == 0:
    internet_connection = 'Internet connected'
else:
    internet_connection = 'No internet connenction!'

print(internet_connection)


# In[48]:


mac_addr = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))

print(mac)


# In[2]:


postgre_connection = db.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="Abcd1234")


# In[ ]:




