from selenium import webdriver
import unittest

class FindByIdName(unittest.TestCase):

    def setUp(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        elementIdToFind = "name"
        elementNameToFind = "show-hide"
        self.driver = webdriver.Firefox()
        self.driver.get(baseUrl)
        self.addCleanup(self.driver.quit)

    def testIdFind(self):

        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id(elementIdToFind)

        if elementById is not None:
            print("We found an element by the ID of " + elementIdToFind + ".")
            # if we can find our chosen elementById, print message

    def testNameFind(self):
        elementByName = driver.find_element_by_name(elementNameToFind)

        if elementByName is not None:
            print("We found an element by the name of " + elementNameToFind + ".")
            # if we can find our chosen elementByName, print message

        # quit on completion
if __name__ == "__main__":
    unittest.main(verbosity=2)
