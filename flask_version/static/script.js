// 初始化 Ace 编辑器
const editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");
editor.setShowPrintMargin(false);
editor.setValue(`# 在这里输入你的 Python 代码
print("Hello, World!")
`);

// 获取输出元素
const outputElement = document.getElementById('output');

// 运行代码
async function runCode() {
    const code = editor.getValue();
    try {
        const response = await fetch('/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: code })
        });
        const data = await response.json();

        if (data.error) {
            outputElement.innerHTML = `<span class="error">${data.error}</span>`;
        } else {
            outputElement.innerHTML = `<span class="success">${data.output}</span>`;
        }
    } catch (error) {
        outputElement.innerHTML = `<span class="error">Error: ${error.message}</span>`;
    }
}

// 格式化代码
async function formatCode() {
    const code = editor.getValue();
    try {
        const response = await fetch('/format', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: code })
        });
        const data = await response.json();

        if (data.error) {
            outputElement.innerHTML = `<span class="error">${data.error}</span>`;
        } else {
            editor.setValue(data.formatted_code);
            editor.clearSelection();
            outputElement.innerHTML = '<span class="success">代码已格式化</span>';
        }
    } catch (error) {
        outputElement.innerHTML = `<span class="error">Error: ${error.message}</span>`;
    }
}

// 清空输出
function clearOutput() {
    outputElement.innerHTML = '';
} 