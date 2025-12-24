pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Récupération du code...'
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installation des dépendances Python...'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Exécution des tests...'
                bat 'pytest tests/ --cov=app --cov-report=xml --cov-report=html'
            }
        }
        
      stage('SonarQube Analysis') {
    steps {
        echo 'Analyse SonarQube...'
        script {
            def scannerHome = tool name: 'SonarScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
            withSonarQubeEnv('SonarQube') {
                bat """
                    ${scannerHome}\\bin\\sonar-scanner.bat ^
                    -Dsonar.projectKey=my-first-pipeline ^
                    -Dsonar.sources=app ^
                    -Dsonar.tests=tests ^
                    -Dsonar.python.coverage.reportPaths=coverage.xml ^
                    -Dsonar.host.url=http://localhost:9000
                """
            }
        }
    }
}
        
        stage('Build Docker Image') {
            steps {
                echo 'Construction de l\'image Docker...'
                bat 'docker build -t my-python-app:latest .'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Déploiement...'
                bat 'docker stop my-python-app || exit 0'
                bat 'docker rm my-python-app || exit 0'
                bat 'docker run -d --name my-python-app -p 5000:5000 my-python-app:latest'
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline réussie !'
        }
        failure {
            echo '❌ Pipeline échouée !'
        }
    }
}