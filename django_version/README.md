# Python Playground - Django 版本

这是一个基于 Django 的在线 Python 代码编辑器和执行环境。

## 功能特点

- 在线代码编辑
- Python 代码实时执行
- 代码格式化（使用 black）
- 完整的 Django 项目结构
- 内置管理界面

## 项目结构

```
django_version/
├── README.md                    # 项目说明文档
├── requirements.txt             # 项目依赖
├── manage.py                    # Django 管理脚本
├── playground/                  # 主应用目录
│   ├── views.py                # 视图函数
│   ├── urls.py                 # URL 配置
│   └── static/                 # 静态文件
│       └── index.html          # 前端页面
└── playground_project/         # 项目配置目录
    ├── settings.py            # 项目设置
    └── urls.py               # 项目 URL 配置
```

## 安装说明

1. 确保已安装 Python 3.x
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 初始化数据库：
   ```bash
   python manage.py migrate
   ```

## 运行说明

1. 在终端中进入 django_version 目录
2. 运行开发服务器：
   ```bash
   python manage.py runserver 8000
   ```
3. 打开浏览器访问：`http://localhost:8000`

## API 接口说明

### 1. 代码格式化
- 端点：`/format`
- 方法：POST
- 请求体：
  ```json
  {
    "code": "你的Python代码"
  }
  ```
- 返回：
  ```json
  {
    "formatted_code": "格式化后的代码"
  }
  ```

### 2. 代码执行
- 端点：`/execute`
- 方法：POST
- 请求体：
  ```json
  {
    "code": "你的Python代码"
  }
  ```
- 返回：
  ```json
  {
    "output": "代码执行输出"
  }
  ```

## 注意事项

1. 当前配置适用于开发环境，生产环境部署需要：
   - 修改 SECRET_KEY
   - 关闭调试模式（DEBUG = False）
   - 配置 ALLOWED_HOSTS
   - 使用生产级 WSGI 服务器（如 Gunicorn）
   - 配置静态文件服务（使用 Nginx 等）

2. 代码执行在服务器端进行，注意防范恶意代码

## 技术栈

- Django 5.0.2
- Black 24.2.0 