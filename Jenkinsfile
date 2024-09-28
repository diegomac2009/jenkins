pipeline {
    agent any
    stages {
        stage('Show Branch Variables') {
            steps {
                script {
                    // Imprime las variables relacionadas con la rama para confirmar el valor correcto
                    echo "GIT_BRANCH: ${env.GIT_BRANCH}"    // Nombre de la rama
                    echo "GIT_COMMIT: ${env.GIT_COMMIT}"    // Hash del commit actual
                }
            }
        }
        stage('Build') {
            when {
                expression {
                    return env.GIT_BRANCH == 'Staging' || env.GIT_BRANCH == 'origin/Staging'  // Ajusta según el valor de GIT_BRANCH
                }
            }
            steps {
                echo 'Building in Staging...'
            }
        }
        stage('Tests') {
            when {
                expression {
                    return env.GIT_BRANCH == 'Testing' || env.GIT_BRANCH == 'origin/Testing'  // Ajusta según el valor de GIT_BRANCH
                }
            }
            steps {
                echo 'Running tests in Testing...'
            }
        }
        stage('Deploy') {
            when {
                expression {
                    return env.GIT_BRANCH == 'main' || env.GIT_BRANCH == 'origin/main'  // Ajusta según el valor de GIT_BRANCH
                }
            }
            steps {
                echo 'Deploying in main...'
                sh 'echo "Se hizo un cambio en la rama main a las $(date)" >> /var/jenkins_home/jenkins_pipeline.log'
                sh 'echo "GIT_BRANCH: ${env.GIT_BRANCH}" >> /var/jenkins_home/jenkins_pipeline.log'
                sh 'echo "GIT_COMMIT: ${env.GIT_COMMIT}" >> /var/jenkins_home/jenkins_pipeline.log'
            }
        }
    }
}
