pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    echo ===== Installing requirements =====
                    python -m pip install --upgrade pip
                    if exist requirements.txt (
                        pip install -r requirements.txt
                    ) else (
                        echo requirements.txt not found, skipping
                    )
                '''
            }
        }

        stage('Run Script') {
            steps {
                bat '''
                    python run.py
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