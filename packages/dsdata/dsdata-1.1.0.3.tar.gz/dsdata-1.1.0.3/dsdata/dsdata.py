# coding: utf-8

from __future__ import absolute_import

import pandas as pd
import requests
import json
import os
import time
import logging
import jaydebeapi
from typing import List, Optional
from dsdata.client.api import RestApiClient
from dsdata.config import EnvConfig
from dsdata.models.dataset import LocalDataset, QueryData
from dsdata.util import query_iterator

logging.basicConfig(format='[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d %(levelname)s] %(message)s',
                    level=logging.INFO)
logging.root.setLevel(logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DsData(object):
    """统一DS数据对象
    """
    def __init__(self, config=None):
        self._config = config or EnvConfig()
        self.api_client = RestApiClient(self._config)

    def load_dataset(self, dataset_url, size, chunksize):
        """根据设置返回数据集或迭代器
        :param dataset_key: 唯一标识数据集URI
        :param size: 获取数据量行数，默认上限一百万行
        :param chunksize: 默认返回获取的DataFrame全量数据，设置后返回一个 JsonReader，每次迭代读取chunksize大小的数据
        :return:
        """

        if (size is not None) and (not isinstance(size, int)):
            raise ValueError("size参数类型错误")

        if (not size) or size > 1000000:
            size = 1000000

        if (chunksize is not None) and (not isinstance(chunksize, int)):
            raise ValueError("chunksize参数类型错误")

        if chunksize and chunksize<=0:
            raise ValueError("chunksize必须为正整数")

        if chunksize and chunksize > size:
            raise ValueError("chunksize必须小于等于size")

        data_str, data_li = self.api_client.download_dataset(dataset_url, size, chunksize)

        # 返回迭代对象
        if chunksize:
            local_dataset = pd.read_json(data_str, chunksize=chunksize, lines=True)
            return local_dataset

        # 返回全量LocalDataset对象，封装了DataFrame
        return LocalDataset(data_li)

    def upload_object_tags(self, tags_upload_url, object_tags):
        """上传主体外部标签
        :param tags_upload_uri: 唯一标识标签上传资源URI
        :param object_tags: 外部标签object
        :return:
        """
        return self.api_client.upload_object_tags(tags_upload_url, object_tags)

    def load_metrics(self, metrics_def_url: str, sql: str, columns: Optional[List[str]], chunksize: Optional[int]):
        if 'https://' not in metrics_def_url and 'http://' not in metrics_def_url:
            metrics_def_url = os.environ.get('DS_API_HOST') + metrics_def_url
        logging.info('metrics_url: {}, sql: {}, columns: {}, chunksize: {}'.format(metrics_def_url, sql, columns, chunksize))

        token_time = os.environ.get('TOKEN_TIME')
        if int(time.time()) > (int(token_time) + 7199):
            raise ValueError("token已过期，请重新初始化")
        # 表定义
        try:
            requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
            s = requests.session()
            s.keep_alive = False  # 关闭多余连接
            response_table_info = requests.post(metrics_def_url, headers={'token': self._config.auth_token})
        except Exception as e:
            logging.error(e)
            raise ValueError('请求指标定义接口失败')

        metrics_info = json.loads(response_table_info.content)
        if 'payload' not in metrics_info and 'msg' not in metrics_info:
            raise ValueError("appkey或appSecret错误，token验证失败，获取数据表定义失败")
        elif 'payload' not in metrics_info and 'msg' in metrics_info:
            raise ValueError("获取数据表定义失败, 数据表定义接口返回：{}".format(metrics_info['msg']))
        elif ('payload' in metrics_info) and (metrics_info['payload'] == None):
            raise ValueError("获取数据表定义失败, 数据表定义接口返回：{}".format(metrics_info['msg']))
        else:
            metrics_info = metrics_info['payload']

        # # db连接参数
        # con = create_engine('mysql+pymysql://{}:{}@{}:{}'.format(self._config._db_conn['db_user'],
        #                                                          parse.quote_plus(self._config._db_conn['db_password']),
        #                                                          self._config._db_conn['db_host'],
        #                                                          self._config._db_conn['db_port']))
        PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
        # print(PROJECT_ROOT_PATH)
        conn_params = {'jdbc_driver': 'com.deepexi.datasense.jdbc.DataSenseDriver',
                       'url': 'jdbc:datasense://{}:{}'.format(self._config._db_conn['db_host'], self._config._db_conn['db_port']),
                       'user': self._config._db_conn['db_user'],
                       'password': self._config._db_conn['db_password'],
                       'jdbc_path': PROJECT_ROOT_PATH + '/datasense-jdbc-client.jar'}
        # 获取数据库名
        # print('token: ', self._config.auth_token)
        try:
            response_database_info = requests.get(self._config._db_info, headers={'token': self._config.auth_token})
        except Exception as e:
            logging.error(e)
            raise ValueError('请求数据库名接口失败')
        database = json.loads(response_database_info.content)
        if 'payload' in database:
            database = database['payload']
            database_name = database[0]['name']
        else:
            if 'msg' in database:
                raise ValueError("获取数据库名失败，数据库名接口返回：{}".format(database['msg']))
            else:
                raise ValueError("appkey或appSecret错误，token验证失败，获取数据库名失败")
        # sql校验，仅支持查询
        if 'create ' in sql.lower() or 'alter ' in sql.lower() or 'drop ' in sql.lower() or \
                'truncate ' in sql.lower() or 'insert into ' in sql.lower() or \
                'delete ' in sql.lower() or 'update ' in sql.lower():
            raise ValueError("仅支持select语句或单个表名，无权进行插入/更新/删除")
        # metrics = pd.read_sql(sql, con, columns, chunksize)
        # sql语句并不是一个表名
        if 'select ' in sql.lower() and 'from ' in sql.lower():
            sql_key_list = sql.split(' ')
            for index, sql_str in enumerate(sql_key_list):
                if sql_str.lower() == 'from':
                    sql_key_list[index + 1] = database_name + '.' + sql_key_list[index + 1]
                    break
            sql = ' '.join(sql_key_list)
        # sql语句为单独一个表名，同时给出查询列名
        elif columns != None and len(columns) > 0:
            sql = 'select ' + ', '.join(columns) + ' from ' + database_name + '.' + sql
        else:
            raise ValueError("不符合sql语句规范")
        try:
            conn = jaydebeapi.connect(conn_params['jdbc_driver'],
                                      conn_params['url'],
                                      [conn_params['user'], conn_params['password']],
                                      conn_params['jdbc_path'])
            curs = conn.cursor()
            curs.execute(sql)
            column_name = [col[0] for col in curs.description]
            if chunksize:
                # metrics_df = query_iterator(curs, column_name=column_name, chunksize=chunksize)
                metrics_df = pd.read_sql(sql, con=conn, columns=columns, chunksize=chunksize)
            else:
                metrics = curs.fetchall()
                # 返回全量dataframe
                metrics_df = pd.DataFrame(list(metrics), columns=column_name)
            return QueryData(metrics_df, metrics_info)
        except Exception as e:
            logging.error(e)

    def load_objects(self, object_def_url: str, sql: str, columns: Optional[List[str]], chunksize: Optional[int]):
        if 'https://' not in object_def_url and 'http://' not in object_def_url:
            object_def_url = os.environ.get('DS_API_HOST') + object_def_url
        logging.info('metrics_url: {}, sql: {}, columns: {}, chunksize: {}'.format(object_def_url, sql, columns, chunksize))

        token_time = os.environ.get('TOKEN_TIME')
        if int(time.time()) > (int(token_time) + 7199):
            raise ValueError("token已过期，请重新初始化")
        # 表定义
        try:
            requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
            s = requests.session()
            s.keep_alive = False  # 关闭多余连接
            response_table_info = requests.post(object_def_url, headers={'token': self._config.auth_token})
        except Exception as e:
            logging.error(e)
            raise ValueError('请求主体定义接口失败')
        object_info = json.loads(response_table_info.content)
        if 'payload' not in object_info and 'msg' not in object_info:
            raise ValueError("appkey或appSecret错误，token验证失败，获取数据表定义失败")
        elif 'payload' not in object_info and 'msg' in object_info:
            raise ValueError("获取数据表定义失败, 数据表定义接口返回：{}".format(object_info['msg']))
        elif ('payload' in object_info) and (object_info['payload'] == None):
            raise ValueError("获取数据表定义失败, 数据表定义接口返回：{}".format(object_info['msg']))
        else:
            object_info = object_info['payload']

        # # db连接参数
        # con = create_engine('mysql+pymysql://{}:{}@{}:{}'.format(self._config._db_conn['db_user'],
        #                                                          parse.quote_plus(self._config._db_conn['db_password']),
        #                                                          self._config._db_conn['db_host'],
        #                                                          self._config._db_conn['db_port']))
        PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
        conn_params = {'jdbc_driver': 'com.deepexi.datasense.jdbc.DataSenseDriver',
                       'url': 'jdbc:datasense://{}:{}'.format(self._config._db_conn['db_host'], self._config._db_conn['db_port']),
                       'user': self._config._db_conn['db_user'],
                       'password': self._config._db_conn['db_password'],
                       'jdbc_path': PROJECT_ROOT_PATH + '/datasense-jdbc-client.jar'}
        # 获取数据库名
        try:
            response_database_info = requests.get(self._config._db_info, headers={'token': self._config.auth_token})
        except Exception as e:
            logging.error(e)
            raise ValueError('请求数据库名接口失败')
        database = json.loads(response_database_info.content)
        if 'payload' in database:
            database = database['payload']
            database_name = database[0]['name']
        else:
            if 'msg' in database:
                raise ValueError("获取数据库名失败，数据库名接口返回：{}".format(database['msg']))
            else:
                raise ValueError("appkey或appSecret错误，token验证失败，获取数据库名失败")
        # sql校验，仅支持查询
        if 'create ' in sql.lower() or 'alter ' in sql.lower() or 'drop ' in sql.lower() or \
                'truncate ' in sql.lower() or 'insert into ' in sql.lower() or \
                'delete ' in sql.lower() or 'update ' in sql.lower():
            raise ValueError("仅支持select语句或单个表名，无权进行插入/更新/删除")
        # metrics = pd.read_sql(sql, con, columns, chunksize)
        # sql语句并不是一个表名
        if 'select ' in sql.lower() and 'from ' in sql.lower():
            sql_key_list = sql.split(' ')
            for index, sql_str in enumerate(sql_key_list):
                if sql_str.lower() == 'from':
                    sql_key_list[index + 1] = database_name + '.' + sql_key_list[index + 1]
                    break
            sql = ' '.join(sql_key_list)
        # sql语句为单独一个表名，同时给出查询列名
        elif columns != None and len(columns) > 0:
            sql = 'select ' + ', '.join(columns) + ' from ' + database_name + '.' + sql
        else:
            raise ValueError("不符合sql语句规范")
        with jaydebeapi.connect(conn_params['jdbc_driver'],
                                conn_params['url'],
                                [conn_params['user'], conn_params['password']],
                                conn_params['jdbc_path']) as conn:
            with conn.cursor() as curs:
                # curs = conn.cursor()
                curs.execute(sql)
                column_name = [col[0] for col in curs.description]
                if chunksize:
                    # object_df = query_iterator(curs, column_name, chunksize)
                    object_df = pd.read_sql(sql, con=conn, columns=columns, chunksize=chunksize)
                else:
                    object = curs.fetchall()
                    # 返回全量dataframe
                    object_df = pd.DataFrame(list(object), columns=column_name)
                return QueryData(object_df, object_info)
