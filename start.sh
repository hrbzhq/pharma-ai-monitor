#!/bin/bash

echo "🚥 Pharma AI Monitor startup script"
echo "=================================="

# Check Python version
python_version=$(python --version 2>&1)
echo "Python版本: $python_version"

# Check virtualenv
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "✅ 虚拟环境: $VIRTUAL_ENV"
else
    echo "⚠️  未检测到虚拟环境，建议使用虚拟环境"
fi

# Install dependencies
echo ""
echo "📦 检查并安装依赖..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ 依赖安装失败，请检查错误信息"
    exit 1
fi

echo "✅ 依赖安装成功"

echo ""
echo "🚀 启动服务器..."
echo "📡 访问地址: http://localhost:5000"
echo "⛔ 按 Ctrl+C 停止服务"
echo ""

# Start server
python standalone_server.py
