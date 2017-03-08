from selenium import webdriver
import unittest

class FindByXpathCSS(unittest.TestCase):

    def setUp(self): # setup and declaration of inputs required for sel and unittest to do its job
        # --------- Edit inputs here: -------------
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        self.elementXpathToFind = ".//*[@id='radio-btn-example']/fieldset/label[3]"
        self.elementCssToFind = "legend"
        # --------- Do not edit below this line: -------------
        self.driver = webdriver.Firefox()
        self.driver.get(baseUrl)

    def testIdFind(self): #simple find by Id test, outputs message on completion
        elementByXpath = self.driver.find_element_by_xpath(self.elementXpathToFind)
        if elementByXpath is not None:
            print("We found an element by the XPath of " + self.elementXpathToFind + ".")
        else:
            print("Could not find an element by the Xpath of " + self.elementXpathToFind + ".")

    def testNameFind(self): # simple find by name test, outputs message on completion
        elementByName = self.driver.find_element_by_css_selector(self.elementCssToFind)
        if elementByName is not None:
            print("We found an element by the CSS of " + self.elementCssToFind + ".")
        else:
            print("Could not find an element by the CSS of " + self.elementCssToFind + ".")

    def tearDown(self): #cleanup resources and close windows when test completes
        self.addCleanup(self.driver.quit)

if __name__ == "__main__": # run cli output and functionality from unittest lib
    unittest.main(verbosity=2)
