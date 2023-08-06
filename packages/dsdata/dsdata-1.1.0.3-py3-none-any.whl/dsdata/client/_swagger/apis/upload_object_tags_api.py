# coding: utf-8

from __future__ import absolute_import
import os
import time
from ..configuration import Configuration
from ..api_client import ApiClient
from six import iteritems
import json

class UploadObjectTagsApi(object):
    """上传数据统一API.
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def upload_object_tags(self, tags_upload_url, object_tags, **kwargs):
        """上传主体标签
        """
        kwargs['_return_http_data_only'] = True
        return self.upload_object_tags_with_http_info(tags_upload_url, object_tags, **kwargs)

    def upload_object_tags_with_http_info(self, tags_upload_url, object_tags, **kwargs):
        """通过http获取数据
               """
        if not isinstance(object_tags, dict) or "objects" not in object_tags:
            raise ValueError("object_tags参数有误")

        all_params = ['object_tags']
        all_params.append('_return_http_data_only')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        if 'object_tags' in params:
            body_params = params['object_tags']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])

        token_time = os.environ.get('TOKEN_TIME')
        if int(time.time()) > (int(token_time) + 7199):
            raise ValueError("token已过期，请重新初始化")
        header_params['token'] = os.environ.get('DS_AUTH_TOKEN')

        # Authentication setting
        auth_settings = ['oauth']

        # 获取数据集基础信息
        try:
            ret = self.api_client.call_api(tags_upload_url, 'POST',
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

        if ret.get("msg") == "系统异常":
            raise ValueError("object_tags参数格式错误")

        elif ret.get("msg") == 'ok' and ret.get('payload').get('valid_nums') == 0:
            raise ValueError("成功上传数为0，请检查参数是否为有效值")

        elif ret.get("msg") == '404 NOT_FOUND':
            raise ValueError("tags_upload_uri输入有误")

        elif not ret.get("payload"):
            raise ValueError(ret['msg'])

        return ret.get("msg"), ret.get('payload').get('valid_nums')
