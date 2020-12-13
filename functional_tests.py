from selenium import webdriver 

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title #checking that the page has the word 'Django' in the title