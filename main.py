
#Created By Obama's Step Son#1557
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#Created By Obama's Step Son#1557
import sys
import re
import time
import random
import signal
import os
import inspect
import string
import requests
from random import randint

#Created By Obama's Step Son#1557
accounton = 0
howmany = int(input("How Many Accounts To Generate"))


#Created By Obama's Step Son#1557
while (accounton < howmany):   

  
#Created By Obama's Step Son#1557
    dictionary=open('dictionary.txt')
    lines=dictionary.readlines()
    accounton = accounton + 1

   
#Created By Obama's Step Son#1557
    username = str(lines[randint(1,10000)]+lines[randint(1,10000)]+str(randint(1,10000))).replace("\n", "")
    password = ''.join([random.choice(string.ascii_letters + string.digits ) for n in range(12)])
    email = username+'@gmail.com'
    accountlist = open('accounts.txt', 'a')
    tokenlist = open('tokens.txt', 'a')


#Created By Obama's Step Son#1557
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

#Created By Obama's Step Son#1557
    driver = webdriver.Chrome(options = options, executable_path = 'chromedriver.exe')
    driver.get("http://twitch.tv/")
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button').click()
    time.sleep(3)


#Created By Obama's Step Son#1557
    print("Entering Credentials")
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[1]/div/div[2]/input').send_keys(username)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[2]/div[1]/div[2]/div[1]/input').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[2]/div[2]/div/div[2]/div[1]/input').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[1]/select/option[5]').click()
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[2]/div/input').send_keys('19')
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[3]/div/input').send_keys('2001')
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[4]/div/div/div[2]/input').send_keys(email)

 
#Created By Obama's Step Son#1557
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[5]/button').click()
    input('Press enter when you solved the captcha.')
    driver.refresh()
    time.sleep(5)

   
#Created By Obama's Step Son#1557
    print("Writing User:Pass")
    accountlist.write("\n")
    accountlist.write(username+':'+password)

 
#Created By Obama's Step Son#1557
    print("Writing Token")
    tokenvalue = driver.get_cookie('auth-token')
    tokenlist.write("\n")
    tokenlist.write(tokenvalue["value"])
    driver.close()


#Created By Obama's Step Son#1557
print('Sucessfully created '+str(howmany)+' accounts.')