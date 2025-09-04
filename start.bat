@echo off
chcp 65001 >nul

echo 🚥 药企AI需求监控系统启动脚本
echo ==================================

:: 检查Python版本
python --version 2>nul
if errorlevel 1 (
    echo ❌ Python未安装或未加入到PATH
    echo 请安装Python 3.8+并添加到系统PATH
    pause
    exit /b 1
)

:: 检查虚拟环境
if defined VIRTUAL_ENV (
    echo ✅ 虚拟环境: %VIRTUAL_ENV%
) else (
    echo ⚠️  未检测到虚拟环境，建议使用虚拟环境
)

echo.
echo 📦 检查并安装依赖...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ 依赖安装失败，请检查错误信息
    pause
    exit /b 1
)

echo ✅ 依赖安装成功

echo.
echo 🚀 启动服务器...
echo 📡 访问地址: http://localhost:5000
echo ⛔ 按 Ctrl+C 停止服务
echo.

:: 启动服务器
python standalone_server.py

pause
