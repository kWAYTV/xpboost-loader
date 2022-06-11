# XPBOOST.LUA Loader, auto load and inject the accounts
I basically replaced vac bypass success windows by beeps to make it a procces *without* having to click annoying shit like [this](https://cdn.discordapp.com/attachments/984877542529962054/985120358204076032/unknown.png).<br /><br />
Place everything in a folder with **ONLY** the *template.bat* and the *skeet loader* (exe)<br /><br />
Before telling me i try to rat you with the **.exe** head up [here](https://github.com/kWAYTV/xpboost-loader#vac-bypass-loader-is-legit)
# Setting it up
Install SanboxiePlus<br /><br />
Fill the **template.bat** as follows:<br /><br />
**/box:name**<br /> with the name of each respective sandboxie box (one per account without main)<br />
**bot1_user bot1_pass**<br /> username password format (whith every one).<br />
**Steam path**<br />
**Sandboxie Path**<br />
**Vac bypass loader Path**<br /> preferable drop it in D: Drive root directory and don't edit the .bat default path<br /><br />
Main *doesn't* use sandboxie neither vac bypass<br />
Set up the *timeouts* according to your pc specs.<br /><br />
# How to add more bots
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
# VAC-Bypass-Loader Isn't Legit!
Then make it yourself!
```
https://github.com/danielkrupinski/VAC-Bypass
1. Search for msgbox in the solution, anything that is a success msgbox, delete the line, leave errors!
2. Compile

https://github.com/R3nzTheCodeGOD/DLL-Byte-Converter
1. Use this python project to convert the DLL to an array of bytes.
2. Copy the output.

https://github.com/danielkrupinski/VAC-Bypass-Loader
1. Replace the binary code from binary.h with the output from the python converter.
2. Then compile exe 
```
# Links
[Discord](https://discord.gg/kws)<br />
[Telegram](https://t.me/kwaytv)<br />
[XPBOOST.LUA](https://discord.gg/xpboost)