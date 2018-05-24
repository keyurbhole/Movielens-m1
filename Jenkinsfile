pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python movie_analysis.py'
      }
    }
    stage('Test') {
      steps {
        echo 'Success'
      }
    }
  }
}