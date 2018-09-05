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
    stage('Send email') {
            def mailRecipients = "xinjiayang@deepglint.com"
            def jobName = currentBuild.fullDisplayName
            emailext body: '''${SCRIPT, template="matrix.groovy"}''',
            subject: "[Jenkins] ${jobName}",
            to: "${mailRecipientsi}",
            recipientProviders: [[$class: 'CulpritsRecipientProvider']]
    }
	stage('End') {
	    steps {
		sh "./build.sh end"
	    }
	}
    }
}
