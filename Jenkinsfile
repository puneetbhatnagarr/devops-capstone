pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Environment Check') {
            steps {
                sh 'git --version'
                sh 'python3 --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh './venv/bin/python -m pip install --upgrade pip'
                sh './venv/bin/pip install -r app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/python -m pytest'
            }
        }
    }
}

