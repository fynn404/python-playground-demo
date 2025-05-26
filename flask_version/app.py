from flask import Flask, request, send_from_directory, jsonify
import black
import traceback
from io import StringIO
import contextlib

# 创建 Flask 应用实例
# 设置应用名称为 "Python Playground"
app = Flask(__name__)

# 根路由，返回主页 HTML
# 当用户访问根路径 "/" 时，返回 static 目录下的 index.html 文件
@app.route('/')
def root():
    return send_from_directory('static', 'index.html')

# 代码格式化接口
# 接收 POST 请求，使用 black 库对 Python 代码进行格式化
# 请求体格式：{"code": "Python代码字符串"}
# 返回格式：{"formatted_code": "格式化后的代码"} 或 {"error": "错误信息"}
@app.route('/format', methods=['POST'])
def format_code():
    try:
        # 从请求体中获取代码
        code = request.json.get('code', '')
        # 使用 black 格式化代码，采用默认配置
        formatted_code = black.format_str(code, mode=black.Mode())
        return jsonify({"formatted_code": formatted_code})
    except Exception as e:
        # 捕获并返回格式化过程中的错误
        # 包含完整的错误堆栈信息，方便调试
        error_msg = str(e) + "\n" + traceback.format_exc()
        return jsonify({"error": error_msg}), 400

# 代码执行接口
# 接收 POST 请求，在服务器端执行 Python 代码
# 请求体格式：{"code": "Python代码字符串"}
# 返回格式：{"output": "执行输出"} 或 {"error": "错误信息"}
@app.route('/execute', methods=['POST'])
def execute_code():
    try:
        # 从请求体中获取代码
        code = request.json.get('code', '')
        # 创建 StringIO 对象捕获标准输出
        output = StringIO()
        # 使用 contextlib.redirect_stdout 重定向标准输出到 StringIO
        with contextlib.redirect_stdout(output):
            # 在隔离的命名空间中执行代码
            # 只提供内置函数，不提供全局变量，确保代码执行的安全性
            exec(code, {"__builtins__": __builtins__}, {})
        return jsonify({"output": output.getvalue()})
    except Exception as e:
        # 捕获并返回执行过程中的错误
        # 包含完整的错误堆栈信息，方便调试
        error_msg = str(e) + "\n" + traceback.format_exc()
        return jsonify({"error": error_msg})

# 只有直接运行此文件时才启动服务器
if __name__ == '__main__':
    # 启动 Flask 开发服务器
    # host='0.0.0.0' 允许外部访问
    # port=8000 设置端口号
    # debug=True 启用调试模式，方便开发
    app.run(host='0.0.0.0', port=8000, debug=True) 