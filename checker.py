import requests 
import colorama
from colorama import init, Fore 
init()


with open('vanities.txt', 'r') as file: # open the vanity txt file (you can name it whatever you want just make sure to change code)
    vanities = file.readlines() # read the txt file
    for x in vanities: # create a var for each word in the txt file
        vanity = x.rstrip() # remove whitespaces 
        r = requests.get(f"https://discordapp.com/api/v6/invite/{vanity}") # get the discord api link for each vanity
        if r.status_code == 200: # create a conditional, a 200 status code means that the request was successfull 
            print(Fore.RED + f"{x} is taken") # simple print statement 
        elif r.status_code == 404: # 404 status code means the request was unsuccessfull meaning the link is not taken
            print(Fore.GREEN + f"{x} is not taken!") # another simple print statement
