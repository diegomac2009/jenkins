pipeline {
    agent any
    stages {
        stage('Show Branch Variables') {
            steps {
                script {
                    // Imprime las variables relacionadas con la rama
                    echo "BRANCH_NAME: ${env.BRANCH_NAME}"  // Nombre de la rama en un multibranch pipeline
                    echo "GIT_BRANCH: ${env.GIT_BRANCH}"    // Nombre de la rama cuando se hace checkout manual
                    echo "GIT_COMMIT: ${env.GIT_COMMIT}"    // Hash del commit actual
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Tests') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying in main...'
                sh 'echo "Se hizo un cambio en la rama main a las $(date)" >> /var/jenkins_home/jenkins_pipeline.log'
            }
        }
    }
}
