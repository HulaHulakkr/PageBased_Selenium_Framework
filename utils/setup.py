from selenium.webdriver.chrome.options import *
from selenium import webdriver
import os
import datetime

# Based script set up data stored here
class FilePath(object):
    BPU_SPEED_MEASURE_EXCEL_PATH = r'\\housing\projects\HOMES\HOMES HIR\BPU Performance Measure Result\BPU Speed Measure 2024.xlsx'
    DOWNLOAD_FOLDER_PATH = os.getcwd() +"\\result\download_files"
    SCREENCAPTURE_FOLDER_PATH = os.getcwd() + "\\result\\"
    LOGS_FOLDER_PATH = os.getcwd() + "\\logs"
class BrowserOptions(object):
    OPTIONS = Options()
    OPTIONS.add_argument('--offline')
    OPTIONS.add_argument('--avoid-stats	')
    # OPTIONS.add_argument("--headless")  # Runs Chrome in headless mode.
    OPTIONS.add_argument('--no-sandbox')  # Bypass OS security model
    OPTIONS.add_argument('disable-infobars')
    OPTIONS.add_argument('disable-features=DownloadUI')
    OPTIONS.add_argument("--safebrowsing-disable-download-protection")
    # options.add_argument("--start-fullscreen")
    OPTIONS.add_argument('--disable-gpu')
    OPTIONS.add_argument('--incognito')
    OPTIONS.add_experimental_option("prefs", {
        "download.default_directory": FilePath.DOWNLOAD_FOLDER_PATH,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        "profile.default_content_setting.popups": 0
    })


class Function_4_input_content(object):
    SUBJECT = "Regular performance measure"
    ISSUED_BY = "bputester"
    ADDRESSED_TO = "bputester2"
    DOCUMENT_DATE = datetime.datetime.today().strftime("%d/%m/%Y")
    FILE_INPUT = os.getcwd()+"\data\\5MB.doc"

class Function_8_input_content(object):
    DOCUMENT_TITTLE = "Testing"
    DOCUMENT_DATE = datetime.datetime.today().strftime("%d/%m/%Y")
    FILE_INPUT = os.getcwd()+"\data\\5MB.doc"

class ExcelWorksheetName(object):
    worksheet1 = 'Speed Measure'
    worksheet2 = 'Working'

"""
Below is for debug only

accounts = {"Account_name": "Password",
            }
def get_password(account):
    try:
        return accounts[account]
    except:
        print("\nUser %s is not defined, enter a valid user.\n" % account)

def log_in(driver, account):
    driver.find_element(By.ID, "username").send_keys(account)
    driver.find_element(By.ID, "password").send_keys(get_password(account))
    driver.find_element(By.XPATH, "//*[@id='content-container']/div[2]/form/div[4]/input").click()
"""
class Url(object):
    INTRANET_URL = "https://@Account:Password@hom.int.housingauthority.gov.hk/.HOMES_WEB/index.do"
    # INTRANET_URL = "https://@Account:Password@hom.int.housingauthority.gov.hk/.HOMES_WEB/index.do"
    EXTRANET_URL = "https://hom.housing.gov.hk/.HOMES_WEB/index.do"
