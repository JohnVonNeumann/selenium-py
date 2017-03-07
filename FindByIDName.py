from selenium import webdriver
import unittest

class FindByIdName(unittest.TestCase):

    def setUp(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        self.elementIdToFind = "name"
        self.elementNameToFind = "show-hide"
        self.driver = webdriver.Firefox()
        self.driver.get(baseUrl)

    def testIdFind(self):
        elementById = self.driver.find_element_by_id(self.elementIdToFind)
        if elementById is not None:
            print("We found an element by the ID of " + self.elementIdToFind + ".")
            # if we can find our chosen elementById, print message

    def testNameFind(self):
        elementByName = self.driver.find_element_by_name(self.elementNameToFind)
        if elementByName is not None:
            print("We found an element by the name of " + self.elementNameToFind + ".")
            # if we can find our chosen elementByName, print message

    def tearDown(self):
        self.addCleanup(self.driver.quit)

if __name__ == "__main__":
    unittest.main(verbosity=2)
