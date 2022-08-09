# unzip file and write basic infomation to db
import os
import zipfile

import yaml


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

    def unzip_file(self, path_to_zip_file: str, directory_to_extract_to: str):
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)

    def process(self):
        directory = os.fsencode(self.zip_path)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".zip"):
                file_path = self.zip_path + filename
                self.unzip_file(file_path, self.csv_path)
            else:
                continue


if __name__ == '__main__':
    process = UnzipFileProcess()
    process.process()
