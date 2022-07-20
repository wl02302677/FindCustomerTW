import os

import yaml


class ConfigUtil:
    def __init__(self):
        self.config_file = '../config/config.yaml'

    def get_config(self, att):

        if not os.path.exists(self.config_file):
            raise Exception("There is no configuration file '{}'".format(self.config_file))
        else:
            with open(self.config_file) as f:
                config = yaml.safe_load(f)

                return config[att]
