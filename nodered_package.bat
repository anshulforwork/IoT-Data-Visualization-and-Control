@echo off

rem Install required Node-RED packages
echo Installing Node-RED packages...
npm install -g node-red-contrib-open node-red-dashboard node-red-node-ui-table
if errorlevel 1 (
    echo Error: Failed to install Node-RED packages.
    exit /b 1
)