# XPBOOST.LUA Loader, auto load and inject the accounts
I basically replaced vac bypass success windows by beeps to make it a procces *without* having to click annoying shit like [this](https://cdn.discordapp.com/attachments/984877542529962054/985120358204076032/unknown.png).<br /><br />
Place everything in a folder with **ONLY** the *template.bat*/*loader.py* and the *skeet loader* (exe)<br /><br />
Before telling me i try to rat you with the **VAC-Bypass-Loader.exe** head up [here](https://github.com/kWAYTV/xpboost-loader#vac-bypass-loader-is-legit)<br /><br />
Main account doesn't use sandbox neither vac bypass loader. Be sure to have steam and sandboxie clossen when opening the *.bat*.
# Important for the .py users
Fill the *config.json* on the .py loader besides it having the auto config feature as it's not fixed yet.
# Settings (.bat)
Install SanboxiePlus<br /><br />
Fill the **template.bat** as follows:<br /><br />
**/box:name**<br /> With the name of each respective sandboxie box (one per account except main)<br />
**bot1_user bot1_pass**<br /> username password format (whith every one).<br />
**Steam.exe path**<br /> Self explanatory.<br />
**Sandboxie.exe Path**<br /> Self explanatory.<br />
**VAC-Bypass-Loader.exe Path**<br /> Preferable drop the .exe in D: Drive root directory and don't edit the .bat default path<br /><br />
Main *doesn't* use sandboxie neither vac bypass<br />
Set up the *timeouts* according to your pc specs. In the .py default timeouts are *80 seconds*, will change in the future updates.<br /><br />
# Settings (.py)
Just create a config.json in the same directory and fill it with this information
```json
{
    "sandboxie_path": "null",
    "steam_path": "null",
    "bypass_path": "null",
    "bot1": {
        "username": "null",
        "password": "null",
        "box": "null"
    },
    "bot2": {
        "username": "null",
        "password": "null",
        "box": "null"
    },
    "bot3": {
        "username": "null",
        "password": "null",
        "box": "null"
    },
    "main": {
        "username": "null",
        "password": "null",
        "box": "null"
    }
}
```
**..._paths**: Are normal directory paths. Ex: `C:/program files/Sandboxie-Plus/Start.exe`,`D:/Steam/Steam.exe`,`D:/VAC-Bypass-Loader.exe`
**user and pass** Self explanatory. Bot 1 will be *top left*, bot2 will be *top right*, bot3 will be *bottom mid* and main in *top mid*
**box** the name of the sandboxie box for each respective account.
# How to add more bots (.bat)
To add more bots add this code below line line 41 as much times as bots you want to add:<br />
```bat
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
Be aware that you need to edit the *x* and *y* value to the position on your screen<br />
Let me know in discord if you need help


# How to add more bots (.py)
*Soon...*

# To do list
- Custom delays
- Fix auto cfg generator
- Detect csgo opening and injection instead of waiting
- I'm sure forgetting smth

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
[Discord](https://discord.gg/MRNuVCXuTS)<br />
[Telegram](https://t.me/kwaytv)<br />
[XPBOOST.LUA](https://discord.gg/xpboost)