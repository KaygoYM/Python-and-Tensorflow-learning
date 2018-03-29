# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:37:06 2018

@author: KAI
"""
from selenium import webdriver
#driver = webdriver.Chrome()     # 打开 Chrome 浏览器
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

#chrome_options = Options()
#chrome_options.add_argument("--headless")       # define headless
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()
follower_all=[]
driver.get('https://space.bilibili.com/423895#/fans/follow')
while(1):

    html=driver.page_source
    soup = BeautifulSoup(html, features='lxml')
#print(soup)
    all_href = soup.find_all('a')
#print(all_href)
    follow_path=re.compile('//space.bilibili.com/(.+?)/')
    temp=[]
    for l in all_href:
        data=l.get('href')
        #print(data)
        if data:
            if follow_path.findall(data):
                temp.append(follow_path.findall(data))
    following_id=list(set([int(f[0]) for f in temp]))
    following_id.sort()
    follower_all.append(following_id)
    elements=driver.find_elements_by_xpath("//*[@id='page-follows']/div/div[2]/div[2]/div[2]/ul[2]/li[6]")
    try:
        elements[0].click()
    except:
        break
    #driver.find_element(by='xpath', value="//*[@id='page-follows']/div/div[2]/div[2]/div[2]/ul[2]/li[6]").click()
#all_href = [l['href'] for l in all_href]
#print(all_href,'\n')
