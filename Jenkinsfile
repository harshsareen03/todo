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
                python -m venv venv

                call venv\\Scripts\\activate

                pip install -r requirements.txt
                '''

            }

        }

        stage('Run Tests') {

            steps {

                bat '''
                call venv\\Scripts\\activate

                pytest
                '''

            }

        }

        stage('Build') {

            steps {

                echo 'Build Successful'

            }

        }


        stage('RUN APP') {

            steps {

                bat '''
                call venv\\Scripts\\activate

                python app.py
                '''

            }

        }

    }

}