pipeline {
    agent any

    environment {
        PYTHON = 'python'
        VENV_DIR = '.venv'
    }

    stages {
        stage('Preparar entorno') {
            steps {
                echo 'Configurando entorno virtual...'
                bat """
                    ${PYTHON} -m venv ${VENV_DIR}
                    call ${VENV_DIR}\\Scripts\\activate
                    pip install --upgrade pip
                """
            }
        }

        stage('Instalar dependencias') {
            steps {
                echo 'Instalando dependencias...'
                bat """
                    call ${VENV_DIR}\\Scripts\\activate
                    if exist requirements.txt (
                        pip install -r requirements.txt
                    ) else (
                        echo No hay requirements.txt, continuando...
                    )
                """
            }
        }

        stage('Ejecutar pruebas unitarias') {
            steps {
                echo 'Ejecutando pruebas con unittest...'
                bat """
                    call ${VENV_DIR}\\Scripts\\activate
                    python -m unittest discover -s . -p "test_*.py" -v
                """
            }
        }
    }

    post {
        always {
            echo 'Finalizando pipeline...'
            bat "rmdir /s /q ${VENV_DIR} || echo No se encontró el entorno virtual."
        }
        success {
            echo 'Todas las pruebas pasaron correctamente.'
        }
        failure {
            echo 'Hubo errores en las pruebas.'
        }
    }
}
