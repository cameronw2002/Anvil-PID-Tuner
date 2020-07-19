@echo off
setlocal
IF NOT EXIST _env (
    echo Initializing virtual environment...
    call python -m venv _env
)
call _env\Scripts\activate && pip install -r requirements.txt
call _env\Scripts\activate && python %~dp0/AnvilTuner.py