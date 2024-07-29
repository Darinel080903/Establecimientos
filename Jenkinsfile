pipeline{
    agent any
    environment {
        DOCKER_IMAGE = 'service-user2'
        PORT_MAPPING = '8002:8002'
        CONTAINER_NAME = 'service-user2-container'
        AWS_REGION = 'us-east-1'
        AWS_ACCESS_KEY_ID = "${env.AWS_ACCESS_KEY_ID}"
        AWS_SECRET_ACCESS_KEY = "${env.AWS_SECRET_ACCESS_KEY}"
        URR2 = "${env.URR2}"
        USS2 = "${env.USS2}"
        PSS2 = "${env.PSS2}"
    }

    stages {
        stage('Stop Container and Remove') {
            steps {
                script {
                    def containerExists = sh(script: "docker ps -a --filter name=^/${CONTAINER_NAME}\$ --format '{{.Names}}'", returnStdout: true).trim()
                    if (containerExists == CONTAINER_NAME) {
                        sh "docker stop ${CONTAINER_NAME}"
                        sh "docker rm ${CONTAINER_NAME}"
                    }
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                script {
                    def dockerImage = docker.build(DOCKER_IMAGE)
                    dockerImage.run("-e AWS_ACCESS_KEY_ID=${env.AWS_ACCESS_KEY_ID} \
                        -e AWS_SECRET_ACCESS_KEY=${env.AWS_SECRET_ACCESS_KEY} \
                        -e AWS_REGION=${env.AWS_REGION} \
                        -e URR2=${env.URR2} \
                        -e USS2=${env.USS2} \
                        -e PSS2=${env.PSS2} \
                        -p 8002:8002 --name ${CONTAINER_NAME}")
                }
            }
        }
    }
}