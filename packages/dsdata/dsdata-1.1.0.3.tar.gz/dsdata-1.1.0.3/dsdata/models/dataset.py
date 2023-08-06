# coding: utf-8

import pandas as pd
# from dsdata.util import LazyLoadedDict

class LocalDataset(object):
    """返回统一数据类型，方便后续扩展
    """

    def __init__(self, data):

        self._data = data

        # self.dataframes = LazyLoadedDict.from_keys(
        #     ['ds_dataset'],
        #     self._load_dataframe,
        #     type_hint='pandas.DataFrame')
        self.dataframe = self._load_dataframe()

    def _load_dataframe(self):
        """创建pandas.DataFrame数据

        """
        return pd.read_json(self._data)


class QueryData(object):
    """
    返回统一数据类型，方便后续扩展
    """
    def __init__(self, data, data_info):

        self.dataframe = data
        self.data_info = data_info

    def __repr__(self):
        return "QueryData: {dataframe: pd.Dataframe, data_info: dict}"