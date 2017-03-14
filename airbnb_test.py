from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AirbnbTestSuite():

    def setup(self):
        #open AirBnb.com
        baseUrl = "https://www.airbnb.com.au/"
        self.browser = webdriver.Firefox()
        self.browser.get(baseUrl)
        self.browser.maximize_window()

    def searchLocation(self):
        #enter where you want to visit
        searchElement = self.browser.find_element_by_id('search-location')
        searchElement.send_keys('Melbourne, Victoria' + Keys.RETURN)

    def checkinout(self):
        # enter checkin and checkout dates
        startDateElement = self.browser.find_element_by_id('startDate').click()
        arrivalDateToSelect = self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div[2]/table/tbody/tr[3]/td[3]").click()
        departureDateToSelect = self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div[2]/table/tbody/tr[3]/td[7]").click()

    def selectGuests(self):
        # select number of guests from dropdown
        guestClickElement = self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/button").click()
        addOneAdultClick = self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/div/div/div/div[1]/div/div[2]/div/button").click()
        closeAddGuest = self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/div/div/div/div[4]/div/div[2]/div/button").click()

    def completeSearch(self):
        # click on search button
        clickSearch = self.browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[4]/button").click()


    #exit the script and close the window
    def finishTest(self):
        self.browser.quit()

ff = AirbnbTestSuite()
ff.setup()
ff.searchLocation()
ff.checkinout()
ff.selectGuests()
ff.completeSearch()
ff.finishTest()
