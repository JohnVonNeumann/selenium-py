from selenium import webdriver
# dl'd selenium libs

# example uses firefox but i've used chrome as that is the webdriver I installed
# you will error out if you don't place the webdriver in /usr/local/bin
browser = webdriver.Chrome()
browser.get('http://seleniumhq.org/')
