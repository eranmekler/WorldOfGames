pipeline {
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Checkout') {
            steps {
                sh 'checkout scm'
            }
        }
        stage('Build') {
            steps {
                sh "docker-compose build"
            }
        }
        stage('Run') {
            steps {
                sh "docker-compose run -d"
            }
        }
        stage('Test') {
            steps {
                sh "docker exec -it wog python tests/e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_ID')]) {
                    sh 'docker login -u $DOCKER_ID -p $DOCKER_PASSWORD'
                    sh 'docker push eranmekler/world_of_games:latest'
                }
                sh 'docker-compose down;docker rmi $(docker images -q)'
            }
        }
    }
}