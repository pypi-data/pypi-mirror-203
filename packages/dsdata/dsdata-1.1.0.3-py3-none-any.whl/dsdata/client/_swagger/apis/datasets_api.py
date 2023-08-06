# coding: utf-8

from __future__ import absolute_import
import os
import math
import json
from six import iteritems
import time
from ..configuration import Configuration
from ..api_client import ApiClient
from tqdm import tqdm


class DatasetsApi(object):
    """操作数据统一API.
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_dataset(self, dataset_key, size, chunksize,  **kwargs):
        """获取DS数据集, 一些预设配置参数
        """
        kwargs['_return_http_data_only'] = True
        return self.get_dataset_with_http_info(dataset_key, size, chunksize, **kwargs)

    def get_dataset_with_http_info(self, dataset_key, size, chunksize, **kwargs):
        """通过http获取数据
        """
        page = 1
        # init_size = 1
        all_params = ['page']
        all_params.append('_return_http_data_only')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "获取错误参数 '%s'"
                    " 执行get_dataset" % key
                )
            params[key] = val
        del params['kwargs']

        if not isinstance(size, int) or size==0:
            raise ValueError("page取值必须为正整数")

        collection_formats = {}

        path_params = {}


        query_params = {}

        if size != 1000000:
            if 'page' in params:
                query_params['page'] = params['page']
                query_params['size'] = size

        if chunksize:
            query_params['size'] = chunksize

        header_params = {}

        form_params = []


        local_var_files = {}

        body_params = {}

        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        token_time = os.environ.get('TOKEN_TIME')
        if int(time.time()) > (int(token_time) + 7199):
            raise ValueError("token已过期，请重新初始化")
        header_params['token'] = os.environ.get('DS_AUTH_TOKEN')

        auth_settings = ['oauth']

        # 获取数据集基础信息
        try:
            ret = self.api_client.call_api(dataset_key, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DatasetSummaryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content'),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
        except:
            raise RuntimeError('服务异常请重试')

        ret = json.loads(ret.data.decode())

        if not ret.get("payload"):
            raise ValueError(ret['msg'])
        # 单项查询
        if 'totalElements' not in ret['payload']:
            data_li = ret["payload"]
            data_str = json.dumps([data_li])
            data_li = json.dumps([data_li])

            return data_str, data_li
        # 列表查询
        else:
            data_li = ret["payload"]['content']
            total_elements = ret["payload"]["totalElements"]
            true_chunksize = ret["payload"]["size"]
            total_pages = ret["payload"]["totalPages"]

            if size and total_elements > size:
                total_pages = math.ceil(size / true_chunksize)
                query_params['size'] = true_chunksize
                offset = abs(size - total_pages * true_chunksize)

                if size < true_chunksize:
                    query_params['size'] = size
                    offset = 0
            else:
                total_pages = math.ceil(total_elements / true_chunksize)
                query_params['size'] = true_chunksize
                offset = abs(total_elements - total_pages * true_chunksize)

                if size < true_chunksize:
                    offset = 0
                    query_params['size'] = size

            if total_pages == 1:
                data_str = "\n".join(json.dumps(data) for data in data_li)
                data_li = json.dumps(data_li)

                return data_str, data_li

            # 通过分页获取数据
            for page in tqdm(range(2, total_pages + 1)):
                query_params['page'] = page
                try:
                    ret = self.api_client.call_api(dataset_key, 'GET',
                                                   path_params,
                                                   query_params,
                                                   header_params,
                                                   body=body_params,
                                                   post_params=form_params,
                                                   files=local_var_files,
                                                   response_type='DatasetSummaryResponse',
                                                   auth_settings=auth_settings,
                                                   callback=params.get('callback'),
                                                   _return_http_data_only=params.get('_return_http_data_only'),
                                                   _preload_content=params.get('_preload_content'),
                                                   _request_timeout=params.get('_request_timeout'),
                                                   collection_formats=collection_formats)
                except:
                    raise RuntimeError('服务异常请重试')

                ret = json.loads(ret.data.decode())
                if not ret.get("payload"):
                    raise ValueError("token过期请重新初始化")
                tmp = ret["payload"]['content']
                data_li.extend(tmp)
            # 转为分行字符串分块读入
            data_li = data_li[0:len(data_li) - offset]
            data_str = "\n".join(json.dumps(data) for data in data_li)
            data_li = json.dumps(data_li)

            return data_str, data_li


