import unittest
from selenium import webdriver
# standard lib we use for basic run unit test ttype functionality

class GoogleTestCase(unittest.TestCase):
# we create a new class and give it imported functionality provided by unittest lib
# in this instance, because we creating a new test, we use TestCase, which is used
# for small testcases.
# Docs: https://docs.python.org/2/library/unittest.html

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)
        # addCleanup is used to clean up resources used by the test

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    # first exposure to this type of test, so this gives us cli functionality in a clean way
    #with formatting and whatnot.
    unittest.main(verbosity=2)
    # main() can take a variety of args, verbosity=2 indicates we wish to see a lot of output info
