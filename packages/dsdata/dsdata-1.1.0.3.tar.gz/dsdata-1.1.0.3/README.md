# sdk-py

dsdata 使用样例：

```
from dsdata import DsClient

endpoint = 'https://xxxx.com'
AppKey = 'xxx'
AppSecret = 'xxxx'
ds = DsClient(endpoint=endpoint, app_key=AppKey, app_secret=AppSecret)

# 测试获取主体数据和定义
data = ds.load_objects('/api-service/220sc/default/12334/objects-definitions',
                       'select * from object_lhc_product', columns=['subject_id'], chunksize=2)
# 测试获取指标主题和定义
data = ds.load_metrics('/api-service/220sc/default/12323/definitions',
                       'SELECT * FROM h5', columns=None, chunksize=2)
# 测试获取数据集
data = ds.load_dataset('/api-service/220sc/default/dataset-ms-test1', 20)
# 测试上传标签
tags = {"objects":[{'object_id':"3", 'tag_code':'tag_wbbq2', 'tag_values': 123}]}
msg, valid_nums = ds.upload_object_tags('/api-service/220sc/default/dsdata0830/tags-upload', tags)

```