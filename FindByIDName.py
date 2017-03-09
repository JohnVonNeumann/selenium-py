from selenium import webdriver
import unittest
import logging
import custom_logger as cl

class FindByIdName(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    def setUp(self): # setup and declaration of inputs required for sel and unittest to do its job
        # --------- Edit inputs here: -------------
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        self.elementIdToFind = "name"
        self.elementNameToFind = "show-hide"
        # --------- Do not edit below this line: -------------
        self.driver = webdriver.Firefox()
        self.driver.get(baseUrl)
        self.log.debug('Setup Complete')

    def testIdFind(self): #simple find by Id test, outputs message on completion
        elementById = self.driver.find_element_by_id(self.elementIdToFind)
        if elementById is not None:
            self.log.debug("We found an element by the ID of " + self.elementIdToFind + ".")
        else:
            self.log.error("Could not find an element by the ID of " + self.elementIdToFind + ".")

    def testNameFind(self): # simple find by name test, outputs message on completion
        elementByName = self.driver.find_element_by_name(self.elementNameToFind)
        if elementByName is not None:
            self.log.debug("We found an element by the name of " + self.elementNameToFind + ".")
        else:
            self.log.error("Could not find an element by the name of " + self.elementNameToFind + ".")

    def tearDown(self): #cleanup resources and close windows when test completes
        self.addCleanup(self.driver.quit)
        self.log.debug('Teardown complete')

if __name__ == "__main__": # run cli output and functionality from unittest lib
    unittest.main(verbosity=2)

demo = FindByIdName()
