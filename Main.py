from pages.intranet_pages import *
from pages.extranet_pages import *
from pages.base_page import *
from utils.setup import *
import time
import datetime
import sys

class BPUSpeedMeasure(object):
    def __init__(self, driver, folder_path, curr_time, logger):
        self.driver = driver
        self.folder_path = folder_path
        self.curr_time = curr_time
        self.timeout = 30
        self.logger = logger

    def wait_user_manually_login(self):
        print("Please input the account name, password and token manually within 3 minutes:\n ")

        try:  # wait user manually finish login page
            element = WebDriverWait(self.driver, 180).until(
                EC.presence_of_element_located((By.ID, "shadow")))
        except:
            self.logger.error("Login Fails, Please login on time!")
            sys.exit()

    def function_1(self):
        # set the instance
        page = IntranetMainPage(self.driver, self.folder_path, self.curr_time, self.logger)
        self.logger.info("Function 1: Task List display (Intranet)")

        # start timeR
        time.sleep(2)
        page.screen_capture("-f1-time_mark_start.png")
        start = datetime.datetime.now()
        self.logger.info("Time mark start: " + str(start))
        page.click_task_list()

        # wait
        page.wait_task_list_load()

        # stop timer
        end = datetime.datetime.now()
        loading_time = round((end-start).seconds + (end - start).microseconds/1e6, 2)
        self.logger.info("Time mark stop: "+str(end)+"\nFunction 1 loading time: "+str(loading_time)+"\n")
        page.screen_capture("-f1-time_mark_stop.png")

        return loading_time

    def function_2(self):
        #set the instance
        page = IntranetSearchPage(self.driver, self.folder_path, self.curr_time, self.logger)
        self.logger.info("Function 2: Search Projects load")

        time.sleep(1)
        page.goto_top_menu(2)
        page.click_project_search()

        # start timer
        time.sleep(2)
        page.screen_capture("-f2-time_mark_start.png")
        start = datetime.datetime.now()
        self.logger.info("Time mark start: " + str(start))
        page.click_project_search_button()

        # wait
        page.wait_project_search_result_load()

        # stop timer
        end = datetime.datetime.now()
        loading_time = round((end-start).seconds + (end - start).microseconds/1e6, 2)
        self.logger.info("Time mark stop: "+str(end)+"\nFunction 2 loading time: "+str(loading_time)+"\n")
        page.screen_capture("-f2-time_mark_stop.png")

        return loading_time

    def function_3(self):
        # set the instance
        page = IntranetKMPage(self.driver, self.folder_path, self.curr_time, self.logger)
        self.logger.info("Function 3: KR document browse")

        time.sleep(1)
        page.goto_top_menu(6)
        page.click_KR_browse()

        # start timer
        time.sleep(2)
        page.screen_capture("-f3-time_mark_start.png")
        start = datetime.datetime.now()
        self.logger.info("Time mark start: " + str(start))
        page.click_KR_browse_DCD_top_link()

        # wait
        page.wait_KM_document_load()

        # stop timer
        end = datetime.datetime.now()
        loading_time = round((end-start).seconds + (end - start).microseconds/1e6, 2)
        self.logger.info("Time mark stop: "+str(end)+"\nFunction 3 loading time: "+str(loading_time)+"\n")
        page.screen_capture("-f3-time_mark_stop.png")

        return loading_time

    def function_4(self):
        # set the instance
        page = IntranetMainPage(self.driver, self.folder_path, self.curr_time, self.logger)
        self.logger.info("Function 4: Testing document update into CABIN")

        time.sleep(1)
        page.goto_top_menu(1)
        page.update_document_input([
            Function_4_input_content.SUBJECT,
            Function_4_input_content.ISSUED_BY,
            Function_4_input_content.ADDRESSED_TO,
            Function_4_input_content.DOCUMENT_DATE,
            Function_4_input_content.FILE_INPUT])

        # start timer
        time.sleep(2)
        page.screen_capture("-f4-time_mark_start.png")
        start = datetime.datetime.now()
        self.logger.info("Time mark start: " + str(start))
        page.click_document_update_button()

        # wait
        page.wait_upload_document_acknowledgement()

        # stop timer
        end = datetime.datetime.now()
        loading_time = round((end-start).seconds + (end - start).microseconds/1e6, 2)
        self.logger.info("Time mark stop: "+str(end)+"\nFunction 4 loading time: "+str(loading_time)+"\n")
        page.screen_capture("-f4-time_mark_stop.png")

        return loading_time

    def function_5(self):
        # set the instance
        page = IntranetMainPage(self.driver, self.folder_path, self.curr_time, self.logger)
        self.logger.info("Function 5: Testing document download from CABIN")

        time.sleep(1)
        page.click_close_button()

        # start timer
        time.sleep(2)
        page.screen_capture("-f5-time_mark_start.png")
        start = datetime.datetime.now()
        self.logger.info("Time mark start: " + str(start))
        page.click_top_document_subject()

        # stop timer
        end = page.get_downloaded_file(FilePath.DOWNLOAD_FOLDER_PATH)
        loading_time = round((end-start).seconds + (end - start).microseconds/1e6, 2)
        self.logger.info("Time mark stop: "+str(end)+"\nFunction 5 loading time: "+str(loading_time)+"\n")
        page.log_out()

        return loading_time

    def function_6(self):
        # set the instance
        page = ExtranetMainPage(self.driver, self.folder_path, self.curr_time, self.logger)
        self.logger.info("Function 6: Task List display (Extranet)")

        # start timeR
        time.sleep(2)
        page.screen_capture("-f6-time_mark_start.png")
        start = datetime.datetime.now()
        self.logger.info("Time mark start: " + str(start))
        page.click_task_list()

        # wait
        page.wait_task_list_load()

        # stop timer
        end = datetime.datetime.now()
        loading_time = round((end - start).seconds + (end - start).microseconds / 1e6, 2)
        self.logger.info("Time mark stop: "+str(end)+"\nFunction 6 loading time: "+str(loading_time)+"\n")
        page.screen_capture("-f6-time_mark_stop.png")

        return loading_time

    def function_7(self):
        # set the instance
        page = ExtranetKMPage(self.driver, self.folder_path, self.curr_time, self.logger)
        self.logger.info("Function 7: Browse a Material Database item")

        time.sleep(1)
        page.goto_top_menu(4)
        page.click_material_database_layout_2()

        # start timer
        time.sleep(2)
        page.screen_capture("-f7-time_mark_start.png")
        start = datetime.datetime.now()
        self.logger.info("Time mark start: " + str(start))
        page.click_material_database_layout_3()

        # wait
        page.wait_material_database_document_load()

        # stop timer
        end = datetime.datetime.now()
        loading_time = round((end - start).seconds + (end - start).microseconds / 1e6, 2)
        self.logger.info("Time mark stop: "+str(end)+"\nFunction 7 loading time: "+str(loading_time)+"\n")
        page.screen_capture("-f7-time_mark_stop.png")

        return loading_time
    def function_8(self):
        # set the instance
        page = ExtranetContractPage(self.driver, self.folder_path, self.curr_time, self.logger)
        self.logger.info("Function 8: Upload a 5MB document into Contract folder")

        time.sleep(1)
        page.goto_top_menu(2)
        page.click_BW_daily_clip_image()

        # Switch to new-generated window
        page.switch_to_windows(1)
        window = AttechmentWindow(self.driver, self.folder_path, self.curr_time, self.logger)
        window.daily_report_input_file([
            Function_8_input_content.DOCUMENT_TITTLE,
            Function_8_input_content.DOCUMENT_DATE,
            Function_8_input_content.FILE_INPUT])

        # start timer
        time.sleep(2)
        window.screen_capture("-f8-time_mark_start.png")
        window.click_confirm_button()
        start = datetime.datetime.now()
        self.logger.info("Time mark start: " + str(start))
        window.alert_operation(True)

        # wait
        window.wait_delete_button()

        # stop timer
        end = datetime.datetime.now()
        loading_time = round((end - start).seconds + (end - start).microseconds / 1e6, 2)
        self.logger.info("Time mark stop: "+str(end)+"\nFunction 8 loading time: "+str(loading_time)+"\n")
        window.screen_capture("-f8-time_mark_stop.png")

        return loading_time
    def function_9(self):
        # set the instance
        page = AttechmentWindow(self.driver, self.folder_path, self.curr_time, self.logger)
        self.logger.info("Function 9: Download a 5MB document into Contract folder")

        # start timer
        time.sleep(2)
        page.screen_capture("-f9-time_mark_start.png")
        start = datetime.datetime.now()
        self.logger.info("Time mark start: " + str(start))
        page.click_retrieve_button()

        # stop timer
        end = page.get_downloaded_file(FilePath.DOWNLOAD_FOLDER_PATH)
        loading_time = round((end - start).seconds + (end - start).microseconds / 1e6, 2)
        self.logger.info("Time mark stop: "+str(end)+"\nFunction 9 loading time: "+str(loading_time)+"\n")

        page.click_delete_button()
        page.driver.close()
        page.switch_to_windows(0)

        return loading_time

    def function_KM(self):
        # set the instance
        page = ExtranetKMPage(self.driver, self.folder_path, self.curr_time, self.logger)
        self.logger.info("Function KM: Download a KM document file")

        page.goto_top_menu(4)
        time.sleep(2)
        page.click_DCD_CONTRACTOR_ACCESS_DOCUMENT_1()

        #start timer
        time.sleep(6)
        page.screen_capture("-f-KM-time_mark_start.png")
        start = datetime.datetime.now()
        self.logger.info("Time mark start: " + str(start))
        page.click_DCD_CONTRACTOR_ACCESS_DOCUMENT_1_EXCEL_1()

        # stop timer
        end = page.get_downloaded_file(FilePath.DOWNLOAD_FOLDER_PATH)
        loading_time = round((end - start).seconds + (end - start).microseconds / 1e6, 2)
        self.logger.info("Time mark stop: "+str(end)+"\nFunction KM loading time: "+str(loading_time)+"\n")

        page.log_out()

        return loading_time

