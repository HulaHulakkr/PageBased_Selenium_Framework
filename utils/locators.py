from selenium.webdriver.common.by import By


# for maintainability we can separate web objects by page name

# Based elements used in base page
class TopMenuLocator(object):
    MENU_MAIN = (By.XPATH, "//*[@id='topMenu']/td/table/tbody/tr[1]/td/table/tbody/tr/td[3]")
    MENU_2 = (By.XPATH, "//*[@id='topMenu']/td/table/tbody/tr[1]/td/table/tbody/tr/td[6]")
    MENU_3 = (By.XPATH, "//*[@id='topMenu']/td/table/tbody/tr[1]/td/table/tbody/tr/td[9]")
    MENU_4 = (By.XPATH, "//*[@id='topMenu']/td/table/tbody/tr[1]/td/table/tbody/tr/td[12]")
    MENU_5 = (By.XPATH, "//*[@id='topMenu']/td/table/tbody/tr[1]/td/table/tbody/tr/td[15]")
    MENU_6 = (By.XPATH, "//*[@id='topMenu']/td/table/tbody/tr[1]/td/table/tbody/tr/td[18]")

class BasedButton(object):
    LOGOUT = (By.CLASS_NAME, "wpsToolBarLink")

# Intranet and Extranet shared in common part
class MainPageLocator(object):
    TASK_LIST = (By.XPATH, "//*[@id='mainMenu']/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a")
    TASK_LIST_TABLE = (By.ID, "index")

# Intranet Part (for function 1 - 5)
class IntranetMainPageLocator(MainPageLocator):

    FILE_CABINET = (By.XPATH, "//*[@id='mainMenu']/table/tbody/tr[21]/td/table/tbody/tr/td[2]/a")
    FILE_CABINET_LAYOUT_1 = (By.XPATH, "//*[@id='FolderTree_Layer_1']/table/tbody/tr[1]/td[1]/a")
    FILE_CABINET_LAYOUT_2 = (By.XPATH, "//*[@id='FolderTree_Layer_1']/table/tbody/tr[64]/td[1]/a")
    FILE_CABINET_LAYOUT_3 = (By.XPATH, "//*[@id='FolderTree_Layer_1']/table/tbody/tr[66]/td[1]/a")
    FILE_CABINET_LAYOUT_4 = (By.XPATH, "//*[@id='FolderTree_Layer_1']/table/tbody/tr[68]/td[1]/a")
    FILE_CABINET_UPDATE_DOCUMENT_BUTTON = (By.XPATH, "//*[@id='FolderTree_Layer_3']/table/tbody/tr[22]/td/table/tbody/tr/td[1]/input[1]")

    SUBJECT_BOX = (By.NAME, "docTitle")
    ISSUED_BY_BOX = (By.NAME, "from")
    ADDRESSED_TO_BOX = (By.NAME, "to")
    DOCUMENT_DATE_BOX = (By.NAME, "docDate")
    FILE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='FolderDocCreate']/table/tbody/tr/td[1]/table[2]/tbody/tr[9]/td/table/tbody/tr[1]/td[2]/input")

    UPDATE_DOCUMENT_ACKNOWLEDGEMENT = (By.XPATH, "//*[@id='collaboration']/tbody/tr[1]/td/p[1]")
    CLOSE_BUTTON = (By.XPATH, "//*[@id='collaboration']/tbody/tr[2]/td/input")

    TOP_DOCUMENT_SUBJECT = (By.XPATH, "//*[@id='FolderTree_Layer_3']/table/tbody/tr[2]/td[3]/a")
class IntranetProjectPageLocator(object):
    PROJECT_SEARCH = (By.XPATH, "//*[@id='mainMenu']/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a")
    PROJECT_SEARCH_BUTTON = (By.XPATH, "//*[@id='projectSearch']/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[16]/td/table/tbody/tr[3]/td[3]/div/input")

    PROJECT_SEARCH_RESULT_TABLE = (By.ID, "searchProjectsSaveSessionAction")
