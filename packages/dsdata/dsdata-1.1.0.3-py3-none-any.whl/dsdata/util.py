# coding: utf-8
from __future__ import absolute_import
import functools
import pandas as pd

try:
    import collections.abc as collections
    from collections.abc import Mapping
except ImportError:
    import collections
    from collections import Mapping

def query_iterator(result, columns, chunksize):
    """Return generator through chunked result set."""
    has_read_data = False
    while True:
        data = result.fetchmany(chunksize)
        # return data
        if not data:
            if not has_read_data:
                yield pd.DataFrame.from_records(
                    [], columns=columns
                )
            break
        else:
            has_read_data = True
            frame = pd.DataFrame.from_records(
                data, columns=columns
            )
            yield frame

class LazyLoadedDict(Mapping):
    """具有延迟加载值的自定义不可变字典实现
    """

    def __init__(self, lazy_loaded_items):
        self._dict = lazy_loaded_items

    @classmethod
    def from_keys(cls, keys, loader_func, type_hint=None):
        """LazyLoadedDict 的工厂方法`
        :param keys: 用于创建字典的键列表
        :param loader_func: 应用于所有键的功能
        :param type_hint: 预期类型
        """
        return cls({k: LazyLoadedValue(
            lambda k=k: loader_func, type_hint=type_hint) for k in keys})

    def __getitem__(self, item):
        return self._dict[item]()

    def __iter__(self):
        return iter(self._dict.keys())

    def __len__(self):
        return len(self._dict)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, repr(self._dict))

    def __str__(self):
        return str(self._dict)


class LazyLoadedValue(object):
    def __init__(self, loader_func, type_hint=None):
        self._loader_func = loader_func
        self._type_hint = type_hint

    def __call__(self, *args, **kwargs):
        return self._loader_func()

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ('<{}>'.format(self._type_hint)
             if self._type_hint is not None else repr(self._loader_func)))

    def __str__(self):
        return str(self())
