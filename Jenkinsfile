// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    stages {
        stage('Check') {
            steps {
                sh './build.sh check'
            }
        }
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
//        stage('Test') {
//            steps {
//                sh './build.sh test'
//            }
//        }
//        stage('ShowTestResult') {
//	    steps {
//	        publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'report/demo_test.html', reportFiles: 'index.html', reportName: 'HTML Report'])
//	    }
//	}
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
