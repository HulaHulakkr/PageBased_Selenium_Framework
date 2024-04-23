#!/usr/bin/env python
'''
This example demonstrates a simple use of pycallgraph.
'''
import argparse
import re

from pycallgraph2 import PyCallGraph
from pycallgraph2 import Config
from pycallgraph2.output import GraphvizOutput
from BPU_speed_measure import *
from utils.setup import *
from utils.operations import *
import datetime

#!/usr/bin/env python
'''
Runs a regular expression over the first few hundred words in a dictionary to
find if any words start and end with the same letter, and having two of the
same letters in a row.
'''



class RegExp(object):

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--grouped', action='store_true')
        conf = parser.parse_args()

        if conf.grouped:
            self.run('regexp_grouped.png', Config(groups=True))
        else:
            self.run('regexp_ungrouped.png', Config(groups=False))

    def run(self, output, config):
        graphviz = GraphvizOutput()
        graphviz.output_file = output
        self.expression = r'^([^s]).*(.)\2.*\1$'

        with PyCallGraph(config=config, output=graphviz):
            driver = webdriver.Chrome(options=BrowserOptions.OPTIONS)

            FUNCTIONS_LOADING_TIME = []

            # Below are the intranet part (function 1-5)
            driver.get(Url.INTRANET_URL)
            # wait_input(driver)
            log_in(driver, "bputester")

            intranet_test = BPUSpeedMeasure(driver, FilePath.SCREENCAPTURE_FOLDER_PATH,
                                            datetime.datetime.now().strftime("%Y%m%d-%H%M"))
            FUNCTIONS_LOADING_TIME.append(intranet_test.function_1())
            FUNCTIONS_LOADING_TIME.append(intranet_test.function_2())
            FUNCTIONS_LOADING_TIME.append(intranet_test.function_3())
            FUNCTIONS_LOADING_TIME.append(intranet_test.function_4())
            FUNCTIONS_LOADING_TIME.append(intranet_test.function_5())

            # driver.get(Url.EXTRANET_URL)
            # wait_input(driver)
            # extranet_test = BPUSpeedMeasure(driver, FilePath.SCREENCAPTURE_FOLDER_PATH, datetime.datetime.now().strftime("%Y%m%d-%H%M"))
            # FUNCTIONS_LOADING_TIME.append(intranet_test.function_6())
            # FUNCTIONS_LOADING_TIME.append(intranet_test.function_7())
            # FUNCTIONS_LOADING_TIME.append(intranet_test.function_8())
            # FUNCTIONS_LOADING_TIME.append(intranet_test.function_9())
            # FUNCTIONS_LOADING_TIME.append(intranet_test.function_KM())

            original_workbook = load_original_workbook(FilePath.BPU_SPEED_MEASURE_EXCEL_PATH)
            worksheet1 = get_worksheet(original_workbook, 'Speed Measure')
            fill_bpu_speed_measure_result(worksheet1, FUNCTIONS_LOADING_TIME, datetime.datetime.today())
            worksheet2 = get_worksheet(original_workbook, 'Working')
            fill_monthly_bpu_speed_measure_record(worksheet1, worksheet2, FUNCTIONS_LOADING_TIME,
                                                  datetime.datetime.today())
            save_workbook(original_workbook, FilePath.SCREENCAPTURE_FOLDER_PATH + '\\BPU Speed Measure 2024.xlsx')


if __name__ == '__main__':
    RegExp().main()
