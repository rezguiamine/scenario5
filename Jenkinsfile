pipeline {
    agent any

    environment {
        IMAGE_NAME = "scenario5-app"
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                    trivy image \
                    --severity CRITICAL \
                    --exit-code 1 \
                    --ignore-unfixed \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Push') {
            steps {
                echo "Image passed security scan"
                sh '''
                    docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Deploy Staging') {
            steps {
                sh '''
                    docker rm -f scenario5-staging || true

                    docker run -d \
                    --name scenario5-staging \
                    -p 5001:5000 \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Production Approval') {
            steps {
                input message: 'Deploy to production?'
            }
        }

        stage('Deploy Production') {
            steps {
                sh '''
                    docker rm -f scenario5-prod || true

                    docker run -d \
                    --name scenario5-prod \
                    -p 5002:5000 \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully"
        }

        failure {
            echo "Pipeline failed"
        }

        always {
            echo "Pipeline finished"
        }
    }
}