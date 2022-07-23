import pandas as pd

from main.utils.ConfigUtil import ConfigUtil


class OpenSrcDataImporter:
    def __init__(self, company_category):
        basic_sentence = '公司登記(依營業項目別)－'
        config = ConfigUtil()
        self.category = company_category
        self.path = config.get_config('basic_path') + basic_sentence + company_category + '.csv'

    def read_csv(self, path):
        print(path)
        df = pd.read_csv(path)
        return df

    def save_to_mongo(self):
        print('save process ....')

    def process_flow(self):
        company_df = self.read_csv(self.path)
        print(company_df.to_string())


if __name__ == '__main__':
    category = '室內裝潢'
    importer = OpenSrcDataImporter(category)
    importer.process_flow()



