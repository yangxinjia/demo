// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    stages {
        stage('Build') {
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
		junit allowEmptyResults: true, testResults: './demo_test.xml'
	    }
	}
        stage('SendEmail'){
	    steps{
                mail bcc: '', body: 'ci Jenkinsfile pipline mail test', cc: '18810911526@163.com', from: '', replyTo: '', subject: 'test_CI', to: 'xinjiayang@deepglint.com'
	    }
	}
	stage('End') {
	    steps {
		sh "./build.sh end"
	    }
	}
    }
}
