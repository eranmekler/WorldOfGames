pipeline {
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh "sudo docker-compose build"
            }
        }
        stage('Run') {
            steps {
                sh "sudo docker-compose up -d"
            }
        }
        stage('Test') {
            steps {
                sh "sudo docker exec wog python tests/e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_ID')]) {
                    sh 'sudo docker login -u $DOCKER_ID -p $DOCKER_PASSWORD'
                    sh 'sudo docker push eranmekler/world_of_games:latest'
                }
                sh 'sudo docker-compose down;docker rmi $(docker images -q)'
            }
        }
    }
}