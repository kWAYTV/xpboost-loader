#################IMPORTS#######################
import os, glob, subprocess, time, json, sys  #
from colorama import Fore, Back, Style        #
from colorama import init                #
###############################################

#################CODE##########################
clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")
os.system(f"title Shillify Discord - Starting... - discord.gg/kws")

#Slow type
def slow_type(text, speed, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()

#Intro text
intro = f"""
{Fore.MAGENTA}════════════════════════════════════════════════════════════════════════════════════════════════{Fore.RESET}
██╗  ██╗██████╗ ██████╗  ██████╗  ██████╗ ███████╗████████╗██╗     ██╗   ██╗ █████╗ 
╚██╗██╔╝██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝██║     ██║   ██║██╔══██╗
 ╚███╔╝ ██████╔╝██████╔╝██║   ██║██║   ██║███████╗   ██║   ██║     ██║   ██║███████║
 ██╔██╗ ██╔═══╝ ██╔══██╗██║   ██║██║   ██║╚════██║   ██║   ██║     ██║   ██║██╔══██║
██╔╝ ██╗██║     ██████╔╝╚██████╔╝╚██████╔╝███████║   ██║██╗███████╗╚██████╔╝██║  ██║
╚═╝  ╚═╝╚═╝     ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
{Fore.MAGENTA}════════════════════════════════════════════════════════════════════════════════════════════════{Fore.RESET}
\n\n
{Fore.MAGENTA}╭───────────────╮{Fore.RESET}
│  XPBOOST.LUA  │  
{Fore.MAGENTA}╰───────────────╯{Fore.RESET}
"""

#Intro title and shit
def print_intro():
    clear()
    slow_type(intro + Style.RESET_ALL, 0.001)

#Global declarations
global exists
global filled
filled = False
exists = False

#Start Loader
def StartLoader():
    subprocess.call('for /r "." %a in (*.exe) do start "" "%~fa" --load=1', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

#Restart function
def restart():
    slow_type(Fore.CYAN + "Restart: " + Style.RESET_ALL +  "Trying to restart, if it doesn't work, do it manually.  - discord.gg/kws", 0.001)
    time.sleep(2)
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

#Config exists function
def config_exists():
    global exists
    os.system(f"title XPBOOST.LUA Loader - Checking config...  - discord.gg/kws")
    slow_type(Fore.MAGENTA + "Checker: " + Style.RESET_ALL + "Checking if config exists...",0.001,)
    try:
        with open("config.json") as f:
            config = json.load(f)
        exists = True
    except FileNotFoundError:
        exists = False
        os.system(
            f"title XPBOOST.LUA Loader - Config not found! Creating one...  - discord.gg/kws"
        )
        slow_type(
            Fore.MAGENTA
            + "Checker: "
            + Style.RESET_ALL
            + "Config not found! Creating one...",
            0.001,
        )
        clear()
        with open("config.json", "w") as f:
            config = {
                "sandboxie_path": "null",
                "steam_path": "null",
                "bypass_path": "null",
                "bot1": {"username": "null", "password": "null", "box": "null"},
                "bot2": {"username": "null", "password": "null", "box": "null"},
                "bot3": {"username": "null", "password": "null", "box": "null"},
                "main": {"username": "null", "password": "null", "box": "null"},
            }
            json.dump(config, f)
    return config
    exists = True
    restart()

config_exists()
#Import data from json file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

    sandPath = config["sandboxie_path"]
    steamPath = config["steam_path"]
    bypassPath = config["bypass_path"]
    bot1_user = config["bot1"]["username"]
    bot1_pass = config["bot1"]["password"]
    bot1_box = config["bot1"]["box"]
    bot2_user = config["bot2"]["username"]
    bot2_pass = config["bot2"]["password"]
    bot2_box = config["bot2"]["box"]
    bot3_user = config["bot3"]["username"]
    bot3_pass = config["bot3"]["password"]
    bot3_box = config["bot3"]["box"]
    main_user = config["main"]["username"]
    main_pass = config["main"]["password"]


#Check if config is filled function
def config_filled():
    global sandPath, steamPath, bypassPath, bot1_user, bot1_pass, bot1_box, bot2_user, bot2_pass, bot2_box, bot3_user, bot3_pass, bot3_box, main_user, main_pass, filled
    if sandPath or steamPath or bypassPath or bot1_user or bot1_pass or bot1_box or bot2_user or bot2_pass or bot3_user or bot3_pass or bot3_box or main_user or main_pass != "null":
        filled = True
    if sandPath or steamPath or bypassPath or bot1_user or bot1_pass or bot1_box or bot2_user or bot2_pass or bot3_user or bot3_pass or bot3_box or main_user or main_pass == "null":
        filled = False
    if filled == False and sandPath == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED
            + "Checker: "
            + Style.RESET_ALL
            + "No settings found... Answer to the questions carefully!",
            0.001,
        )
        os.system(
            f"title XPBOOST.LUA Loader - No settings found... Answer to the questions carefully!  - discord.gg/kws"
        )
        time.sleep(2)
        clear()
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Sandboxie path not set!", 0.001
        )
        os.system(
            f"title XPBOOST.LUA Loader - Sandboxie path not set!  - discord.gg/kws"
        )
        while unset == True:
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your sandboxie-plus start.exe path: ",
                0.001,
            )
            sandPath = input()

            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }

            sandPath = sandPath
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Sandboxie path set!",
                0.001,
            )
            os.system(
                f"title XPBOOST.LUA Loader - Sandboxie path set!  - discord.gg/kws"
            )
    else:
        pass
    if filled == False and steamPath == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Steam path not set!", 0.001
        )
        os.system(f"title XPBOOST.LUA Loader - Steam path not set!  - discord.gg/kws")
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your steam.exe path: ",
                0.001,
            )
            steamPath = input()

            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            steamPath = steamPath
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Steam path set!", 0.001
            )
            os.system(f"title XPBOOST.LUA Loader - Steam path set!  - discord.gg/kws")
    else:
        pass
    if filled == False and bypassPath == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "VAC Bypass path not set!", 0.001
        )
        os.system(
            f"title XPBOOST.LUA Loader - VAC Bypass path not set!  - discord.gg/kws"
        )
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your vac-bypass-loader.exe path: ",
                0.001,
            )
            bypassPath = input()

            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            bypassPath = bypassPath
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "VAC Bypass path set!",
                0.001,
            )
            os.system(
                f"title XPBOOST.LUA Loader - VAC Bypass path set!  - discord.gg/kws"
            )
    else:
        pass
    if filled == False and bot1_user == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Bot 1 username not set!", 0.001
        )
        os.system(
            f"title XPBOOST.LUA Loader - Bot 1 username not set!  - discord.gg/kws"
        )
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your bot1 username: ",
                0.001,
            )
            bot1_user = input()
            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Bot 1 username set!",
                0.001,
            )
            os.system(
                f"title XPBOOST.LUA Loader - Bot 1 username set!  - discord.gg/kws"
            )
    else:
        pass
    if filled == False and bot1_pass == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Bot 1 password not set!", 0.001
        )
        os.system(
            f"title XPBOOST.LUA Loader - Bot 1 password not set!  - discord.gg/kws"
        )
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your bot1 password: ",
                0.001,
            )
            bot1_pass = input()
            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Bot 1 password set!",
                0.001,
            )
            os.system(
                f"title XPBOOST.LUA Loader - Bot 1 password set!  - discord.gg/kws"
            )
    else:
        pass
    if filled == False and bot1_box == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Bot 1 box not set!", 0.001
        )
        os.system(f"title XPBOOST.LUA Loader - Bot 1 box not set!  - discord.gg/kws")
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your bot1 box: ",
                0.001,
            )
            bot1_box = input()
            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Bot 1 box set!", 0.001
            )
            os.system(f"title XPBOOST.LUA Loader - Bot 1 box set!  - discord.gg/kws")
    else:
        pass
    if filled == False and bot2_user == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Bot 2 username not set!", 0.001
        )
        os.system(
            f"title XPBOOST.LUA Loader - Bot 2 username not set!  - discord.gg/kws"
        )
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your bot2 username: ",
                0.001,
            )
            bot2_user = input()
            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Bot 2 username set!",
                0.001,
            )
            os.system(
                f"title XPBOOST.LUA Loader - Bot 2 username set!  - discord.gg/kws"
            )
    else:
        pass
    if filled == False and bot2_pass == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Bot 2 password not set!", 0.001
        )
        os.system(
            f"title XPBOOST.LUA Loader - Bot 2 password not set!  - discord.gg/kws"
        )
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your bot2 password: ",
                0.001,
            )
            bot2_pass = input()
            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Bot 2 password set!",
                0.001,
            )
            os.system(
                f"title XPBOOST.LUA Loader - Bot 2 password set!  - discord.gg/kws"
            )
    else:
        pass
    if filled == False and bot2_box == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Bot 2 box not set!", 0.001
        )
        os.system(f"title XPBOOST.LUA Loader - Bot 2 box not set!  - discord.gg/kws")
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your bot2 box: ",
                0.001,
            )
            bot2_box = input()
            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Bot 2 box set!", 0.001
            )
            os.system(f"title XPBOOST.LUA Loader - Bot 2 box set!  - discord.gg/kws")
    else:
        pass
    if filled == False and bot3_user == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Bot 3 username not set!", 0.001
        )
        os.system(
            f"title XPBOOST.LUA Loader - Bot 3 username not set!  - discord.gg/kws"
        )
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your bot3 username: ",
                0.001,
            )
            bot3_user = input()
            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Bot 3 username set!",
                0.001,
            )
            os.system(
                f"title XPBOOST.LUA Loader - Bot 3 username set!  - discord.gg/kws"
            )
    else:
        pass
    if filled == False and bot3_pass == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Bot 3 password not set!", 0.001
        )
        os.system(
            f"title XPBOOST.LUA Loader - Bot 3 password not set!  - discord.gg/kws"
        )
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your bot3 password: ",
                0.001,
            )
            bot3_pass = input()
            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
             
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Bot 3 password set!",
                0.001,
            )
            os.system(
                f"title XPBOOST.LUA Loader - Bot 3 password set!  - discord.gg/kws"
            )
    else:
        pass
    if filled == False and bot3_box == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Bot 3 box not set!", 0.001
        )
        os.system(f"title XPBOOST.LUA Loader - Bot 3 box not set!  - discord.gg/kws")
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your bot3 box: ",
                0.001,
            )
            bot3_box = input()
            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Bot 3 box set!", 0.001
            )
            os.system(f"title XPBOOST.LUA Loader - Bot 3 box set!  - discord.gg/kws")
    else:
        pass
    if filled == False and main_user == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Main username not set!", 0.001
        )
        os.system(
            f"title XPBOOST.LUA Loader - Main username not set!  - discord.gg/kws"
        )
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your main username: ",
                0.001,
            )
            main_user = input()
            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Main username set!", 0.001
            )
            os.system(
                f"title XPBOOST.LUA Loader - Main username set!  - discord.gg/kws"
            )
    else:
        pass
    if filled == False and main_pass == "null":
        clear()
        unset = True
        slow_type(
            Fore.RED + "Checker: " + Style.RESET_ALL + "Main password not set!", 0.001
        )
        os.system(
            f"title XPBOOST.LUA Loader - Main password not set!  - discord.gg/kws"
        )
        while unset == True:
            slow_type(
                Fore.RED + "Checker: " + Style.RESET_ALL + "No settings found!", 0.001
            )
            slow_type(
                Fore.BLUE
                + "Input: "
                + Style.RESET_ALL
                + "Please enter your main password: ",
                0.001,
            )
            main_pass = input()
            update = {
                "sandboxie_path": sandPath, "steam_path": steamPath, "bypass_path": bypassPath,
             "bot1": {"username": bot1_user, "password": bot1_pass, "box": bot1_box},
             "bot2": {"username": bot2_user, "password": bot2_pass, "box": bot2_box},
             "bot3": {"username": bot3_user, "password": bot3_pass, "box": bot3_box},
             "main": {"username": main_user, "password": main_pass}
             }
            config.update(update)
            with open("config.json", "w") as jsfile:
                json.dump(config, jsfile)
                jsfile.close()
            unset = False
            slow_type(
                Fore.GREEN + "Success: " + Style.RESET_ALL + "Main password set!", 0.001
            )
            os.system(
                f"title XPBOOST.LUA Loader - Main password set! Starting...  - discord.gg/kws"
            )
    else:
        pass
    filled = True

