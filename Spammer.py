from os import read
from selenium import webdriver
import time

'''
Requires Chrome version 93 To Run
'''

driver = webdriver.Chrome()

sitetext=open("site.txt","r")#Change site.txt with your google form
sitedata=sitetext.read()

driver.get(sitedata)
time.sleep(2)

loop = True
while loop == True:
    button = driver.find_element_by_xpath("""//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span""") # clicks the submit button (doesn't click anything else so it only works if it has requirements)
    button.click()
    time.sleep(0.15)
    driver.refresh()