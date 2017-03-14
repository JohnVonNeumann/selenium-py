from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyformance import meters
from pyformance import reporters
import time


class AirbnbTestSuite:

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.baseurl = "https://www.airbnb.com.au/"
        self.browser.get(self.baseurl)
        self.browser.maximize_window()
        self.timer = meters.Timer()

    def searchlocation(self):
        #enter where you want to visit
        self.searchelement = self.browser.find_element_by_id('search-location')
        self.searchelement.send_keys('Melbourne, Victoria' + Keys.RETURN)

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

reporter = reporters.ConsoleReporter()
reporter.report_now()
ff = AirbnbTestSuite()
ff.searchlocation()
ff.checkinout()
ff.selectguests()
ff.completesearch()
ff.finishtest()
