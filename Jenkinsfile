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
		emailext body: 'test ci 1', subject: 'test ci', to: 'xinjiayang@deepglint.com'
	    }
	}
	stage('End') {
	    steps {
		sh "./build.sh end"
	    }
	}
    }
}
