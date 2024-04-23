from utils.locators import *
from pages.base_page import BasePage
import time

class ExtranetMainPage(BasePage):
    def __init__(self, driver, folder_path, curr_time, logger):
        self.locator = ExtranetMainPageLocator
        super().__init__(driver, folder_path, curr_time, logger)


    def click_task_list(self): # function 6 start point
        self.find_element(*self.locator.TASK_LIST).click()

    def wait_task_list_load(self):
        self.wait_element(self.locator.TASK_LIST_TABLE)
class ExtranetContractPage(BasePage):
    def __init__(self, driver, folder_path, curr_time, logger):
        self.locator = ExtranetContractPageLocator
        super().__init__(driver, folder_path, curr_time, logger)

    def activate_daily_report(self):
        self.find_element(*self.locator.UN99NR).click()
        self.find_element(*self.locator.UN99NR_9999998).click()
    def click_BW(self):
        self.activate_daily_report()
        time.sleep(1)
        self.find_element(*self.locator.BW).click()
    def click_BW_daily_report(self):
        self.click_BW()
        time.sleep(1)
        self.find_element(*self.locator.BW_DAILY_REPORT).click()
    def click_BW_daily_new_button(self):
        self.click_BW_daily_report()
        self.find_element(*self.locator.BW_DAILY_REPORT_NEW_BUTTON).click()
    def click_BW_daily_clip_image(self):
        self.click_BW_daily_new_button()
        self.find_element(*self.locator.BW_DAILY_REPORT_CLIP_IMAGE).click()

class ExtranetCentralFunctionPage(BasePage):
    pass
class ExtranetKMPage(BasePage):
    def __init__(self, driver, folder_path, curr_time, logger):
        self.locator = ExtranetKMPageLocator
        super().__init__(driver, folder_path, curr_time, logger)

    def click_material_database(self):
        time.sleep(8)
        self.find_element(*self.locator.MATERIALS_DATABASE).click()

    def click_DCD(self):
        time.sleep(2)
        self.find_element(*self.locator.DCD).click()

    def click_DCD_CONTRACTOR_ACCESS(self):
        self.click_DCD()
        self.find_element(*self.locator.DCD_CONTRACTOR_ACCESS).click()

    def click_DCD_CONTRACTOR_ACCESS_DOCUMENT_1(self):
        self.click_DCD_CONTRACTOR_ACCESS()
        self.find_element(*self.locator.DCD_CONTRACTOR_ACCESS_DOCUMENT_1).click()

    def click_DCD_CONTRACTOR_ACCESS_DOCUMENT_1_EXCEL_1(self):
        self.find_element(*self.locator.DCD_CONTRACTOR_ACCESS_DOCUMENT_1_EXCEL_1).click()
    def click_material_database_layout_1(self):
        self.click_material_database()
        time.sleep(1)
        self.find_element(*self.locator.MATERIALS_BW).click()
    def click_material_database_layout_2(self):
        self.click_material_database_layout_1()
        time.sleep(1)
        self.find_element(*self.locator.MATERIALS_BW_CLAC).click()

    def click_material_database_layout_3(self):  # function 7 start point
        self.find_element(*self.locator.MATERIALS_BW_CLAC_OTHERS).click()

    def wait_material_database_document_load(self):
        self.wait_element(self.locator.MATERIAL_DATABASE_DOC_TABLE)


class AttechmentWindow(BasePage):
    def __init__(self, driver, folder_path, curr_time, logger):
        self.locator = AttachmentWindowLocator
        super().__init__(driver, folder_path, curr_time, logger)

    def click_new_attachment_button(self):
        self.find_element(*self.locator.NEW_ATTACHMENT_BUTTON).click()

    def daily_report_input_file(self, input_list):
        self.click_new_attachment_button()
        time.sleep(1)
        self.input_content(input_list[0], *self.locator.DOCUMENT_TITTLE_BOX)
        self.input_content(input_list[1], *self.locator.DOCUMENT_DATE_BOX)
        self.input_content(input_list[2], *self.locator.DOCUMENT_FILE_INPUT)

    def wait_delete_button(self):
        self.wait_element(self.locator.DELETE_BUTTON)

    def click_confirm_button(self):
        self.find_element(*self.locator.CONFIRM_BUTTON).click()

    def click_retrieve_button(self):
        self.find_element(*self.locator.RETRIEVE_BUTTON).click()

    def click_delete_button(self):
        self.find_element(*self.locator.DELETE_BUTTON).click()
