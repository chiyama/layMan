@echo off

set PYTHONROOT=C:\Python27

set PATH=%PATH%;%PYTHONROOT%\Lib\site-packages\pywin32_system32
set PYTHONPATH=%PYTHONPATH%;%PYTHONROOT%\Lib\site-packages\win32

%PYTHONROOT%\python.exe %~dp0layMan.py %1
