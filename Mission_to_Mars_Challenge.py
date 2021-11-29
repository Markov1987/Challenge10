#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[29]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[30]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[31]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[32]:


slide_elem.find('div', class_='content_title')


# In[33]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[34]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[35]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[36]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[37]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[38]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[39]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[40]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[41]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[42]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[43]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)
html = browser.html
image_soup = soup(html, 'html.parser')


# In[47]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

#Define Base Url    
Base_url="https://marshemispheres.com/"

#Loop through images
for i in range(4):
    
    #Get titles
    title=image_soup.find_all("h3")
    title=title[i].get_text()
    first_click=browser.find_by_tag("img",wait_time=3)[i+3]
    first_click.click()
    
    new_html=browser.html
    new_soup = soup(new_html, 'html.parser')
    browser.is_element_present_by_css('div.list_text',wait_time=3)
    photos_url= new_soup.find_all("a")[3].get("href")
    
    #Get Images
    img_url=Base_url+photos_url
    hemisphere_dict={"img_url":img_url,"title":title}
    
    #Add to Dictionary
    hemisphere_image_urls.append(hemisphere_dict)
    
    browser.back()


# In[48]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[25]:


# 5. Quit the browser
browser.quit()


# In[ ]:




