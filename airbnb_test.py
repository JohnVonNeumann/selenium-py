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

    #when (checkin date picker)
    #<input id="header-checkin--sm" class="checkin input-large ui-datepicker-target" name="checkin" placeholder="Check in" type="text"/>

        # select checkin on the 16th
        #<td class="CalendarDay CalendarDay--valid CalendarDay--hovered">15</td>

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
