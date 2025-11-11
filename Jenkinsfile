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
                bat '''
                    %PYTHON% -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    %PYTHON% -m pip install --upgrade pip
                '''
            }
        }

        stage('Instalar dependencias') {
            steps {
                echo 'Instalando dependencias...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    pip install pytest
                '''
            }
        }

        stage('Ejecutar pruebas (pytest)') {
            steps {
                echo 'Ejecutando pruebas con pytest...'
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    pytest -v --maxfail=1 --disable-warnings
                '''
            }
        }
    }

    post {
        always {
            echo 'Limpiando entorno virtual...'
            bat 'rmdir /s /q %VENV_DIR% || echo No se encontró el entorno virtual.'
        }
        success {
            echo 'Todas las pruebas pasaron correctamente.'
        }
        failure {
            echo 'Hubo errores en las pruebas.'
        }
    }
}