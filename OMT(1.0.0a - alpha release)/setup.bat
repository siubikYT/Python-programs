@echo off
REM Script to download and install Python, requests, and customtkinter

echo =============================================
echo Python Installer with Libraries Setup
echo =============================================

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo Python is already installed.
) else (
    echo Downloading Python installer...
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe -OutFile python-installer.exe"

    echo Installing Python...
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    if %ERRORLEVEL% neq 0 (
        echo Python installation failed. Exiting.
        exit /b 1
    )
    echo Python installed successfully.
)

REM Verify pip installation
pip --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Pip is not installed. Reinstalling Python.
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
)

REM Install libraries
echo Installing required libraries...
pip install requests customtkinter

if %ERRORLEVEL% neq 0 (
    echo Library installation failed. Please check your internet connection.
    exit /b 1
)

echo Libraries installed successfully.
echo =============================================
echo Setup complete!
pause
