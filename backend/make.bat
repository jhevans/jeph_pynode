C:\Python27_64\Scripts\virtualenv.exe --clear env
env\Scripts\pip.exe install --no-index --find-links deps -r requirements.txt
env\Scripts\pip.exe install -e .
exit /b %ERRORLEVEL%
