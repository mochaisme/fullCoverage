pipeline {
    agent any
    
    triggers {
        pollSCM('* * * * *') // Cek perubahan di repo setiap menit
    }

    environment {
        VENV_DIR = "venv" // Nama virtual environment
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo "Setting up Python environment..."
                sh '''
                    set -e
                    python3 -m venv ${VENV_DIR}
                    ${VENV_DIR}/bin/python -m pip install --upgrade pip
                    ${VENV_DIR}/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Build') {
            steps {
                echo "Building.."
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh '''
                    set -e
                    cd utests
                    ../${VENV_DIR}/bin/python test_calculator.py
                '''
            }
        }

        stage('Deliver') {
            steps {
                echo 'Delivering....'
                sh '''
                    echo "Doing delivery stuff..."
                '''
            }
        }
    }
}
