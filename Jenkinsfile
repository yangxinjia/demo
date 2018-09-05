// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    stages {
//        stage('Check') {
//            steps {
//                sh './build.sh check'
//            }
//        }
        stage('Compile') {
            steps {
                sh './build.sh compile'
            }
        }
	stage('Run') {
	    steps {
		sh './build.sh run'
	    }
	}
        stage('Test') {
            steps {
                sh './build.sh test'
            }
        }
        stage('ShowTestResult') {
	    steps {
		junit allowEmptyResults: true, testResults: 'report/*.xml'
	    }
	}
        stage('Sendemail') {
            steps {
                emailext body: '${FILE,path="/var/lib/jenkins/email-templates/matrix.groovy"}', subject: 'demo', to: 'xinjiayang@deepglint.com'    
            }
        }
	stage('End') {
	    steps {
		sh "./build.sh end"
	    }
	}
    }
}
