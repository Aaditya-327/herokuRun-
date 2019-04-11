
# coding: utf-8

# In[12]:


import requests
from bs4 import BeautifulSoup
from datetime import datetime
import praw


from sendText import text


# In[13]:


#Get data from the link in HTML format
linkToday = "http://nepalicalendar.rat32.com/"

r = requests.get(linkToday)


# In[14]:


#Extract data from the page
soup = BeautifulSoup(r.text, 'html.parser')

Month = soup.find("div", {"id": "mth"}).text[1:]
Date = soup.find("div", {"id": "gate"}).text[:-4]
Year = soup.find("div", {"id": "yr"}).text[1:-6]
Week = soup.find("div", {"id": "bar"}).text
English = datetime.today().strftime('%Y %B %d')
combine = " ".join([Year, Month, Date])

display = u"""WK   {}

EN  {}
NP  {}

TIL """.format(Week, combine, English)


# In[15]:


extra = ["Aad1tya23","p@ssw0rd","cqtbqCS6tCeJ9g","JQwcpZR8346OcezEg2XRQCYxksw"]
ua = "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"
reddit = praw.Reddit(user_agent= ua,
                     client_id= extra[2],
                     client_secret= extra[3],
                     username= extra[0],
                     password= extra[1])

subTop = reddit.subreddit('todayilearned').top("day")
for _ in subTop:
    display2 = _.title
    break


# In[17]:



if len(display2)>144:
    A = display2[4:][:144] + " ..."
    B = "... " + display2[4:][144:]
    text(A, ['9843147666'])
    text(B, ['9843147666'])
    text(display, ['9843147666'])
    
else:
    text(display2, ['9843147666'])
    text(display, ['9843147666'])

