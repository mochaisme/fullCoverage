pipeline {
    agent any
    environment {
        SONARQUBE_SERVER = 'sonar-scanner' // Name from Jenkins settings
    }
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/mochaisme/fullCoverage.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests & Generate Coverage') {
            steps {
                sh 'pytest --cov=. --cov-report=xml'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv(SONARQUBE_SERVER) {
                    sh 'sonar-scanner'
                }
            }
        }
    }
}
