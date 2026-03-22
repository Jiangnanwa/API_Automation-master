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
                    set PYTHON_EXE="D:\\python3.8\\python.exe"

                    echo ===== Creating virtual environment =====
                    %PYTHON_EXE% -m venv %VENV%
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
            echo 'Script executed successfully! Sending email...'
            emailext(
                subject: "✅ 【构建成功】自动化测试报告 - ${env.JOB_NAME} (#${env.BUILD_NUMBER})",
                body: """
                    <h2>🎉 项目构建成功！</h2>
                    <hr/>
                    <ul>
                        <li><strong>项目名称：</strong> ${env.JOB_NAME}</li>
                        <li><strong>构建编号：</strong> 第 ${env.BUILD_NUMBER} 次运行</li>
                        <li><strong>运行状态：</strong> <span style="color:green;">Success (成功)</span></li>
                        <li><strong>查看完整结果：</strong> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></li>
                    </ul>
                    <p>您的自动化脚本已顺利跑完，太棒啦！</p>
                """,
                to: "2524918238@qq.com,304840656@qq.com"  // 填你的收件邮箱。如果有多个，用逗号隔开
            )
        }
        failure {
            echo 'Script execution failed! Sending alert email...'
            emailext(
                subject: "❌ 【构建失败】警报！自动化测试未通过 - ${env.JOB_NAME} (#${env.BUILD_NUMBER})",
                body: """
                    <h2 style="color:red;">⚠️ 项目构建失败！</h2>
                    <hr/>
                    <ul>
                        <li><strong>项目名称：</strong> ${env.JOB_NAME}</li>
                        <li><strong>构建编号：</strong> 第 ${env.BUILD_NUMBER} 次运行</li>
                        <li><strong>运行状态：</strong> <span style="color:red;">Failure (失败)</span></li>
                        <li><strong>查看报错日志：</strong> <a href="${env.BUILD_URL}console">${env.BUILD_URL}console</a></li>
                    </ul>
                    <p>请尽快点击上方链接，查看控制台日志排查报错原因。</p>
                """,
                to: "2524918238@qq.com" 
            )
        }
    }
}