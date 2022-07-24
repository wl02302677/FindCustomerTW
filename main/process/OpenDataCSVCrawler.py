import os

from selenium.webdriver import ActionChains
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

    def crawl(self):

        self.chrome.get(self.base_url)

        # 5 types data csv category
        cate_company_by_items = self.chrome.find_element("id", "cate2")
        cate_company_other_info = self.chrome.find_element("id", "cate3")
        register_of_companies = self.chrome.find_element("id", "cate4")
        cate_company_by_region = self.chrome.find_element("id", "cate5")
        company_registration_stat = self.chrome.find_element("id", "cate5")
        # cate1_li = cate_company_by_items.find_elements(By.TAG_NAME, "li")
        # for li_item in cate1_li:
        #     href_info = li_item.find_element(By.TAG_NAME, "a")
        #     link = href_info.get_attribute("href")
        #     Logger.info('entry: ' + link)
        #
        #     Logger.info(self.download_page_crawler(link))
        cates_list = [cate_company_by_items, cate_company_other_info, register_of_companies
            , cate_company_by_region, company_registration_stat]

        for cates in cates_list:
            self.get_download_page(cates)

    # basic company data classified by business items
    def get_download_page(self, cates):
        cates_li = cates.find_elements(By.TAG_NAME, "li")
        for li_item in cates_li:
            href_info = li_item.find_element(By.TAG_NAME, "a")
            file_name = href_info.text
            link = href_info.get_attribute("href")
            Logger.info('entry: ' + link)

            Logger.info(self.download_page_crawler(link, file_name))

    def download_page_crawler(self, download_url, file_name):
        options = Options()
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome('chromedriver', chrome_options=options)
        driver.get(download_url)
        # custom_table = chrome.find_element("class", "customTable")
        # print(custom_table.text)
        csv_button = driver.find_element(By.CLASS_NAME, "csv")
        csv_button.click()

        buttons = driver.find_element(By.CLASS_NAME, "ui-dialog-buttonset")
        # ActionChains(buttons).click("button").perform()
        # download_button = buttons.find_element(By.TAG_NAME, "button")
        download_button = buttons.find_element(By.CSS_SELECTOR, ".ui-button.ui-corner-all.ui-widget")
        download_button.click()
        driver.close()
        self.move_file(file_name)

        return 'Download success'

    def move_file(self, file_name):
        download_path = self.configutil.get_config('download_path')
        save_path = self.configutil.get_config('save_path')
        file_path_from = download_path + file_name + '.zip'
        file_path_to = save_path + file_name + '.zip'

        os.replace(file_path_from, file_path_to)

    def process_flow(self):
        Logger.info('process begin.....')
        self.crawl()


if __name__ == '__main__':
    crawler = OpenDataCSVCrawler()
    crawler.process_flow()
