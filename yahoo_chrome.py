from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Keys allows us to give a keystroke to the script, in this instance, Enter

browser = webdriver.Chrome()
# call our webdriver on an instance of Chrome

browser.get('http://www.yahoo.com')
assert 'Yahoo!' in browser.title
# direct browser to yahoo
# check if title in browser includes the word Yahoo!

elem = browser.find_element_by_name('p') # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)
# look for view element by the name of p
# using the Keys class metjod, enter seleniumhq into the search cox, and hit enter

browser.quit()
# close the browser
