pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup and Run') {
            steps {
                bat '''
                    @echo off
                    setlocal

                    :: 使用 Jenkins 提供的工作空间路径
                    set WORKSPACE=%WORKSPACE%
                    set VENV=%WORKSPACE%\\venv

                    echo ===== Creating virtual environment =====
                    python -m venv %VENV%
                    if %errorlevel% neq 0 (
                        echo Failed to create venv
                        exit /b %errorlevel%
                    )

                    echo ===== Upgrading pip =====
                    %VENV%\\Scripts\\python -m pip install --upgrade pip

                    echo ===== Installing requirements =====
                    if exist requirements.txt (
                        :: 使用国内镜像源并增加超时时间，避免网络问题
                        %VENV%\\Scripts\\pip install --timeout 100 --retries 5 -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
                        if %errorlevel% neq 0 (
                            echo Failed to install requirements
                            exit /b %errorlevel%
                        )
                    ) else (
                        echo requirements.txt not found, skipping
                    )

                    echo ===== Running run.py =====
                    %VENV%\\Scripts\\python run.py
                    if %errorlevel% neq 0 (
                        echo Script execution failed
                        exit /b %errorlevel%
                    )

                    echo Done.
                '''
            }
        }
    }

    post {
        success {
            echo 'Script executed successfully!'
        }
        failure {
            echo 'Script execution failed!'
        }
    }
}