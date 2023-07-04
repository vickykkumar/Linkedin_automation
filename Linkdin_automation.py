#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from selenium.webdriver.common.keys import Keys

#file name where you have all the linkdin mails of the peoples if you want you can change this part
df1=pd.read_excel('Recruiters List.xlsx',engine="openpyxl")


# In[2]:


import time


# In[3]:


df1.head()


# In[4]:


Name=df1['Name']


# In[8]:

#profiles list
linkdin_profiles=df1['LinkedIn Profile ']


# In[9]:


linkdin_profiles[0]


# In[5]:


linkdin_profiles=df1["LinkedIn Profile "]


# In[36]:


from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver= wd.Chrome('YOUR CHROME DRIVER PATH')
driver.get('https://www.linkedin.com/')
try:
    
    time.sleep(5)
    email=driver.find_element(By.NAME,'session_key')
    email.send_keys('username')
    password=driver.find_element(By.NAME,'session_password')
    password.send_keys('password')
    password.send_keys(Keys.ENTER)
    time.sleep(20)
    for i in range(8,len(linkdin_profiles)):
        driver.get(linkdin_profiles[i])
        try:
            content=driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div')
            l1=content.text.split('\n')
        
            if(l1[0]!='Connect'):
                try:
                    more=WebDriverWait(driver,5).until(
                        EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button/span'))
                    )
                    more.click()
                except:
                    more=WebDriverWait(driver,5).until(
                        EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button/span'))
                    )
                    more.click()
                time.sleep(2)
                try:
                    connect=driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[3]/div')
                    connect.click()
                except:
                    connect=driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[3]/div')
                    connect.click()
            else:
                connect=driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button/span')
                connect.click()
        except:
            continue
    

        note=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div[3]/button[1]'))
        )
        note.click()
        time.sleep(5)
        message=driver.find_element(By.NAME,'message')
        message.send_keys(f"Hi {Name[i]} , I’m reaching out because I’m exploring new opportunities. I am a student at Edith Cowan University, Australia with this I have 2 plus years of experience as a data analyst, and now looking for a remote internship. If you have time, let’s discuss If there are opportunities available.")
        send_message=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]/span')
        send_message.click()

except:
    print('unable to login or unable to find Connect option.')

