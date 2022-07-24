from selenium.webdriver.common.by import By

from utils.Logger import Logger
from utils.ConfigUtil import ConfigUtil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class OpenDataCSVCrawler:
    def __init__(self):
        configutil = ConfigUtil()
        self.base_url = configutil.get_config('base_url')
        self.logger = Logger()


    def crawl(self):
        options = Options()
        options.add_argument("--disable-notifications")

        chrome = webdriver.Chrome('chromedriver', chrome_options=options)
        chrome.get(self.base_url)

        cate_company_by_items = chrome.find_element("id", "cate2")
        cate_company_other_info = chrome.find_element("id", "cate3")
        register_of_companies = chrome.find_element("id", "cate4")
        cate_company_by_region = chrome.find_element("id", "cate5")
        company_registration_stat = chrome.find_element("id", "cate5")

        # basic company data classified by business items
        cate1_li = cate_company_by_items.find_elements(By.TAG_NAME, "li")
        for li_item in cate1_li:
            # print(li_item.text)
            href_info = li_item.find_element(By.TAG_NAME, "a")
            link = href_info.get_attribute("href")
            print(link)

    def process_flow(self):
        Logger.info('process begin.....')
        self.crawl()


if __name__ == '__main__':
    crawler = OpenDataCSVCrawler()
    crawler.process_flow()
