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
	print(f"{G}[{B}!!!{G}] {Y}Instagram {G}: {C}jaredbrts175")
	print(f"{G}[{B}!!!{G}] {Y}Coded By  {G}: {C}K3ysTr0K3R")
	print("")
start

try:
	connect_google = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	CONNECTION = connect_google.connect_ex(('www.google.com',80))
	if (CONNECTION == 0):
		print(f"{B}========================================================")
		print(f"{G}[{B}+++{G}] Internet Connection Established{B}: {C}Proceeding")
		print(f"{B}========================================================")
		start()
except socket.gaierror:
	print(f"{B}========================================================")
	print(f"{G}[{R}!!!{G}] No Internet Connection Found{B}: {R}Exiting")
	print(f"{B}========================================================")
	exit()

def check_subdomain(subdomain, target):
	dns = subdomain + "." + target
	try:
		send_get_req = requests.get(f"http://{dns}")
		server = send_get_req.headers
		ip_address = socket.gethostbyname(dns)
		server_name = server.get("Server")
		response_code = send_get_req.status_code
		if server_name:
			print(f"{G}[{B}+{G}] {Y}{dns} {G}[{C}{ip_address}{G}] {G}[{M}{server_name}{G}] {G}[{C}{response_code}{G}]")
	except socket.gaierror:
		print("")
	except requests.ConnectionError:
		pass

try:
	target = input(f"{G}[{Y}i{G}] {G}Insert your target domain here without www{B}: {R}")
	start()
	if (target == ""):
		print(f"{G}[{R}!{G}] You must insert your target domain")
		exit()
	else:
		wordlist_option = input(f"""{G}[{M}1{G}] {M}subdomains-small.txt
{G}[{M}2{G}] {M}subdomains-top1mil-20000.txt
{G}[{M}3{G}] {M}subdomains-top1mil-5000.txt
{G}[{M}4{G}] {M}subdomains-top1mil.txt

{G}[{Y}i{G}] First things first, pick an option for the wordlist you want to use for {R}{target}{B}: """)
		if (wordlist_option == "1"):
			start()
			print(f"{G}[{Y}i{G}] Option {R}{wordlist_option} {G}selected")
			print(f"{G}[{Y}i{G}] Now using the {R}subdomains-small.txt {G}wordlist")
			print(f"{G}[{Y}i{G}] Starting subdomain enumeration on {R}{target}")
			print("")
			with open("subdomains-small.txt", "r") as file:
				with ThreadPoolExecutor() as executor:
					for line in file:
						subdomain = line.strip()
						executor.submit(check_subdomain, subdomain, target)

		elif (wordlist_option == "2"):
			start()
			print(f"{G}[{Y}i{G}] Option {R}{wordlist_option} {G}selected")
			print(f"{G}[{Y}i{G}] Now using the {R}subdomains-top1mil-20000.txt {G}wordlist")
			print(f"{G}[{Y}i{G}] Starting subdomain enumeration on {R}{target}")
			print("")
			with open("subdomains-top1mil-20000.txt", "r") as file:
				with ThreadPoolExecutor() as executor:
					for line in file:
						subdomain = line.strip()
						executor.submit(check_subdomain, subdomain, target)
		
		elif (wordlist_option == "3"):
			start()
			print(f"{G}[{Y}i{G}] Option {R}{wordlist_option} {G}selected")
			print(f"{G}[{Y}i{G}] Now using the {R}subdomains-top1mil-5000.txt {G}wordlist")
			print(f"{G}[{Y}i{G}] Starting subdomain enumeration on {R}{target}")
			print("")
			with open("subdomains-top1mil-5000.txt", "r") as file:
				with ThreadPoolExecutor() as executor:
					for line in file:
						subdomain = line.strip()
						executor.submit(check_subdomain, subdomain, target)
						
		elif (wordlist_option == "4"):
			start()
			print(f"{G}[{Y}i{G}] Option {R}{wordlist_option} {G}selected")
			print(f"{G}[{Y}i{G}] Now using the {R}subdomains-top1mil.txt {G}wordlist")
			print(f"{G}[{Y}i{G}] Starting subdomain enumeration on {R}{target}")
			print("")
			with open("subdomains-top1mil.txt", "r") as file:
				with ThreadPoolExecutor() as executor:
					for line in file:
						subdomain = line.strip()
						executor.submit(check_subdomain, subdomain, target)
		else:
			start()
			print(f"{G}[{R}!{G}] You must choose an option")
except KeyboardInterrupt:
	print(f"\n{G}[{R}!{G}] User aborted the script")
	exit()
