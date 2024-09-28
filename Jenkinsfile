pipeline {
    agent any
    stages {
        stage('Show Branch') {
            steps {
                script {
                    echo "Current branch: ${env.BRANCH_NAME}"
                }
            }
        }
        stage('Build') {
            when {
                branch 'Staging'
            }
            steps {
                echo 'Staging...'
            }
        }
        stage('Tests') {
            when {
                branch 'Testing'
            }
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying main...'
                sh 'echo "Se hizo un cambio en la rama main a las $(date)" >> /var/jenkins_home/jenkins_pipeline.log'
            }
        }
    }
}
