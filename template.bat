@echo off
title XPBOOST.LUA Loader by kWAY#1701
echo --------------------
echo Welcome to XPBOOST.LUA Loader by kWAY#1701
echo --------------------
timeout /t 4 /nobreak > null
echo --------------------
echo [*] REMEMBER TO CUSTOMIZE THE TIMEOUTS DEPENDING ON YOUR PC SPECS TO NOT WAIT A LOT IF NOT NEEDED.
echo --------------------
echo [+] Starting the loader and first bot!
echo --------------------
start "" "c:/program files/Sandboxie-Plus/Start.exe" /box:xpboosting "D:\VAC-Bypass-Loader.exe" /s "D:\Steam\Steam.exe" -silent  -login bot1_user bot1_pass -applaunch 730 -x 0 -y 0 -sw -w 640 -h 480 -low -novid -window -noborder -nosound
echo [+] Waiting to inject.
echo --------------------
timeout /t 60 /nobreak > nul
echo [+] Injecting!
echo --------------------
for /r "." %%a in (*.exe) do start "" "%%~fa" --load=1
echo [+] Waiting to open bot2.
timeout /t 120 /nobreak > nul
echo [+] Opening bot2.
echo --------------------
start "" "c:/program files/Sandboxie-Plus/Start.exe" /box:xpboosting2 "D:\VAC-Bypass-Loader.exe" "D:\Steam\Steam.exe" -silent  -login bot2_user bot2_pass -applaunch 730 -x 1280 -y 0 -sw -w 640 -h 480 -low -novid -window -noborder -nosound
echo [+] Waiting to inject.
echo --------------------
timeout /t 60 /nobreak > nul
echo [+] Injecting!
echo --------------------
for /r "." %%a in (*.exe) do start "" "%%~fa" --load=1
echo [+] Waiting to open bot3.
echo --------------------
timeout /t 120 /nobreak > nul
echo [+] Opening bot3!
echo --------------------
start "" "c:/program files/Sandboxie-Plus/Start.exe" /box:xpboosting3 "D:\VAC-Bypass-Loader.exe" "D:\Steam\Steam.exe" -silent  -login bot3_user bot3_pass -applaunch 730 -x 640 -y 480 -sw -w 640 -h 480 -low -novid -window -noborder -nosound
echo [+] Waiting to inject.
echo --------------------
timeout /t 60 /nobreak > nul
echo [+] Injecting!
echo --------------------
for /r "." %%a in (*.exe) do start "" "%%~fa" --load=1
echo [+] Waiting to open Main.
echo --------------------
timeout /t 180 /nobreak > nul
echo [+] Opening main!
echo --------------------
start "" "C:\Program Files (x86)\Steam\Steam.exe" -silent -login main_user main_pass -applaunch 730 -x 640 -y 0 -sw -w 640 -h 480 -low -novid -window -noborder -nosound
echo [+] Waiting to inject.
echo --------------------
timeout /t 60 /nobreak > nul
echo [+] Injecting!
echo --------------------
for /r "." %%a in (*.exe) do start "" "%%~fa" --load=1
echo [+] Startup done, Good luck!
echo --------------------
echo ---discord.gg/kws---
echo --------------------
pause
exit