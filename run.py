from BPU_speed_measure import *
from utils.setup import *
from utils.operations import *


# Initial the WebDriver using the options from setup.py
driver = webdriver.Chrome(options=BrowserOptions.OPTIONS)

# Initial the all operation class instance from operation.py
testing_time = TimeOPs()
testing_log = LogOPs(FilePath.LOGS_FOLDER_PATH, testing_time, 'utf-8', logging.INFO, logging.INFO)
testing_logger = testing_log.get_logger()
testing_file = FileOPs()
testing_excel = ExcelOPs()

# Initial the list to store the BPU speed measure results
FUNCTIONS_LOADING_TIME = [1,1,1,1,1]

# create the folder to store the screencaptures
testing_file.create_folder(FilePath.SCREENCAPTURE_FOLDER_PATH+testing_time.return_format_YYYYMMDD_hyphen_HHMM())

# Below are the intranet part (function 1-5)
driver.get(Url.INTRANET_URL)
intranet_test = BPUSpeedMeasure(driver,
                                FilePath.SCREENCAPTURE_FOLDER_PATH+testing_time.return_format_YYYYMMDD_hyphen_HHMM(),
                                testing_time.return_format_YYYY_slash_MM_slash_DD(),
                                testing_logger)

intranet_test.wait_user_manually_login()
# log_in(driver, "bputester")
FUNCTIONS_LOADING_TIME.append(intranet_test.function_1())
FUNCTIONS_LOADING_TIME.append(intranet_test.function_2())
FUNCTIONS_LOADING_TIME.append(intranet_test.function_3())
FUNCTIONS_LOADING_TIME.append(intranet_test.function_4())
FUNCTIONS_LOADING_TIME.append(intranet_test.function_5())

# Below are the extranet part (function 6 - KM)
driver.get(Url.EXTRANET_URL)
extranet_test = BPUSpeedMeasure(driver,
                                FilePath.SCREENCAPTURE_FOLDER_PATH+testing_time.return_format_YYYYMMDD_hyphen_HHMM(),
                                testing_time.return_format_YYYY_slash_MM_slash_DD(),
                                testing_logger)
extranet_test.wait_user_manually_login()
FUNCTIONS_LOADING_TIME.append(extranet_test.function_6())
FUNCTIONS_LOADING_TIME.append(extranet_test.function_7())
FUNCTIONS_LOADING_TIME.append(extranet_test.function_8())
FUNCTIONS_LOADING_TIME.append(extranet_test.function_9())
FUNCTIONS_LOADING_TIME.append(extranet_test.function_KM())

# Delete useless files
testing_file.delete_all_files_under(FilePath.DOWNLOAD_FOLDER_PATH)

# Below is the Excel operation part
original_workbook = testing_excel.load_original_workbook(FilePath.BPU_SPEED_MEASURE_EXCEL_PATH)
worksheet1 = testing_excel.get_worksheet(original_workbook, ExcelWorksheetName.worksheet1)
worksheet2 = testing_excel.get_worksheet(original_workbook, ExcelWorksheetName.worksheet2)

testing_excel.fill_monthly_bpu_speed_measure_record(worksheet1, worksheet2, FUNCTIONS_LOADING_TIME, testing_time)
testing_excel.fill_bpu_speed_measure_result(worksheet1, FUNCTIONS_LOADING_TIME, testing_time)

testing_excel.save_workbook(original_workbook, os.getcwd() + '\\BPU Speed Measure 2024.xlsx')
print("\nAll the tasks are completed, please check the result folder!")
print("Please go to ",os.getcwd(),"\logs to check the logs")
