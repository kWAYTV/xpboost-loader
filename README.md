# XPBOOST.LUA Loader | Made by kWAY#1701 and darby#0001
Place everything in a folder with **ONLY** the *loader.py* and the *skeet loader* (exe)<br /><br />
Before telling me i try to rat you with the **VAC-Bypass-Loader.exe** head up [here](https://github.com/kWAYTV/xpboost-loader#vac-bypass-loader-isnt-legit)<br /><br />
Main account doesn't use sandbox neither vac bypass loader. Be sure to have steam and sandboxie closed when opening the *.py*.
# Settings (.py)
Run the script for **auto config generation**.
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
    },
    "sleep": "null",
}
```
- **..._paths**: Are normal directory paths. Ex: `C:/program files/Sandboxie-Plus/Start.exe`,`D:/Steam/Steam.exe`,`D:/VAC-Bypass-Loader.exe`<br />
- **user and pass** Self explanatory. Bot 1 will be *top left*, bot2 will be *top right*, bot3 will be *bottom mid* and main in *top mid*<br />
- **box** The name of the sandboxie box for each respective account.<br />
- **sleep** The time in *seconds* that a csgo window delays to be **fully open** *plus 5 seconds* on your pc<br />

# How to add more bots (.py)
I will try either to make a feature to customize the bots you use or ask me in Discord but cba.
# To do list
- Detect csgo opening and injection instead of waiting<br />
- I'm sure forgetting smth<br />
# VAC-Bypass-Loader Isn't Legit!
Then make it yourself!<br />

https://github.com/danielkrupinski/VAC-Bypass
1. Search for msgbox in the solution, anything that is a success msgbox, delete the line, leave errors!<br />
2. Compile<br />

https://github.com/R3nzTheCodeGOD/DLL-Byte-Converter<br />
1. Use this python project to convert the DLL to an array of bytes.<br />
2. Copy the output.<br />

https://github.com/danielkrupinski/VAC-Bypass-Loader<br />
1. Replace the binary code from binary.h with the output from the python converter.<br />
2. Then compile exe<br />
<br />
Dont break my head asking for help with this.

# Links
[Discord](https://discord.gg/MRNuVCXuTS)<br />
[Telegram](https://t.me/kwaytv)<br />
[XPBOOST.LUA](https://discord.gg/xpboost)