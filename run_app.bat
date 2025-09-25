@echo off
echo ===================================================
echo WuwaAPI JSON Builder - Setup & Launch
echo ===================================================

REM Vérifier si Python est installé
pyton --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo [ERROR] Python is not installed correctly on your system
    echo Please install Python 3.9+ before continuing
    pause
    exit /b
)

REM Créer un venv local
IF NOT EXIST venv(
    echo [INFO] Creating virtual environment...
    python -m venv venv
)

REM Activer le venv
call venv/scripts/activate

REM Installer les dépendances
echo [Info] Installing dependencies
pip install --upgrade pip
pip install -r requirements.txt

REM Lancer l'appli
echo [INFO] Starting App...
streamlit run main.py

pause