pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        VENV_DIR = '.venv'
    }

    stages {
        stage('Preparar entorno') {
            steps {
                echo 'Configurando entorno virtual...'
                sh '''
                    ${PYTHON} -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Ejecutar pruebas unitarias') {
            steps {
                echo 'Ejecutando pruebas con unittest...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python -m unittest discover -s . -p "test_*.py" -v
                '''
            }
        }
    }

    post {
        always {
            echo 'Finalizando pipeline...'
            sh 'rm -rf ${VENV_DIR}'
        }
        success {
            echo 'Todas las pruebas pasaron correctamente.'
        }
        failure {
            echo 'Hubo errores en las pruebas.'
        }
    }
}
