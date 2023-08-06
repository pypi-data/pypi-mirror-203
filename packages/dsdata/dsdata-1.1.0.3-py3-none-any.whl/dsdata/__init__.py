# coding: utf-8

from __future__ import absolute_import
from dsdata.config import EnvConfig
from dsdata.dsdata import DsData
import os
import requests
import time
import json

__version__ = '1.0.0'

def _get_instance():
    instance = DsData(config=EnvConfig())

    return instance

class DsClient(object):

    def __init__(self, endpoint, app_key, app_secret):
        self.endpoint = endpoint
        self.app_key = app_key
        self.app_secret = app_secret
        self._get_token(self.endpoint, self.app_key, self.app_secret)

    def _get_token(self, endpoint, app_key, app_secret):
        """
        获取access_token
        """
        if 'https://' not in endpoint or 'http://' not in endpoint:
            url = endpoint + '/api-service/oauth/token'
        else:
            raise ValueError('endpoint参数异常')

        query = {"appKey": app_key, "appSecret": app_secret, "grant_type": "application"}

        r = requests.post(url, params=query, headers={})
        if 'error' in r.json()["payload"]:
            raise ValueError(r.json()['msg'])

        token_time = int(time.time())
        token = r.json()["payload"]["access_token"]

        try:
            db_info = requests.get(endpoint + '/api-service/jdbc/client/info', headers={'token': token})
        except Exception as e:
            print(e)
            raise ValueError('请求数据库连接信息接口失败')
        db_info = json.loads(db_info.content)
        if db_info.get('code') and str(db_info['code']) == '200':
            db_host = db_info['payload']['jdbcClientIp']
            db_port = db_info['payload']['jdbcClientPort']
            db_info_host = endpoint + '/api-service/jdbc/database/info'
        else:
            if 'msg' in db_info:
                raise ValueError('请求数据库连接信息接口失败，错误信息：{}'.format(db_info['msg']))
            else:
                raise ValueError('请求数据库连接信息接口失败')

        # os.environ.setdefault('TOKEN_TIME', str(token_time))
        # os.environ.setdefault('DS_AUTH_TOKEN', token)
        # os.environ.setdefault('DS_API_HOST', endpoint)
        # os.environ.setdefault('APP_SECRET', app_secret)
        # os.environ.setdefault('APP_KEY', app_key)
        # os.environ.setdefault('DB_HOST_', db_host)
        # os.environ.setdefault('DB_PORT_', db_port)
        # os.environ.setdefault('DB_INFO_HOST_', db_info_host)

        os.environ['TOKEN_TIME'] = str(token_time)
        os.environ['DS_AUTH_TOKEN'] = token
        os.environ['DS_API_HOST'] = endpoint
        os.environ['APP_SECRET'] = app_secret
        os.environ['APP_KEY'] = app_key
        os.environ['DB_HOST_'] = db_host
        os.environ['DB_PORT_'] = db_port
        os.environ['DB_INFO_HOST_'] = db_info_host

    def load_dataset(self, dataset_url, size=None, chunksize=None):
        """获取DS数据集
        :param dataset_key: 唯一标识数据集URI
        :param size: 获取数据量行数，默认上限一百万行
        :param chunksize: 默认返回获取的DataFrame全量数据，设置后返回一个 JsonReader，每次迭代读取chunksize大小的数据
        :return:
        Examples
        --------
        # 生成全量DataFrame
        >>> from dsdata import DsClient
        >>> ds = DsClient(endpoint, app_key, app_secret)
        >>> data_dataframe = ds.load_dataset(dataset_url).dataframe

        # 设置chunksize生成可迭代JsonReader对象
        >>> from dsdata import DsClient
        >>> ds = DsClient(endpoint, app_key, app_secret)
        >>> data_dataframe = ds.load_dataset(dataset_url, size, chunksize)
        >>> for v in data_dataframe:
        >>>    print(v)
        """
        return _get_instance().load_dataset(dataset_url, size, chunksize)

    def upload_object_tags(self, tags_upload_url, object_tags):
        """上报自定义主体标签
        :param tags_upload_uri: 动态接口URL资源
        :param object_tags: 包含object_id、tag_code和tag_values列表对象
        :return:

        Examples
        --------
        # 上传主体外部标签
        >>> from dsdata import DsClient
        >>> ds = DsClient(endpoint, app_key, app_secret)
        >>> msg, valid_nums = ds.upload_object_tags(tags_upload_url, tags)
        """
        return _get_instance().upload_object_tags(tags_upload_url, object_tags)

    def load_metrics(self, metrics_def_url, sql, columns=[], chunksize=None):
        """获取指标主题数据和定义
        :param metrics_def_uri:
        :param sql:
        :param columns:
        :param chunksize:
        :return:
        """
        if not isinstance(columns, list):
            raise ValueError("参数columns，应为List[str]类型")
        return _get_instance().load_metrics(metrics_def_url, sql, columns, chunksize)

    def load_objects(self, object_def_url, sql, columns=[], chunksize=None):
        """获取主体数据和定义
        :param object_def_uri:
        :param sql:
        :param columns:
        :param chunksize:
        :return:
        """
        if not isinstance(columns, list):
            raise ValueError("参数columns，应为List[str]类型")
        return _get_instance().load_objects(object_def_url, sql, columns, chunksize)