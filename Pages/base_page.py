class BasePage:
    URL = 'https://formy-project.herokuapp.com/'

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()
