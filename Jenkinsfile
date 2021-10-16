pipeline {
    agent any
        stages {
		stage('Building our image') {
            steps{
                script {
                    sh 'sudo -s docker build -t bitcoin-flask .'
         	       }
            	 }
        	}
 	}
}
