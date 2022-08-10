# unzip file and write basic infomation to db
import os
import zipfile

import yaml
from pathlib import Path
from utils.Logger import Logger


class UnzipFileProcess:
    def __init__(self):
        config_file = '../config/config.yaml'
        if not os.path.exists(config_file):
            raise Exception("There is no configuration file '{}'".format(config_file))
        else:
            with open(config_file) as f:
                config = yaml.safe_load(f)
        self.zip_path = config['save_zip_path']
        self.csv_path = config['save_csv_path']

    def zip_file(self):
        return 'zip file done'

    def unzip_file(self, path_to_zip_file: str, directory_to_extract_to: str, zip_name:str):
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            for file_name in zip_ref.namelist():
                csv_name = zip_name.replace('zip', 'csv')
                extracted_path = Path(zip_ref.extract(file_name))
                # zipfile chinese decode problem, use zip file name replace
                extracted_path.rename(directory_to_extract_to + csv_name)

    def process(self):
        directory = os.fsencode(self.zip_path)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            file_path = self.zip_path + filename

            if filename.endswith(".zip"):
                self.unzip_file(file_path, self.csv_path, filename)
                Logger.info('unzip file: ' + file_path)
            else:
                Logger.info('this file type is not zip: ' + file_path)
                continue


if __name__ == '__main__':
    process = UnzipFileProcess()
    process.process()
