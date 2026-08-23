pipeline {

    agent any

    environment {
        EC2_HOST = '13.232.88.100'
        EC2_USER = 'ubuntu'

        IMAGE_NAME = 'student-api:1.1'
        DOCKER_REPOSITORY = 'puneetbt11/student-api'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create Python Environment') {
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

        stage('Transfer Code to EC2') {
            steps {

                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'ec2-ssh-key',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    )
                ]) {

                    sh '''
                        tar \
                            --exclude=.git \
                            --exclude=venv \
                            --exclude=__pycache__ \
                            -czf - . | \
                        ssh -i "$SSH_KEY" \
                            -o StrictHostKeyChecking=accept-new \
                            "$SSH_USER@$EC2_HOST" \
                            "rm -rf /home/ubuntu/devops-capstone-jenkins && \
                             mkdir -p /home/ubuntu/devops-capstone-jenkins && \
                             tar -xzf - -C /home/ubuntu/devops-capstone-jenkins"
                    '''
                }
            }
        }

        stage('Docker Build on EC2') {
            steps {

                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'ec2-ssh-key',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    )
                ]) {

                    sh '''
                        ssh -i "$SSH_KEY" \
                            -o StrictHostKeyChecking=accept-new \
                            "$SSH_USER@$EC2_HOST" \
                            "cd /home/ubuntu/devops-capstone-jenkins && \
                             docker build -t $IMAGE_NAME . && \
                             docker images $IMAGE_NAME"
                    '''
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {

                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'ec2-ssh-key',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    ),
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {

                    sh '''
                        printf '%s' "$DOCKER_PASSWORD" | \
                        ssh -i "$SSH_KEY" \
                            -o StrictHostKeyChecking=accept-new \
                            "$SSH_USER@$EC2_HOST" \
                            "docker login -u '$DOCKER_USERNAME' --password-stdin && \
                             docker tag $IMAGE_NAME $DOCKER_REPOSITORY:1.1 && \
                             docker push $DOCKER_REPOSITORY:1.1"
                    '''
                }
            }
        }
    }
}
