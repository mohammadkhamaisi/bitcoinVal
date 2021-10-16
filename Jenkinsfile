pipeline {
   environment {
		DOCKERHUB_CREDENTIALS=credentials('mohammadkhamaisi')
	}
    agent any
        stages {
		stage('Building the image') {
            steps{
                script {
                    sh 'sudo -s docker build -t bitval .'
         	       }
            	 }
        	}
		stage('Login to Dockerhub') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		stage('Tag') {

			steps {
			    sh 'sudo docker tag bitval mohammadkhamaisi/bitval'
			}
		}

        stage('Push to Dockerhub') {
			steps {
				sh 'sudo docker push mohammadkhamaisi/bitval'
			}
        }  
		
 	}
}
