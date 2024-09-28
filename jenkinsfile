pipeline {
    agent any
    stages {
        stage('Build') {
            when {
                branch 'Staging'  // Solo ejecuta este stage en la rama 'Staging'
            }
            steps {
                echo 'Staging...'
                //
            }
        }
        stage('Tests') {
            when {
                branch 'Testing'  // Solo ejecuta este stage en la rama 'Testing'
            }
            steps {
                echo 'Testing...'
                // 
            }
        }
        stage('Deploy') {
            when {
                branch 'main'  // Solo ejecuta este stage en la rama 'main'
            }
            steps {
                echo 'Deploying main...'
                 // Guarda un mensaje en un archivo de log en el servidor Linux
                sh 'echo "Se hizo un commit en la rama main a las $(date) " >> /var/log/jenkins_pipeline.log'
            }
        }
    }
}
