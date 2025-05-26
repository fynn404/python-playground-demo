# Python Playground - Flask 版本

这是一个基于 Flask 的在线 Python 代码编辑器和执行环境。

## 功能特点

- 在线代码编辑
- Python 代码实时执行
- 代码格式化（使用 black）
- 简单轻量的实现

## 项目结构

```
flask_version/
├── README.md           # 项目说明文档
├── requirements.txt    # 项目依赖
├── app.py             # Flask 应用主文件
└── static/            # 静态文件目录
    └── index.html     # 前端页面
```

## 安装说明

1. 确保已安装 Python 3.x
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 运行说明

1. 在终端中进入 flask_version 目录
2. 运行应用：
   ```bash
   python app.py
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
   - 关闭调试模式
   - 使用生产级 WSGI 服务器（如 Gunicorn）
   - 配置适当的安全选项

2. 代码执行在服务器端进行，注意防范恶意代码

## 技术栈

- Flask 3.0.2
- Black 24.2.0 