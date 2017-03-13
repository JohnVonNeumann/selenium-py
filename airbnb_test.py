from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyformance.registry


#open AirBnb.com
baseUrl = "https://www.airbnb.com.au/"
browser = webdriver.Firefox()
browser.get(baseUrl)
browser.maximize_window()


#enter where you want to visit
searchElement = browser.find_element_by_id('search-location')
searchElement.send_keys('Melbourne, Victoria' + Keys.RETURN)


# enter checkin and checkout dates
startDateElement = browser.find_element_by_id('startDate').click()
arrivalDateToSelect = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div[2]/table/tbody/tr[3]/td[3]").click()
departureDateToSelect = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div[2]/table/tbody/tr[3]/td[7]").click()
browser.implicitly_wait(50)


# select number of guests from dropdown
guestClickElement = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/button").click()
addOneAdultClick = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/div/div/div/div[1]/div/div[2]/div/button").click()
closeAddGuest = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/div/div/div/div[4]/div/div[2]/div/button").click()
browser.implicitly_wait(50)


# click on search button
clickSearch = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[4]/button").click()
browser.implicitly_wait(50)


#exit the script and close the window
browser.quit()
