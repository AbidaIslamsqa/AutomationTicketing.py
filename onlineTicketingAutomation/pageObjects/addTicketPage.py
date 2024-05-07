from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage


class AddTicketPage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Defining the locators in Login page
    loginButton = (By.XPATH, "(//a[normalize-space()='Login'])")

    # Methods for obtaining locators in the test script
    def getLoginButton(self):
        self.driver.find_element(*AddTicketPage.loginButton).click()
        loginPage = LoginPage(self.driver)
        return loginPage