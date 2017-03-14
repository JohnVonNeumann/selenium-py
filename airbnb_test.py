from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AirbnbTestSuite:

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.baseurl = "https://www.airbnb.com.au/"
        self.browser.get(baseurl)
        self.browser.maximize_window()

    def searchlocation(self):
        #enter where you want to visit
        searchelement = self.browser.find_element_by_id('search-location')
        searchelement.send_keys('Melbourne, Victoria' + Keys.RETURN)

    def checkinout(self):
        # enter checkin and checkout dates
        self.browser.find_element_by_id('startDate').click()
        self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div[2]/table/tbody/tr[3]/td[3]").click()
        self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div[2]/table/tbody/tr[3]/td[7]").click()

    def selectguests(self):
        # select number of guests from dropdown
        self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/button").click()
        self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/div/div/div/div[1]/div/div[2]/div/button").click()
        self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/div/div/div/div[4]/div/div[2]/div/button").click()

    def completesearch(self):
        # click on search button
        self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[4]/button").click()


    #exit the script and close the window
    def finishtest(self):
        self.browser.quit()

ff = AirbnbTestSuite()
ff.searchocation()
ff.checkinout()
ff.selectguests()
ff.completesearch()
ff.finishtest()
