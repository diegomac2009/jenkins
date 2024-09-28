pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Aquí puedes agregar comandos para la construcción, como `sh 'npm install'`
            }
        }
        stage('Tests') {
            steps {
                echo 'Testing...'
                // Aquí puedes ejecutar comandos de pruebas, ej. `sh 'npm test'`
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying in main...'
                // Guardar un mensaje en el log en el servidor
                sh 'echo "Se hizo un cambio en la rama main a las $(date)" >> /var/jenkins_home/jenkins_pipeline.log'
            }
        }
    }
}
