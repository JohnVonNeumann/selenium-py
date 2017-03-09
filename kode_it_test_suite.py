# This is going to be a complete test suite that will run tests against all aspects of the Lets Kode It
# webpage using Selenium-py

from selenium import webdriver
import unittest
import logging
import custom_logger as cl

class KodeItTestSuite(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    def setUp(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        self.driver = webdriver.Firefox()
        self.driver.get(baseUrl)
        self.log.info('Setup Complete.')














    def tearDown(self):
        self.addCleanup(self.driver.quit)
        self.log.info('Teardown Complete')

if __name__ == "__main__":
    unittest.main(verbosity=2)
