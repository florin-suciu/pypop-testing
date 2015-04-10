from constants.common import PARKING_TITLE, PARKING_URL

from pypop.pageobjects.base_page_element import BasePageElement, BasePageElementClearFirst
from pypop.pageobjects.base_page_object import BasePageObject

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#=======================================================================================================================
# locators
#=======================================================================================================================
locators = {}
locators['parking.lot'] = By.ID, 'Lot'
locators['parking.entry_time'] = By.ID, 'EntryTime'
locators['parking.entry_date'] = By.ID, 'EntryDate'
locators['parking.exit_time'] = By.ID, 'ExitTime'
locators['parking.exit_date'] = By.ID, 'ExitDate'
locators['parking.calculate'] = By.XPATH, '//input[@type="submit" and @name="Submit"]'
# TODO: following 2 locators are not good, need updating
locators['parking.result_price'] = By.CLASS_NAME, 'SubHead'
locators['parking.result_time'] = By.CLASS_NAME, 'BodyCopy'


class ParkingCalculatorPageObject(BasePageObject):

    lot = BasePageElement(locators.get('parking.lot'))
    start_time = BasePageElementClearFirst(locators.get('parking.entry_time'))
    start_date = BasePageElementClearFirst(locators.get('parking.entry_date'))
    end_time = BasePageElementClearFirst(locators.get('parking.exit_time'))
    end_date = BasePageElementClearFirst(locators.get('parking.exit_date'))

    def __init__(self, driver):
        self.driver = driver
        try:
            self.assertEqual(PARKING_TITLE, self.driver.title)
        except AssertionError:
            self.driver.get(PARKING_URL)
            self.assertEqual(PARKING_TITLE, self.driver.title)

    def calculate(self):
        by, locator = locators.get("parking.calculate")
        calculate_button = self.driver.find_element(by, locator)
        calculate_button.click()

    def check_value(self):
        time_by, time_locator = locators.get("parking.result_time")
        price_by, price_locator = locators.get("parking.result_price")

        a = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((time_by, time_locator)))

        time_element = self.driver.find_element(time_by, time_locator).get_attribute('value')
        price = self.driver.find_element(price_by, price_locator).get_attribute('value')

        # TODO: continue check after setting the locators right
