#!/bin/python3

import os
import socket
import requests
import pyfiglet
from colorama import Fore as colour
from concurrent.futures import ThreadPoolExecutor

G = colour.GREEN
B = colour.BLUE
R = colour.RED
C = colour.CYAN
Y = colour.YELLOW
M = colour.MAGENTA

def start():
    os.system('clear')
    print("")
    banner = pyfiglet.figlet_format("DN-SPLIT")
    print(G + banner)
    print(f"{G}[{B}!!!{G}] {Y}Tool-Name {G}: {C}DN-SPLIT")
    print(f"{G}[{B}!!!{G}] {Y}Github    {G}: {C}https://github.com/K3ysTr0K3R")
    print(f"{G}[{B}!!!{G}] {Y}Instagram {G}: {C}1_k3ystr0k3r_1")
    print(f"{G}[{B}!!!{G}] {Y}Coded By  {G}: {C}K3ysTr0K3R")
    print("")

def check_subdomain(subdomain, target):
    dns = f"{subdomain}.{target}"
    try:
        send_get_req = requests.get(f"http://{dns}")
        server = send_get_req.headers
        ip_address = socket.gethostbyname(dns)
        server_name = server.get("Server")
        response_code = send_get_req.status_code
        if server_name:
            print(f"{G}[{B}+{G}] {Y}{dns} {G}[{C}{ip_address}{G}] {G}[{M}{server_name}{G}] {G}[{C}{response_code}{G}]")
    except (socket.gaierror, requests.ConnectionError):
        pass

def main():
    start()

    try:
        connect_google = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        CONNECTION = connect_google.connect_ex(('www.google.com', 80))
        if CONNECTION == 0:
            print(f"{B}========================================================")
            print(f"{G}[{B}+++{G}] Internet Connection Established{B}: {C}Proceeding")
            print(f"{B}========================================================")
            start()
        else:
            print(f"{B}========================================================")
            print(f"{G}[{R}!!!{G}] No Internet Connection Found{B}: {R}Exiting")
            print(f"{B}========================================================")
            exit()

        target = input(f"{G}[{Y}i{G}] {G}Insert your target domain here without www{B}: {R}")
        start()

        if not target:
            print(f"{G}[{R}!{G}] You must insert your target domain")
            exit()
        else:
            wordlist_option = input(f"""{G}[{M}1{G}] {M}subdomains-small.txt
{G}[{M}2{G}] {M}subdomains-top1mil-20000.txt
{G}[{M}3{G}] {M}subdomains-top1mil-5000.txt
{G}[{M}4{G}] {M}subdomains-top1mil.txt

{G}[{Y}i{G}] First things first, pick an option for the wordlist you want to use for {R}{target}{B}: """)

            wordlist_files = [
                "subdomains-small.txt",
                "subdomains-top1mil-20000.txt",
                "subdomains-top1mil-5000.txt",
                "subdomains-top1mil.txt"
            ]

            if wordlist_option in {"1", "2", "3", "4"}:
                start()
                print(f"{G}[{Y}i{G}] Option {R}{wordlist_option} {G}selected")
                print(f"{G}[{Y}i{G}] Now using the {R}{wordlist_files[int(wordlist_option) - 1]} {G}wordlist")
                print(f"{G}[{Y}i{G}] Starting subdomain enumeration on {R}{target}")
                print("")

                with open(wordlist_files[int(wordlist_option) - 1], "r") as file:
                    with ThreadPoolExecutor() as executor:
                        for line in file:
                            subdomain = line.strip()
                            executor.submit(check_subdomain, subdomain, target)
            else:
                start()
                print(f"{G}[{R}!{G}] You must choose a valid option")

    except KeyboardInterrupt:
        print(f"\n{G}[{R}!{G}] User aborted the script")
        exit()

if __name__ == "__main__":
    main()
