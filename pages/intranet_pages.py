from utils.locators import *
from pages.base_page import BasePage
import time

class IntranetMainPage(BasePage):
    def __init__(self, driver, folder_path, curr_time, logger):
        self.locator = IntranetMainPageLocator
        super().__init__(driver, folder_path, curr_time, logger)

    def click_task_list(self): # function 1 start point
        self.find_element(*self.locator.TASK_LIST).click()

    def click_file_cabinet(self):
        time.sleep(2)
        self.find_element(*self.locator.FILE_CABINET).click()
    def click_file_cabinet_layout_1(self):
        self.click_file_cabinet()
        self.find_element(*self.locator.FILE_CABINET_LAYOUT_1).click()
    def click_file_cabinet_layout_2(self):
        self.click_file_cabinet_layout_1()
        self.find_element(*self.locator.FILE_CABINET_LAYOUT_2).click()
    def click_file_cabinet_layout_3(self):
        self.click_file_cabinet_layout_2()
        time.sleep(1)
        self.find_element(*self.locator.FILE_CABINET_LAYOUT_3).click()
    def click_file_cabinet_layout_4(self):
        self.click_file_cabinet_layout_3()
        time.sleep(1)
        self.find_element(*self.locator.FILE_CABINET_LAYOUT_4).click()
    def click_file_cabinet_update_document_button(self):
        self.click_file_cabinet_layout_4()
        self.find_element(*self.locator.FILE_CABINET_UPDATE_DOCUMENT_BUTTON).click()

    def update_document_input(self, input_list):
        self.click_file_cabinet_update_document_button()
        time.sleep(1)
        self.input_content(input_list[0], *self.locator.SUBJECT_BOX)
        self.input_content(input_list[1], *self.locator.ISSUED_BY_BOX)
        self.input_content(input_list[2], *self.locator.ADDRESSED_TO_BOX)
        self.input_content(input_list[3], *self.locator.DOCUMENT_DATE_BOX)
        self.input_content(input_list[4], *self.locator.FILE_INPUT)

    def click_document_update_button(self):
        self.find_element(*self.locator.SUBMIT_BUTTON).click()

    def click_close_button(self):
        self.find_element(*self.locator.CLOSE_BUTTON).click()

    def click_top_document_subject(self):
        self.find_element(*self.locator.TOP_DOCUMENT_SUBJECT).click()

    def wait_upload_document_acknowledgement(self):
        self.wait_element(self.locator.UPDATE_DOCUMENT_ACKNOWLEDGEMENT)
    def wait_task_list_load(self):
        self.wait_element(self.locator.TASK_LIST_TABLE)
class IntranetSearchPage(BasePage):
    def __init__(self, driver, folder_path, curr_time, logger):
        self.locator = IntranetProjectPageLocator
        super().__init__(driver, folder_path, curr_time, logger)

    def click_project_search(self):
        self.find_element(*self.locator.PROJECT_SEARCH).click()

    def click_project_search_button(self): # function 2 start point
        self.find_element(*self.locator.PROJECT_SEARCH_BUTTON).click()

    def wait_project_search_result_load(self):
        self.wait_element(self.locator.PROJECT_SEARCH_RESULT_TABLE)

class IntranetContractPage(BasePage):
    pass

class IntranetCentralFunctionsPage(BasePage):
    pass

class IntranetReportPage(BasePage):
    pass
class IntranetKMPage(BasePage):
    def __init__(self, driver, folder_path, curr_time, logger):
        self.locator = IntranetKMPageLocator
        super().__init__(driver, folder_path, curr_time, logger)

    def click_KR(self):
        self.find_element(*self.locator.KNOWLEDGE_REPOSITORY).click()

    def click_KR_browse(self):
        self.click_KR()
        self.find_element(*self.locator.KR_BROWSE).click()

    def click_KR_browse_DCD_top_link(self): # function 3 start point
        self.find_element(*self.locator.KR_BROWSE_DCD_TOP_DOC).click()


    def wait_KM_document_load(self):
        self.wait_element(self.locator.KM_DOC_TABLE)
