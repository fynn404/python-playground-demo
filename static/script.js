// 初始化 Ace 编辑器
const editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");  // 设置编辑器主题
editor.session.setMode("ace/mode/python");  // 设置 Python 语法高亮
editor.setShowPrintMargin(false);  // 隐藏打印边距

// 设置默认的示例代码
editor.setValue(`def example_function(x):
    y = x + 1
    return y

result = example_function(5)
print(result)`, -1);

// 获取输出面板元素
const output = document.getElementById("output");

// 格式化代码功能
async function formatCode() {
    const code = editor.getValue();
    try {
        // 发送格式化请求到后端
        const response = await fetch("/format", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ code: code }),
        });

        if (!response.ok) {
            const error = await response.json();
            output.innerHTML = `<span class="error">代码格式化错误:\n${error.detail}</span>`;
            return;
        }

        const data = await response.json();
        editor.setValue(data.formatted_code, -1);  // 更新编辑器内容
        output.innerHTML = '<span class="success">代码格式化成功！</span>';
    } catch (error) {
        output.innerHTML = `<span class="error">错误: ${error.message}</span>`;
    }
}

// 运行代码功能
async function runCode() {
    const code = editor.getValue();
    try {
        // 发送执行请求到后端
        const response = await fetch("/execute", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ code: code }),
        });

        const data = await response.json();

        // 处理执行结果
        if (data.error) {
            output.innerHTML = `<span class="error">代码执行错误:\n${data.error}</span>`;
        } else {
            output.innerHTML = `<pre class="whitespace-pre-wrap">${data.output}</pre>`;
        }
    } catch (error) {
        output.innerHTML = `<span class="error">错误: ${error.message}</span>`;
    }
}

// 清除输出面板内容
function clearOutput() {
    output.innerHTML = '';
} 