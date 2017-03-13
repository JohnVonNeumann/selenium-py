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

searchElement = browser.find_element_by_name('location')
searchElement.send_keys('Melbourne, Victoria' + Keys.RETURN)

    #once inital has been clicked, modal opens up, where input
    #<input id="header-location--sm" class="input-large needsClick" placeholder="Destination, city, address" autocomplete="off" name="location" type="text"/>


# enter checkin and checkout dates

    #when (checkin date picker)
    #<input id="header-checkin--sm" class="checkin input-large ui-datepicker-target" name="checkin" placeholder="Check in" type="text"/>

        # select checkin on the 16th
        #<a class="ui-state-default ui-state-hover" href="#">16#</a>

        # select checkout on the 18th
        #<a class="ui-state-default ui-state-hover" href="#">18#</a>


# select number of guests from dropdown

    # select guests button
    #<button class="GuestPickerTrigger__button" type="button">

    # select close
    #<button class="component_9w5i1l-o_O-component_button_r8o91c" type="button">


# click on search button

    # search button
    #<button class="btn btn-primary btn-large btn-block" type="submit">   Search #</button>

browser.quit()
