@echo off
cd /d "%~dp0"
call audio2word_env\Scripts\activate.bat
python audio_to_word_gui.py
pause