#Boosting executing function
def boost():
    global sandPath, steamPath, bypassPath, bot1_user, bot1_pass, bot1_box, bot2_user, bot2_pass, bot2_box, bot3_user, bot3_pass, bot3_box, main_user, main_pass
    seconds = 80
    slow_type(Fore.CYAN + "Logs: " + Style.RESET_ALL + "Starting bot 1!", 0.001)
    os.system(f"title XPBOOST.LUA Loader - Starting bot 1!  - discord.gg/kws")
    os.system(
        f'start "" "{sandPath}" /box:{bot1_box} "{bypassPath}" /s "{steamPath}" -silent  -login {bot1_user} {bot1_pass} -applaunch 730 -x 0 -y 0 -sw -w 640 -h 480 -low -novid -window -noborder -nosound'
    )
    slow_type(
        Fore.YELLOW
        + "Sleep: "
        + Style.RESET_ALL
        + f" Opened bot1 window. Sleeping for {seconds} second(s).",
        0.02,
    )
    time.sleep(seconds)
    StartLoader()
    slow_type(
        Fore.RED
        + "Injector: "
        + Style.RESET_ALL
        + f" Injected bot1 window. Sleeping for {seconds} second(s).",
        0.02,
    )
    time.sleep(seconds)
    slow_type(Fore.CYAN + "Logs: " + Style.RESET_ALL + "Starting bot 2!", 0.001)
    os.system(f"title XPBOOST.LUA Loader - Starting bot 2!  - discord.gg/kws")
    os.system(
        f'start "" "{sandPath}" /box:{bot2_box} "{bypassPath}" /s "{steamPath}" -silent  -login {bot2_user} {bot2_pass} -applaunch 730 -x 1280 -y 0 -sw -w 640 -h 480 -low -novid -window -noborder -nosound'
    )
    slow_type(
        Fore.YELLOW
        + "Sleep: "
        + Style.RESET_ALL
        + f" Opened bot2 window. Sleeping for {seconds} second(s).",
        0.02,
    )
    time.sleep(seconds)
    StartLoader()
    slow_type(
        Fore.RED
        + "Injector: "
        + Style.RESET_ALL
        + f" Injected bot2 window. Sleeping for {seconds} second(s).",
        0.02,
    )
    time.sleep(seconds)
    slow_type(Fore.CYAN + "Logs: " + Style.RESET_ALL + "Starting bot 3!", 0.001)
    os.system(f"title XPBOOST.LUA Loader - Starting bot 3!  - discord.gg/kws")
    os.system(
        f'start "" "{sandPath}" /box:{bot3_box} "{bypassPath}" /s "{steamPath}" -silent  -login {bot3_user} {bot3_pass} -applaunch 730 -x 640 -y 480 -sw -w 640 -h 480 -low -novid -window -noborder -nosound'
    )
    slow_type(
        Fore.YELLOW
        + "Sleep: "
        + Style.RESET_ALL
        + f" Opened bot3 window. Sleeping for {seconds} second(s).",
        0.02,
    )
    time.sleep(seconds)
    StartLoader()
    slow_type(
        Fore.RED
        + "Injector: "
        + Style.RESET_ALL
        + f" Injected bot3 window. Sleeping for {seconds} second(s).",
        0.02,
    )
    time.sleep(seconds)
    slow_type(Fore.CYAN + "Logs: " + Style.RESET_ALL + "Starting main!", 0.001)
    os.system(f"title XPBOOST.LUA Loader - Starting main!  - discord.gg/kws")
    os.system(
        f'start "" "{steamPath}" -silent -login {main_user} {main_pass} -applaunch 730 -x 640 -y 0 -sw -w 640 -h 480 -low -novid -window -noborder -nosound'
    )
    slow_type(
        Fore.YELLOW
        + "Sleep: "
        + Style.RESET_ALL
        + f" Opened main window. Sleeping for {seconds} second(s).",
        0.02,
    )
    time.sleep(seconds)
    StartLoader()
    slow_type(
        Fore.RED
        + "Injector: "
        + Style.RESET_ALL
        + f" Injected main window. Sleeping for {seconds} second(s).",
        0.02,
    )
    time.sleep(seconds)
    slow_type(Fore.CYAN + "Logs: " + Style.RESET_ALL + "Successfully started!", 0.001)
    os.system(f"title XPBOOST.LUA Loader - Successfully started!  - discord.gg/kws")
    time.sleep(3)
    clear()
    slow_type(Fore.RED + "Finished: " + Style.RESET_ALL + "Done! Closing...", 0.001)
    exit()

#Start with logo and logs function
def start():
    global sandPath, steamPath, bypassPath, bot1_user, bot1_pass, bot1_box, bot2_user, bot2_pass, bot2_box, bot3_user, bot3_pass, bot3_box, main_user, main_pass, exists, filled
    config_filled()
    if exists == True and filled == True:
        slow_type(Fore.MAGENTA + "Checker: " + Style.RESET_ALL + "Config exists and it's filled!",0.001,)
        slow_type(Fore.MAGENTA + "Checker: " + Style.RESET_ALL + "Starting...",0.001,)
        time.sleep(1)
        clear()
        print_intro()
        os.system(f"title Shillify Discord - Ready! - discord.gg/kws")
        slow_type("Good luck with " + Fore.GREEN + f"boosting" + Style.RESET_ALL + "!\n\n", 0.001)
        time.sleep(2)
        boost()
    elif exists == True and filled == False:
        slow_type(Fore.MAGENTA + "Checker: " + Style.RESET_ALL + "Config exists but it's not filled!",0.001,)
        config_filled()

start()