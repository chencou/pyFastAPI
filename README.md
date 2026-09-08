# pyFastAPI
### 项目护初始化
预先[安装uv](https://docs.astral.sh/uv/getting-started/installation/) 在通过`uv`命令初始化项目安装`fastapi`
```
uv init pyFastAPI --bare
```
```
uv add "fastapi[standard]"
```
### 项目结构
基础项目结构
```
project/
├── database.py    # 引擎、会话工厂、get_db 依赖
├── models.py      # SQLModel 表模型（table=True）
├── schemas.py     # Pydantic 请求/响应模型（不设 table=True）
├── crud.py        # 增删改查逻辑
└── main.py        # FastAPI 路由
```


### 项目启动
创建 `main.py` 文件代码如下示例：
```python
from fastapi import FastAPI 

app = FastAPI()
```

文件路径传给 `fastapi dev` 命令，它会尝试推断要使用的 FastAPI 应用对象：
```
uv run fastapi dev main.py
```

或者 `pyproject.toml` 文件中配置 `[tool.fastapi]` 标签例如：
```
[tool.fastapi]
entrypoint = "main:app"
```
该 entrypoint 会告诉 fastapi 命令按如下方式导入应用：

代码框中 main 是导入创建文件 `main.py`
```python
from main import app
```


然后 `fastapi dev` 命令传入 `--entrypoint` 选项：
```
uv uf fastapi dev --entrypoint main:app
```

