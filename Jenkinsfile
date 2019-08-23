pipeline {
    
    agent any
    stages {
        stage('pip') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('pull data') {

            steps {
                sh 'cd am_bot_data/'
                sh 'git pull origin master'
                sh 'cd ..'
            }
        }
        stage('deploy') {

            steps {
                sh 'python3 main.py'
            }
        }
    }
}
