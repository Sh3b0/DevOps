pipeline {
  agent any
  stages {
    stage('Test') {
      agent any
      steps {
        sh '''apt install python3 python3-pip
pip3 install -r requirements.txt
python3 -m pytest
'''
      }
    }

  }
}