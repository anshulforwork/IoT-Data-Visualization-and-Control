@echo off

rem Ensure npm is available in the PATH
set PATH=%PATH%;%ProgramFiles%\nodejs;%AppData%\npm

rem Install Node-RED globally
echo Installing Node-RED...
npm install -g --unsafe-perm node-red
if errorlevel 1 (
    echo Error: Failed to install Node-RED.
    exit /b 1
)



rem Add the directory where global packages are installed to the PATH
for /f "delims=" %%i in ('npm root -g') do set NPM_GLOBAL=%%i
set PATH=%PATH%;%NPM_GLOBAL%\node_modules\.bin

rem Start Node-RED (optional)
echo Starting Node-RED...
node-red