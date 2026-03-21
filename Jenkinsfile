pipeline {
    agent any

    environment {
        // Windows 路径使用反斜杠，在 Groovy 字符串中需要转义
        VENV = "${WORKSPACE}\\venv"
    }

    stages {
        stage('Checkout') {
            steps {
                // 可选：如果需要在构建前清除工作空间
                // cleanWs()
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                bat '''
                    echo Creating Python virtual environment...
                    python -m venv %VENV%
                    echo Upgrading pip...
                    %VENV%\\Scripts\\python -m pip install --upgrade pip
                    echo Installing requirements...
                    %VENV%\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Run Script') {
            steps {
                bat '''
                    %VENV%\\Scripts\\python run.py
                '''
            }
        }
    }

    post {
        always {
            // Windows 下删除目录
            bat 'if exist %VENV% rd /s /q %VENV%'
        }
        success {
            echo 'Script executed successfully!'
        }
        failure {
            echo 'Script execution failed!'
        }
    }
}