from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import black
import traceback
from io import StringIO
import contextlib

# 主页视图
# 返回静态 HTML 页面
def index(request):
    """返回 Python Playground 的主页"""
    with open('playground/static/index.html') as f:
        return HttpResponse(f.read())

# 代码格式化视图
# @csrf_exempt 装饰器用于禁用 CSRF 保护，因为这是一个 API 端点
# @require_http_methods 装饰器限制只接受 POST 请求
@csrf_exempt
@require_http_methods(["POST"])
def format_code(request):
    """代码格式化接口
    
    接收 POST 请求，使用 black 库对 Python 代码进行格式化
    请求体格式：{"code": "Python代码字符串"}
    返回格式：{"formatted_code": "格式化后的代码"} 或 {"error": "错误信息"}
    """
    try:
        # 解析请求体中的 JSON 数据
        data = json.loads(request.body)
        code = data.get('code', '')
        # 使用 black 格式化代码，采用默认配置
        formatted_code = black.format_str(code, mode=black.Mode())
        return JsonResponse({"formatted_code": formatted_code})
    except Exception as e:
        # 捕获并返回格式化过程中的错误
        # 包含完整的错误堆栈信息，方便调试
        error_msg = str(e) + "\n" + traceback.format_exc()
        return JsonResponse({"error": error_msg}, status=400)

# 代码执行视图
# @csrf_exempt 装饰器用于禁用 CSRF 保护，因为这是一个 API 端点
# @require_http_methods 装饰器限制只接受 POST 请求
@csrf_exempt
@require_http_methods(["POST"])
def execute_code(request):
    """代码执行接口
    
    接收 POST 请求，在服务器端执行 Python 代码
    请求体格式：{"code": "Python代码字符串"}
    返回格式：{"output": "执行输出"} 或 {"error": "错误信息"}
    """
    try:
        # 解析请求体中的 JSON 数据
        data = json.loads(request.body)
        code = data.get('code', '')
        # 创建 StringIO 对象捕获标准输出
        output = StringIO()
        # 使用 contextlib.redirect_stdout 重定向标准输出到 StringIO
        with contextlib.redirect_stdout(output):
            # 在隔离的命名空间中执行代码
            # 只提供内置函数，不提供全局变量，确保代码执行的安全性
            exec(code, {"__builtins__": __builtins__}, {})
        return JsonResponse({"output": output.getvalue()})
    except Exception as e:
        # 捕获并返回执行过程中的错误
        # 包含完整的错误堆栈信息，方便调试
        error_msg = str(e) + "\n" + traceback.format_exc()
        return JsonResponse({"error": error_msg}) 