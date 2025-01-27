@echo off
REM Script to run main.py

echo =============================================
echo Starting main.py...
echo =============================================

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Please install Python first.
    pause
    exit /b 1
)

REM Run main.py
python main.py

REM Check if main.py ran successfully
if %ERRORLEVEL% neq 0 (
    echo An error occurred while running main.py.
    pause
    exit /b 1
)

echo =============================================
echo main.py executed successfully!
pause
