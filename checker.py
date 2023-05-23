import requests 
import colorama
from colorama import init, Fore 
init()


with open('vanities.txt', 'r') as file:
    vanities = file.readlines()
    for x in vanities:
        vanity = x.rstrip()
        r = requests.get(f"https://discordapp.com/api/v6/invite/{vanity}")
        if r.status_code == 200:
            print(Fore.RED + f"{x} is taken")
        elif r.status_code == 404:
            print(Fore.GREEN + f"{x} is not taken!")
