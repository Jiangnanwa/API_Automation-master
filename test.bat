@echo off
setlocal

set WORKSPACE=%~dp0
set VENV=%WORKSPACE%venv

echo ===== Creating virtual environment =====
python -m venv %VENV%
if %errorlevel% neq 0 (
    echo Failed to create venv
    exit /b %errorlevel%
)

echo ===== Upgrading pip =====
%VENV%\Scripts\python -m pip install --upgrade pip

echo ===== Installing requirements =====
if exist requirements.txt (
    %VENV%\Scripts\pip install --timeout 100 --retries 5 -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
) else (
    echo requirements.txt not found, skipping
)

echo ===== Running run.py =====
%VENV%\Scripts\python run.py

echo Done.
pause