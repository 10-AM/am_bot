pipeline {
    
    agent any
    stages {
        stage('pip') {
            when {
                anyOf {
                    branch 'master';
                }
            }
            
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('pull data') {
            when {
                anyOf {
                    branch 'master';
                }
            }

            steps {
                sh 'cd am_bot_data/'
                sh 'git pull origin master'
                sh 'cd ..'
            }
        }
        stage('deploy') {
            when {
                anyOf {
                    branch 'master';
                }
            }

            steps {
                sh 'python3 main.py'
            }
        }
    }
}
