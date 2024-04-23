import datetime
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.locators import *


# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):
    def __init__(self, driver, folder_path, curr_time, logger):
        self.driver = driver
        self.folder_path = folder_path
        self.curr_time = curr_time
        self.timeout = 30
        self.top_menu_locator = TopMenuLocator
        self.based_button = BasedButton
        self.logger = logger


    def wait_element(self, locator):
        try:
            self.driver.implicitly_wait(self.timeout)
            element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

        except TimeoutException:
            self.logger.error("\n* ELEMENT NOT FOUND WITHIN EXPECTED TIME! --> %s" %(locator[1]), "*\n")
            self.driver.quit()

    def find_element(self, *locator):
        try:
            self.driver.implicitly_wait(self.timeout)
            self.wait_element(locator)
            return self.driver.find_element(*locator)

        except TimeoutException:
            self.logger.error("\n* ELEMENT NOT FOUND WITHIN EXPECTED TIME! --> %s" %(locator[1]), "*\n")
            self.driver.quit()

    def input_content(self, content, *locator):
        self.find_element(*locator).send_keys(content)

    def get_downloaded_file(self, download_dir):
        time.sleep(1)

        # wait for file downloading
        seconds = 0
        dl_wait = True
        while dl_wait and seconds < self.timeout*10:
            time.sleep(0.01)
            dl_wait = False
            for fname in os.listdir(download_dir):
                if fname.endswith('.crdownload'):
                    dl_wait = True
            seconds += 0.01

        time.sleep(1)
        # return the datetime of last downloading file
        list = os.listdir(download_dir)
        list.sort(key=lambda fn: os.path.getmtime(download_dir + "\\" + fn)) # sort by time
        file = os.path.getmtime(download_dir + "\\" + list[-1])
        return datetime.datetime.fromtimestamp(file)

    def screen_capture(self, suffix):
        self.driver.get_screenshot_as_file(self.folder_path + "\\" + suffix)

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
    def switch_to_windows(self, handle_index):
        self.driver.switch_to.window(self.driver.window_handles[handle_index])

    def alert_operation(self, accept):
        if(accept):
            self.driver.switch_to.alert.accept()
        elif(not accept):
            self.driver.switch_to.alert.dissmiss()

    def wait_new_window_load(self):
        try:
            self.driver.implicitly_wait(self.timeout)
            WebDriverWait(self.driver, self.timeout).until(EC.number_of_windows_to_be(2))

        except TimeoutException:
            self.logger.error("\n* NO EXTRA WINDOW HAS BEEN FOUND WITHIN EXPECTED TIME! *\n")
            self.driver.quit()
    def log_out(self):
        try:
            self.find_element(*self.based_button.LOGOUT).click()
            self.logger.info("Successfully log out!")

        except TimeoutException:
            self.logger.error("\n* COULD NOT FOUND LOG OUT BUTTON WITHIN EXPECTED TIME! *\n")

    def goto_top_menu(self, index):
        if index == 1:
            self.find_element(*self.top_menu_locator.MENU_MAIN).click()
        elif index == 2:
            self.find_element(*self.top_menu_locator.MENU_2).click()
        elif index == 3:
            self.find_element(*self.top_menu_locator.MENU_3).click()
        elif index == 4:
            self.find_element(*self.top_menu_locator.MENU_4).click()
        elif index == 5:
            self.find_element(*self.top_menu_locator.MENU_5).click()
        elif index == 6:
            self.find_element(*self.top_menu_locator.MENU_6).click()
        else:
            self.logger.error("Invalid index number, please input the top menu you want to go to in range (1-6)")
