# xpboost-loader
XPBOOST.LUA Loader, auto load and inject the accounts.<br />
Install SanboxiePlus<br />
I basically replaced vac bypass success windows by beeps to make it a procces *without* having to click.lace everything in a folder with **ONLY** the *template.bat* and the *skeet loader* (exe)<br /><br />
Setting it up:<br />
**/box:name** with the name of each respective sandboxie box (one per account without main)<br />
**bot1_user bot1_pass** username password format (whith every one).<br />
**Steam path**<br />
**Sandboxie Path**<br />
**Vac bypass loader Path** preferable drop it in D: Drive root directory and don't edit the .bat default path<br /><br />
Main *doesn't* use sandboxie neither vac bypass<br />
Set up the *timeouts* according to your pc specs.<br />
To add more bots add this code below line line 41 as much times as bots you want to add:<br />
```
echo [+] Waiting to open bot(nextnumber).
timeout /t 120 /nobreak > nul
echo [+] Opening bot(nextnumber).
echo --------------------
start "" "c:/program files/Sandboxie-Plus/Start.exe" /box:boxname "D:\VAC-Bypass-Loader.exe" "D:\Steam\Steam.exe" -silent  -login bot(nextnumber)_user bot(nextnumber)_pass -applaunch 730 -x 0 -y 0 -sw -w 640 -h 480 -low -novid -window -noborder -nosound
echo [+] Waiting to inject.
echo --------------------
timeout /t 60 /nobreak > nul
echo [+] Injecting!
echo --------------------
for /r "." %%a in (*.exe) do start "" "%%~fa" --load=1
```
# Links
[Discord](https://discord.gg/kws)<br />
[Telegram](https://t.me/kwaytv)
[xpboost.lua](https://discord.gg/xpboost)
