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
	print(f"{G}[{B}!!!{G}] {Y}Tool-Name {G}: {C}Domainer")
	print(f"{G}[{B}!!!{G}] {Y}Github    {G}: {C}https://github.com/K3ysTr0K3R")
	print(f"{G}[{B}!!!{G}] {Y}Instagram {G}: {C}jaredbrts175")
	print(f"{G}[{B}!!!{G}] {Y}Coded By  {G}: {C}K3ysTr0K3R")
	print("")
start

try:
	connect_google = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	CONNECTION = connect_google.connect_ex(('www.google.com',80))
	if (CONNECTION == 0):
		print(f"{G}[{B}+++{G}] Internet Connection Established{B}: {C}Proceeding")
		print(f"{B}========================================================")
		start()
except socket.gaierror:
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
		if not server_name:
			print(f"{G}[{B}+{G}] {Y}{dns} {G}[{C}{ip_address}{G}] {G}[{M}No-Server{G}] [{response_code}]")
		else:
			print(f"{G}[{B}+{G}] {Y}{dns} {G}[{C}{ip_address}{G}] {G}[{M}{server_name}{G}] [{response_code}]")
	except socket.gaierror:
		print("")
	except requests.ConnectionError:
		print(f"{G}[{R}~{G}] {Y}{dns} {G}[{R}No-Subdomain{G}] {G}[{R}No-Server{G}] {G}[{R}No-Response-Code{G}]")

try:
	target = input(f"{G}[{Y}i{G}] {G}Insert your target domain here without www{B}: {R}")
	start()
	if (target == ""):
		print(f"{G}[{R}!{G}] You must insert your target domain")
		exit()
	else:
		print(f"{G}[{Y}i{G}] Starting subdomain enumeration on {R}{target}")
		print("")
	with open("subdomains.txt", "r") as file:
		with ThreadPoolExecutor() as executor:
			for line in file:
				subdomain = line.strip()
				executor.submit(check_subdomain, subdomain, target)
except KeyboardInterrupt:
	print(f"\n{G}[{R}!{G}] User aborted the script")
	exit()
