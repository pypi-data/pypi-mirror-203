# coding: utf-8

from __future__ import absolute_import, division

import os
from dsdata.client import _swagger

class RestApiClient(object):
    """REST API client
    """
    def __init__(self, config):
        self._config = config

        self._host = os.environ.get('DS_API_HOST')
        swagger_client = _swagger.ApiClient(
            host=self._host,
            header_name='Authorization',
            header_value='Bearer {}'.format(self._config.auth_token))

        self._datasets_api = _swagger.DatasetsApi(swagger_client)
        self._upload_object_tags_api = _swagger.UploadObjectTagsApi(swagger_client)


    def download_dataset(self, dataset_uri, size, chunksize):
        """获取数据集
        """
        return self._datasets_api.get_dataset(dataset_uri, size, chunksize)

    def upload_object_tags(self, tags_upload_url, object_tags):
        """上传主体标签
        """
        return self._upload_object_tags_api.upload_object_tags(tags_upload_url, object_tags)

