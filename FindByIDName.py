from selenium import webdriver

class FindByIdName():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        elementIdToFind = "name"
        elementNameToFind = "show-hide"
        # var setting for easy change of inputs

        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id(elementIdToFind)

        if elementById is not None:
            print("We found an element by the ID of " + elementIdToFind + ".")
            # if we can find our chosen elementById, print message

        elementByName = driver.find_element_by_name(elementNameToFind)

        if elementByName is not None:
            print("We found an element by the name of " + elementNameToFind + ".")
            # if we can find our chosen elementByName, print message
        driver.quit()
        # quit on completion

ff = FindByIdName()
ff.test()
