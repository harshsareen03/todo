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
                sh '''
                python3 -m pip install --upgrade pip
                python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                python3 -m pytest -v
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Build Successful'
            }
        }

        stage('Run App') {
            steps {
                sh '''
                nohup python3 app.py > app.log 2>&1 &
                sleep 5
                '''
            }
        }
    }
}