#### Config

config 存放文件夹，用于存放隐私信息 / 分离配置与实现。

#### 使用要求

{name}.json 对应任意路径下的 {name}.py 文件配置，在 {name}.py 内使用。

无需传入文件名，自动识别，返回 `class` 类型，支持 `.` 操作符。

```python
from extensions.load_config import load_config

config = load_config()

attribute1 = config.attribute1
attribute2 = config.attribute2
```

