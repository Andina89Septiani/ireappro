#web_crawler_ireappro
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#import modul yang dibutuhkan
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from pdb import set_trace as bp ##for testing
import re
import time
import csv


# %%
#running chromedriver
outputFileName='result'
link = "https://play.google.com/store/apps/details?id=com.sterling.ireappro&showAllReviews=true"
driver = webdriver.Chrome('chromedriver.exe')
driver.get(link)


# %%
title = driver.find_element_by_xpath('/html/head/meta[9]').get_attribute('content')

print(title)


# %%
# scrolling data
flag=0
while 1:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    try:
        loadMore=driver.find_element_by_xpath("//*[contains(@class,'U26fgb O0WRkf oG5Srb C0oVfc n9lfJ')]").click()
    except:
        time.sleep(1)
        flag=flag+1
        if flag >= 10:
            break
    else:
        flag=0
reviews=driver.find_elements_by_xpath("//*[@jsname='fk8dgd']//div[@class='d15Mdf bAhLNe']")


# %%
idx_review = 1

# ini nama user-nya
nama_user = reviews[idx_review].find_element_by_xpath(".//span[@class='X43Kjb']").text
# ini tanggal review-nya
tanggal_review = reviews[idx_review].find_element_by_xpath(".//span[@class='p2TkOb']").text
# ini teks review-nya
review_user = reviews[idx_review].find_element_by_xpath(".//span[@jsname='bN97Pc']").text

print("Nama user: " + nama_user)
print("Tanggal review: " + tanggal_review)
print("Review: " + review_user)


# %%
reviews_df = []
for index, review in enumerate(reviews, start=0):
    print('[' + str(index + 1) + ']--------------------------------------------------')
    # ini nama user-nya
    nama_user = reviews[index].find_element_by_xpath(".//span[@class='X43Kjb']").text
    # ini tanggal review-nya
    tanggal_review = reviews[index].find_element_by_xpath(".//span[@class='p2TkOb']").text
    # ini teks review-nya
    review_user = reviews[index].find_element_by_xpath(".//span[@jsname='bN97Pc']").text

    print("Nama user: " + nama_user)
    print("Tanggal review: " + tanggal_review)
    print("Review: " + review_user)
    print('--------------------------------------------------')
    
    temp = pd.DataFrame({'Nama':nama_user,'Tanggal':tanggal_review,'Reviews':review_user},index=[1])
    print('-'*10)
    reviews_df.append(temp)
    #print(elem)


# %%
reviews_df = pd.concat(reviews_df,ignore_index=True)


# %%
reviews_df.to_csv('reviews_ireappro.csv', encoding='utf-8')


# %%
reviews_df


# %%
rating=driver.find_elements_by_xpath(".//div[@class='vQHuPe bUWb7c']")

print ('Ratings: '+str(len(rating)))


# %%
print('data reviews terunduh '+str(len(reviews))+' buah')


# %%



