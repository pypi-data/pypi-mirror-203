# coding: utf-8

import os

class DefaultConfig(object):

    def __init__(self):
        self._auth_token = None

    @property
    def auth_token(self):
        return self._auth_token

class EnvConfig(DefaultConfig):

    def __init__(self):
        super(EnvConfig, self).__init__()
        self._auth_token = os.environ.get('DS_AUTH_TOKEN')
        self._db_conn = {'db_host': str(os.environ.get('DB_HOST')) if os.environ.get('DB_HOST') else os.environ.get('DB_HOST_'),
                         'db_port': str(os.environ.get('DB_PORT')) if os.environ.get('DB_PORT') else os.environ.get('DB_PORT_'),
                         'db_user': os.environ.get('APP_KEY'),
                         'db_password': os.environ.get('APP_SECRET')}
        self._db_info = str(os.environ.get("DB_INFO_HOST")) if os.environ.get("DB_INFO_HOST") else os.environ.get("DB_INFO_HOST_")