// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    stages {
        stage('Echo') {
            steps {
                echo 'step 1 ********' 
            }
        }
	 stage('Build') {
            steps {
                sh 'docker_image.sh' 
                archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true 
            }
        }
	stage('End') {
            steps {
                echo 'end ********'
            }
        }

    }
}
