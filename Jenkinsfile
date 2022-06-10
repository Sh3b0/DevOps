pipeline {
  agent any
  stages {
    stage('Test') {
      agent any
      steps {
        sh '''pip install -r requirements.txt
python -m pytest
'''
      }
    }

  }
}