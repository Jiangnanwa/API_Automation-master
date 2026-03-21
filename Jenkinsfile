pipeline {
    agent any

    environment {
        // 定义环境变量（如 Python 虚拟环境路径）
        VENV = "${WORKSPACE}/venv"
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
                sh '''
                    # 创建并激活 Python 虚拟环境
                    python3 -m venv $VENV
                    source $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Script') {
            steps {
                sh '''
                    source $VENV/bin/activate
                    python run.py
                '''
            }
        }
    }

    post {
        always {
            // 无论成功或失败都执行清理
            sh 'rm -rf $VENV' // 可选
        }
        success {
            echo 'Script executed successfully!'
        }
        failure {
            echo 'Script execution failed!'
        }
    }
}