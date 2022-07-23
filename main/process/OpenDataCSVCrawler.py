from utils.Logger import Logger
from utils.ConfigUtil import ConfigUtil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class OpenDataCSVCrawler:
    def __init__(self):
        self.url = ConfigUtil.get_config('base_url')

    def process_flow(self):
        Logger.logger('process begin.....')


if __name__ == '__main__':
    crawler = OpenDataCSVCrawler()
    crawler.process_flow()
