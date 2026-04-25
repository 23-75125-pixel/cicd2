pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'gitrepo'
        GIT_CREDENTIALS_ID = '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-pat'
        GIT_BRANCH = 'main'
    }

    stages {

        stage('Checkout SCM') {
            steps {
                checkout scm: [
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.GIT_BRANCH}"]],
                    userRemoteConfigs: [[
                        url: "${env.GIT_REPO_URL}",
                        credentialsId: "${env.GIT_CREDENTIALS_ID}"
                    ]]
                ]
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh '''
                . venv/bin/activate
                python test.py
                '''
            }
        }

        stage('Deploy to Apache') {
            steps {
                sh '''
                sudo rsync -av --delete ./ /var/www/html/
                sudo chown -R www-data:www-data /var/www/html/
                '''
            }
        }
    }
}
