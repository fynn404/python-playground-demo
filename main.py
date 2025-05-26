from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import black
import traceback
import sys
from io import StringIO
import contextlib

# 创建 FastAPI 应用实例
app = FastAPI(title="Python Playground")

# 挂载静态文件目录，用于服务前端文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 定义请求体模型
class CodeRequest(BaseModel):
    code: str

# 根路由，返回主页 HTML
@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html") as f:
        return f.read()

# 代码格式化接口
@app.post("/format")
async def format_code(request: CodeRequest):
    try:
        # 使用 black 格式化代码
        formatted_code = black.format_str(request.code, mode=black.Mode())
        return {"formatted_code": formatted_code}
    except Exception as e:
        # 捕获并返回格式化过程中的错误
        error_msg = str(e) + "\n" + traceback.format_exc()
        raise HTTPException(status_code=400, detail=error_msg)

# 代码执行接口
@app.post("/execute")
async def execute_code(request: CodeRequest):
    try:
        # 捕获标准输出
        output = StringIO()
        with contextlib.redirect_stdout(output):
            # 在安全的环境中执行代码
            exec(request.code, {"__builtins__": __builtins__}, {})
        return {"output": output.getvalue()}
    except Exception as e:
        # 捕获并返回执行过程中的错误
        error_msg = str(e) + "\n" + traceback.format_exc()
        return {"error": error_msg}

# 启动服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 