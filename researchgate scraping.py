import selenium
import pandas as pd
from selenium import webdriver
title = []
url='https://www.researchgate.net/profile/Lafta-Alkurawy'
driver = webdriver.Chrome(r'D:/chromedriver_win32/chromedriver.exe')
driver.get(url)
publication = driver.find_element_by_xpath('//*[@id="lite-page"]/main/section[3]/div[1]/div[1]/div/div/div[1]/div[1]')
totalpublication=publication.text
#vedios = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
for x in range(1,int(totalpublication)+1):
    title1=driver.find_element_by_xpath("//*[@id='research-items']/div/div/div[2]/div/div["+ str(x) +"]/div/div/div/div[2]/div/a")
    title.append(title1.text)                              
print(title)
driver.quit()
df= pd.DataFrame(title)
df.to_csv(r"C:\Users\OMEN\Desktop\python\publications.csv")
