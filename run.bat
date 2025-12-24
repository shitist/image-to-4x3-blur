@echo off
:: %~dp0 代表 BAT 文件所在的绝对路径
:: %* 代表传给 bat 的所有参数（支持一次拖拽多张图）
py "%~dp0convert_image.py" %*
pause
