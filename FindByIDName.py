from selenium import webdriver

class FindByIdName():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        elementToFind = "name"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id(elementToFind)

        if elementById is not None:
            print("We found #{elementToFind}")

ff = FindByIdName()
ff.test()
