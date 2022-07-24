import os
import time

from selenium.webdriver.common.by import By

from utils.Logger import Logger
from utils.ConfigUtil import ConfigUtil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class OpenDataCSVCrawler:
    def __init__(self):
        self.configutil = ConfigUtil()
        options = Options()
        options.add_argument("--disable-notifications")
        self.base_url = self.configutil.get_config('base_url')
        self.logger = Logger()
        self.chrome = webdriver.Chrome('chromedriver', chrome_options=options)
        self.download_path = self.configutil.get_config('download_path')

    def crawl(self):

        self.chrome.get(self.base_url)
        file_list = []
        # complete 5 types data csv category
        cate_company_by_items = self.chrome.find_element("id", "cate2")
        # cate_company_other_info = self.chrome.find_element("id", "cate3")
        # register_of_companies = self.chrome.find_element("id", "cate4")
        # cate_company_by_region = self.chrome.find_element("id", "cate5")
        # company_registration_stat = self.chrome.find_element("id", "cate5")
        # cates_list = [cate_company_by_items, cate_company_other_info, register_of_companies, cate_company_by_region,
        #               company_registration_stat]

        # test 1 category
        cates_list = [cate_company_by_items]

        for cates in cates_list:
            self.get_download_page(cates, file_list)

        return file_list

    # basic company data classified by business items
    def get_download_page(self, cates, file_list):
        cates_li = cates.find_elements(By.TAG_NAME, "li")
        options = Options()
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome('chromedriver', chrome_options=options)

        for li_item in cates_li:
            href_info = li_item.find_element(By.TAG_NAME, "a")
            file_name = href_info.text
            file_list.append(file_name)
            link = href_info.get_attribute("href")
            Logger.info('entry: ' + link)
            Logger.info(self.download_page_crawler(link, file_name, driver))
            time.sleep(1)

            # check if file download complete
            file_path = self.download_path + file_name + '.zip'
            self.check_file_exist(file_path)
        time.sleep(2)
        driver.close()
        return file_list

    def download_page_crawler(self, download_url, file_name, driver):

        driver.get(download_url)
        csv_button = driver.find_element(By.CLASS_NAME, "csv")
        csv_button.click()
        buttons = driver.find_element(By.CLASS_NAME, "ui-dialog-buttonset")
        download_button = buttons.find_element(By.CSS_SELECTOR, ".ui-button.ui-corner-all.ui-widget")
        download_button.click()

        return 'Download ' + file_name + ' success..............'

    # TODO: 優化 > db 架好後file name, path等直接寫入 raw data，後續讀db再移檔案
    def move_file(self, file_list):
        for file_name in file_list:
            try:
                save_path = self.configutil.get_config('save_path')
                file_path_from = self.download_path + file_name + '.zip'
                file_path_to = save_path + file_name + '.zip'
                os.replace(file_path_from, file_path_to)
                Logger.info('move file From: ' + file_path_from + 'TO: ' + file_path_to)
            except():
                Logger.info('file ' + file_name + ' did not exist, save to error db, need to check')
                # TODO:write file name to error db

    def check_file_exist(self, file_path):
        if os.path.exists(file_path):
            return True
        else:
            time.sleep(5)
            self.check_file_exist(file_path)

    def process_flow(self):
        Logger.info('process begin.....')
        file_list = self.crawl()
        self.move_file(file_list)
        self.chrome.close()


if __name__ == '__main__':
    crawler = OpenDataCSVCrawler()
    crawler.process_flow()
