# coding: utf-8

from __future__ import absolute_import

import urllib3

import sys
import os
import logging

from six import iteritems
from six.moves import http_client as httplib

def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class Configuration(object):
    def __init__(self):
        """
        Constructor
        """
        self.host = os.environ.get('DS_API_HOST')
        self.api_client = None
        self.temp_folder_path = None
        self.api_key = {}
        self.api_key_prefix = {}
        self.username = ""
        self.password = ""
        self.access_token = ""
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("_swagger")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        self.logger_stream_handler = None
        self.logger_file_handler = None
        self.logger_file = None
        self.debug = False
        self.verify_ssl = True
        self.ssl_ca_cert = None
        self.cert_file = None
        self.key_file = None
        self.proxy = None
        self.safe_chars_for_path_param = ''

    @property
    def logger_file(self):
        """获取日志文件.
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """设置日志文件
        """
        self.__logger_file = value
        if self.__logger_file:
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """获取debug状态
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """
        """
        self.__debug = value
        if self.__debug:
            for _, logger in iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            httplib.HTTPConnection.debuglevel = 1
        else:
            for _, logger in iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        """
        """
        if self.api_key.get(identifier) and self.api_key_prefix.get(identifier):
            return self.api_key_prefix[identifier] + ' ' + self.api_key[identifier]
        elif self.api_key.get(identifier):
            return self.api_key[identifier]

    def get_access_token(self, access_token):
        if (access_token):
            return 'Bearer' + access_token

    def get_basic_auth_token(self):
        """
        """
        return urllib3.util.make_headers(basic_auth=self.username + ':' + self.password)\
                           .get('authorization')

    def auth_settings(self):
        """
        """
        return {

            'oauth':
                {
                    'type': 'oauth2',
                    'in': 'header',
                    'key': 'Authorization',
                    'value': self.get_access_token(self.access_token)
                },

        }

    def to_debug_report(self):
        """
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 1.0.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)
