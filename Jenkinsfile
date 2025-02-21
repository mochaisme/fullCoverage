pipeline {
    agent any

    environment {
        SONAR_HOST_URL = 'http://localhost:9000'   // Ubah jika pakai SonarCloud
        SONAR_TOKEN = credentials('squ_c5fb7be8f4694f6213ce453f72f7f6b897bafb40')  // Gunakan token dari Jenkins Credentials
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mochaisme/fullCoverage.git'  // Ganti dengan repo GitHub-mu
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest pytest-cov'
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh 'pytest --cov=. --cov-report=xml'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar-scanner') {  // Sesuai dengan nama di Jenkins Tool Configuration
                    sh 'sonar-scanner -Dsonar.projectKey=my-python-project -Dsonar.sources=. -Dsonar.python.coverage.reportPaths=coverage.xml'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    def qg = waitForQualityGate()
                    if (qg.status != 'OK') {
                        error "Quality Gate failed: ${qg.status}"
                    }
                }
            }
        }
    }
}
