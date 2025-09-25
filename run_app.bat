@echo off
echo ===================================================
echo WuwaAPI JSON Builder - Setup and Launch
echo ===================================================

REM Vérifier si Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed correctly on your system
    echo Please install Python 3.9+ before continuing
    pause
    exit /b
)

pause
REM Créer un venv local
IF NOT EXIST venv (
    echo [INFO] Creating virtual environment...
    python -m venv venv
)
pause
REM Activer le venv
call venv\scripts\activate.bat

REM Installer les dépendances
echo [INFO] Installing dependencies
pip install --upgrade pip || exit /b
pip install -r requirements.txt || exit /b

REM Lancer l'appli
echo [INFO] Starting App...
python -m streamlit run main.py

pause