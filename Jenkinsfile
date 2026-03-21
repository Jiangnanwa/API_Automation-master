pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}\\venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                // 打印当前工作空间内容，确认代码已拉取
                bat 'echo Current directory: %cd% && dir'
            }
        }

        stage('Setup Environment') {
            steps {
                bat '''
                    echo ===== Checking Python =====
                    where python
                    python --version
                    
                    echo ===== Creating virtual environment =====
                    python -m venv %VENV%
                    if %errorlevel% neq 0 (
                        echo Failed to create venv
                        exit /b %errorlevel%
                    )
                    
                    echo ===== Upgrading pip =====
                    %VENV%\\Scripts\\python -m pip install --upgrade pip
                    if %errorlevel% neq 0 (
                        echo Failed to upgrade pip
                        exit /b %errorlevel%
                    )
                    
                    echo ===== Installing requirements =====
                    if exist requirements.txt (
                        %VENV%\\Scripts\\pip install -r requirements.txt
                        if %errorlevel% neq 0 (
                            echo Failed to install requirements
                            exit /b %errorlevel%
                        )
                    ) else (
                        echo requirements.txt not found, skipping
                    )
                    
                    echo ===== Virtual environment setup completed =====
                '''
            }
        }

        stage('Run Script') {
            steps {
                bat '''
                    echo ===== Running run.py =====
                    if not exist run.py (
                        echo run.py not found!
                        dir
                        exit /b 1
                    )
                    %VENV%\\Scripts\\python run.py
                    if %errorlevel% neq 0 (
                        echo run.py execution failed with error %errorlevel%
                        exit /b %errorlevel%
                    )
                '''
            }
        }
    }

    post {
        always {
            // 清理虚拟环境（可选）
            bat 'if exist %VENV% rd /s /q %VENV%'
        }
        success {
            echo 'Script executed successfully!'
        }
        failure {
            echo 'Script execution failed!'
            // 打印工作空间内容，方便排查
            bat 'echo Current workspace: %cd% && dir'
        }
    }
}