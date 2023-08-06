# base_common_lib
常用的基础通用Lib集合

## 快速入门
1. 安装
``` shell script
pip install baselib
```

2. 创建日志文件
```python
from baselib.log import file_logger
# 生成 logger 对象，默认自定义了日期格式，以及按天做日志分割
logger = file_logger("文件路径+名称")

logger.info("info msg")
logger.debug("debug msg")
```

3. json文件读写，更新
```python
from baselib.json import JsonFile

# 获取json格式文件，当读取异常时返回空的dict
data = JsonFile.read("文件路径+名称")

# 写入json格式文件
JsonFile.write("文件路径+名称", data)

# 直接更新文件，不需要先调用read
JsonFile.update("文件路径+名称", {"1": 2})
```

4. 日期段计算 period （简化datetime的调用）
```python
from baselib.time import Period
# 获取近一个小时的起止时间
start_time, end_time = Period.get_recent_hour(1)

# 获取当前时间
now = Period.now()

# 将当前时间转换格式
now_str = Period.formate_datetime(now)
```