class IntranetKMPageLocator(object):
    KNOWLEDGE_REPOSITORY = (By.XPATH, "//*[@id='tr_2_wps.DCD.KnowledgeManagement.KRDoc.Group']/td/table/tbody/tr/td[2]")
    KR_BROWSE = (By.XPATH, "//*[@id='tr_3_wps.DCD.KnowledgeManagement.KRDoc.Browse']/td/table/tbody/tr/td[3]/a")
    KR_BROWSE_DCD_TOP_DOC = (By.XPATH, "//*[@id='resultInnerDiv1']/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/a")

    KM_DOC_TABLE = (By.ID, "maintTable")

# Extranet Part (for function 6 - KM)
class ExtranetMainPageLocator(MainPageLocator):
    aaa = (By.XPATH, "")

class ExtranetContractPageLocator(object):
    UN99NR = (By.XPATH, "//*[@id='myProjectsSaveSessionAction']/table/tbody/tr[3]/td/img")
    UN99NR_9999998 = (By.XPATH, "//*[@id='myProjectsSaveSessionAction']/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a[2]")
    BW = (By.XPATH, "//*[@id='tr_2_wps.DCD.Contract.SiteRecordBW']/td/table/tbody/tr/td[2]")
    BW_DAILY_REPORT = (By.XPATH, "//*[@id='tr_3_wps.DCD.Project.SiteRecord.DCD_HOMES_UF_STE_S092_1_DailyReport_BWSTR']/td/table/tbody/tr/td[3]/a")
    BW_DAILY_REPORT_NEW_BUTTON = (By.XPATH, "//*[@id='SiteDiaryList']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr/td[2]/input")
    BW_DAILY_REPORT_CLIP_IMAGE = (By.XPATH, "//*[@id='SiteDiarySubmit']/table/tbody/tr/td/table/tbody/tr[2]/td/table[2]/tbody/tr[4]/td[2]/button")

class ExtranetKMPageLocator(object):
    MATERIALS_DATABASE = (By.XPATH, "//*[@id='tr_2_wps.DCD.KnowledgeManagement.MtrlDoc.Group']/td/table/tbody/tr/td[2]")
    MATERIALS_BW = (By.XPATH, "//*[@id='tr_3_wps.DCD.KnowledgeManagement.MtrlDoc.Browse.BW_CNTR']/td/table/tbody/tr/td[3]/a")
    MATERIALS_BW_CLAC = (By.ID, "n_4050_text")
    MATERIALS_BW_CLAC_OTHERS = (By.ID, "n_4051_text")

    MATERIAL_DATABASE_DOC_TABLE = (By.ID, "go_to_page_button")

    DCD = (By.XPATH, "//*[@id='tr_2_wps.DCD.KnowledgeManagement.DCDAcademy']/td/table/tbody/tr/td[2]/a")
    DCD_CONTRACTOR_ACCESS = (By.XPATH, "//*[@id='tr_3_wps.DCD.KnowledgeManagement.DCDAcademy.DCD_HOMES_UF_DEP_S020_DCDACADEMY_CAC']/td/table/tbody/tr/td[3]")
    DCD_CONTRACTOR_ACCESS_DOCUMENT_1 = (By.XPATH, "//*[@id='docTable']/tr[2]/td[2]/table/tbody/tr[1]/td/a")
    DCD_CONTRACTOR_ACCESS_DOCUMENT_1_EXCEL_1 = (By.XPATH, "//*[@id='get_height']/tbody/tr/td/table/tbody/tr[9]/td[2]/font/table/tbody/tr[1]/td[1]/a/font")

# Attachment Window part (for function 8-9)
class AttachmentWindowLocator(object):
    # Below are function 8

    NEW_ATTACHMENT_BUTTON = (By.NAME, "addButton")

    DOCUMENT_TITTLE_BOX = (By.NAME, "docTitle")
    DOCUMENT_DATE_BOX = (By.NAME, "docDate")
    DOCUMENT_FILE_INPUT = (By.CSS_SELECTOR, "input[type='file']")

    CONFIRM_BUTTON = (By.XPATH, "//*[@id='proj1']/tbody/tr[2]/td/table/tbody/tr/td[2]/input")

    DELETE_BUTTON = (By.NAME, "deleteButton")

    # Below are function 9
    RETRIEVE_BUTTON = (By.NAME, "retrieveButton")
