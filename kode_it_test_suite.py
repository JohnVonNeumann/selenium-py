# This is going to be a complete test suite that will run tests against all aspects of the Lets Kode It
# webpage using Selenium-py

from selenium import webdriver
import unittest
import logging
import custom_logger as cl

class KodeItTestSuite(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    def setUp(self):
        # -----------Edit inputs here: ----------
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        self.elementIdToFind = "mouseover"
        self.elementClassToFind = "navbar"

        #---------Do not edit below this line ---------
        self.driver = webdriver.Firefox()
        self.driver.get(baseUrl)
        self.log.info('Setup Complete.')

    def testIdFind(self):
        elementById = self.driver.find_elements_by_id(self.elementIdToFind)
        if elementById is not None:
            self.log.info("We found an element by the ID of " + self.elementIdToFind + ".")
        else:
            self.log.error("Could not find an element by the ID of " + self.elementIdToFind + ".")

    def testClassFind(self):
        elementByClass = self.driver.find_elements_by_class_name(self.elementClassToFind)
        if elementByClass is not None:
            self.log.info("We found an element by the Class Name of " + self.elementClassToFind + ".")
        else:
            self.log.error("Could not find an element by the Class Name of " + self.elementClassToFind + ".")















    def tearDown(self):
        self.addCleanup(self.driver.quit)
        self.log.info('Teardown Complete')

if __name__ == "__main__":
    unittest.main(verbosity=2)
