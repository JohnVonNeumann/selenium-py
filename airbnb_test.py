from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#open AirBnb.com
baseUrl = "https://www.airbnb.com.au/"
browser = webdriver.Firefox()
browser.get(baseUrl)
browser.maximize_window()

#enter where you want to visit

    #initial search element
    #<input id="search-location" class="LocationInput input-large" name="location" placeholder="Destination, city, address" autocomplete="off" value="" data-reactid="20" type="text">

searchElement = browser.find_element_by_id('search-location')
searchElement.send_keys('Melbourne, Victoria' + Keys.RETURN)

# enter checkin and checkout dates

#<input id="startDate" class="DateInput__input" aria-label="Check In" name="startDate" value="" placeholder="Check In" autocomplete="off" aria-describedby="" data-reactid="29" type="text"/>
startDateElement = browser.find_element_by_id('startDate').click()
arrivalDateToSelect = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div[2]/table/tbody/tr[3]/td[3]").click()
departureDateToSelect = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div[2]/table/tbody/tr[3]/td[7]").click()
browser.implicitly_wait(50)
    #when (checkin date picker)
    #<input id="header-checkin--sm" class="checkin input-large ui-datepicker-target" name="checkin" placeholder="Check in" type="text"/>

        # select checkin on the 16th
        #<td class="CalendarDay CalendarDay--valid CalendarDay--hovered">15</td>

        # select checkout on the 18th
        #<a class="ui-state-default ui-state-hover" href="#">18#</a>


# select number of guests from dropdown

guestClickElement = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/button").click()
addOneAdultClick = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/div/div/div/div[1]/div/div[2]/div/button").click()
closeAddGuest = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[3]/div/div/div/div/div[4]/div/div[2]/div/button").click()
browser.implicitly_wait(50)
    # select guests button
    #<button class="GuestPickerTrigger__button" type="button">

    # select close
    #<button class="component_9w5i1l-o_O-component_button_r8o91c" type="button">


# click on search button

clickSearch = browser.find_element_by_xpath("html/body/main/div/div/div[2]/div[1]/div[1]/div/form/div/div/div[4]/button").click()
browser.implicitly_wait(50)
    # search button
    #<button class="btn btn-primary btn-large btn-block" type="submit">   Search #</button>

browser.quit()
