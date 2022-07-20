# -*- coding: utf8 -*-
import os
import pdb
import sys
import pytz
import time
import datetime
import logging
import logging.handlers


# from utils.logger import Logger
# Logger.info( "Congito User Pool Size:  {}".format(len(email_pool)))

class Logger(object):
    # Disable matplotlib debug messages
    logging.getLogger('matplotlib').setLevel(logging.WARNING)

    strftime_format = "%y-%m-%d %H:%M:%S"
    dt = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC).astimezone(pytz.timezone("Asia/Taipei")).strftime(
        strftime_format)
    display_format = '%(asctime)-2s %(process)d %(levelname)-2s %(message)s'
    logging.basicConfig(level=logging.INFO, format=display_format, datefmt=dt)

    logger = logging.getLogger(__name__)

    @classmethod
    def info(cls, message):
        cls.logger.info("{}".format(message))

    @classmethod
    def warn(cls, message):
        cls.logger.warn("{}".format(message))

    @classmethod
    def debug(cls, message):
        cls.logger.debug("{}".format(message))

    @classmethod
    def error(cls, message):
        cls.logger.error("{}".format(message))
