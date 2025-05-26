# Python 代码练习场 (Python Playground)

一个基于网页的 Python 代码练习环境，支持代码格式化和执行功能。

## 功能特点

- 现代化的网页界面
  - 使用 Ace 编辑器，支持语法高亮
  - 响应式设计，适配各种屏幕尺寸
  - 清晰的代码编辑和输出分区

- 代码格式化
  - 使用 Black 格式化工具
  - 一键格式化 Python 代码
  - 实时反馈格式化结果

- 代码执行
  - 在线运行 Python 代码
  - 实时显示程序输出
  - 友好的错误提示

- 其他功能
  - 清除输出按钮
  - 默认示例代码
  - 错误信息高亮显示

## 环境配置

1. 安装依赖包：
```bash
pip install -r requirements.txt
```

2. 启动服务器：
```bash
python main.py
```

3. 打开浏览器访问：`http://localhost:8000`

## 使用说明

1. 代码编辑：
   - 在左侧编辑器中输入或粘贴 Python 代码
   - 支持语法高亮和自动缩进

2. 代码格式化：
   - 点击"Format Code"按钮格式化代码
   - 使用 Black 格式化工具进行标准化格式化
   - 格式化结果会直接更新在编辑器中

3. 代码执行：
   - 点击"Run Code"按钮执行当前代码
   - 程序输出显示在右侧面板
   - 如有错误会显示详细的错误信息

4. 输出管理：
   - 使用"Clear"按钮清除输出内容
   - 输出面板支持滚动查看长内容

## 技术栈

- 后端：
  - FastAPI (Python Web 框架)
  - Black (Python 代码格式化工具)
  - Uvicorn (ASGI 服务器)

- 前端：
  - Ace Editor (代码编辑器)
  - TailwindCSS (样式框架)
  - 原生 JavaScript