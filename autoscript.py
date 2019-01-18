from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


userStr = "kenbhuneycutt@gmail.com"
passStr = "ichigo1g"

chrome = webdriver.Chrome()
chrome.get(('http://accounts.google.com/ServiceLogin?' 'service=mail&continue=http://mail.google' '.com/mail/#identifier'))

#username = chrome.find_element_by_id('Email')
#username.send_keys(userStr)
nextButton = chrome.find_element_by_id('next')
nextButton.click()