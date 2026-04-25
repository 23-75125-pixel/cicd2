pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/23-75125-pixel/cicd2.git'
        GIT_CREDENTIALS_ID = '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-pat'
        GIT_BRANCH = 'main'
    }

    stages {
        stage('Checkout SCM') { ... }
        stage('Setup Python Environment') { ... }
        
        // ILIPAT ANG DEPLOY DITO PARA MABASA NG SELENIUM ANG LATEST CODE
        stage('Deploy to Apache') {
            steps {
                sh 'sudo rsync -av -o --delete ./ /var/www/html/'
                sh 'sudo chown -R www-data:www-data /var/www/html/'
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
