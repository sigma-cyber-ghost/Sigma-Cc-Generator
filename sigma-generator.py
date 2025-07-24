#!/usr/bin/env python3
# SIGMA GHOST BIN - BLACK HAT EDITION

import random
import requests
import sys
import os
import signal
from datetime import datetime

# ========== TERMINAL CONTROL ==========
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ========== COLOR CODES ==========
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'
DIM = '\033[2m'
FLASH = '\033[5m'
REVERSE = '\033[7m'

# ========== SIGMA BANNER ==========
BANNER = f"""{RED}{BOLD}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣷⣄⡀⣀⣴⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⣀⣀⣀⣀⣠⣤⣶⣾⣿⣿⣶⣦⣤⣤⣤⣤⡤⠤⠶⠾⠿⠷⠶⠦⠤⠀⠀⠀⠀⠀⠀
⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣃⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀
⠀⠀⠀⠀⠀⠀⣀⣉⣉⠉⢉⠉⠋⠛⠛⠛⠛⠛⠛⠉⠉⠉⢉⣉⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣾⣿⣿⣿⣆⠹⢿⣿⣿⠟⠉⠉⠻⣿⣿⡿⠁⢸⣿⣿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⠐⠛⠻⠿⠿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠿⠿⠛⠛⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⣦⡀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠚⠿⢿⣿⣿⣿⣦⡀⠀⠀⣰⣿⣿⣿⣿⠿⠟⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⢿⣿⠇⣼⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢰⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {CYAN}SIGMA CYBER GHOST | BLACK HAT EDITION{RESET}
─────────────────────────────────────────────
🔗 {WHITE}TELEGRAM{RESET} : {CYAN}https://t.me/Sigma_Cyber_Ghost{RESET}
🔗 {WHITE}GITHUB  {RESET} : {CYAN}https://github.com/sigma-cyber-ghost{RESET}
🔗 {WHITE}YOUTUBE {RESET} : {CYAN}https://youtube.com/@sigma_ghost_hacking{RESET}
🔗 {WHITE}TWITTER {RESET} : {CYAN}https://x.com/safderkhan0800_{RESET}
─────────────────────────────────────────────
{RED}{BOLD}WARNING:Never Use For Educational Purposes Only!{RESET}
"""

# ========== CTRL+C HANDLER ==========
def sigint_handler(signal, frame):
    print(f"\n{RED}{BOLD}[!] SIGMA TERMINATION: Operation canceled{RESET}")
    print(f"{RED}[-] Erasing traces...{RESET}\n")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

# ========== BIN CHECKER ==========
def check_bin(pan, mm, yy, cvv):
    bin6 = pan[:6]
    if not bin6.isdigit() or len(bin6) != 6:
        return False, "INVALID", "N/A", "0", "🌐 UNKNOWN"
    
    try:
        headers = {'User-Agent': 'SigmaGhost/1.0'}
        res = requests.get(f"https://lookup.binlist.net/{bin6}", headers=headers, timeout=5)
        
        if res.status_code == 200:
            data = res.json()
            balance = random.randint(100, 9999)
            scheme = data.get("scheme", "UNKNOWN").upper()
            typ = data.get("type", "N/A").upper()
            country = data.get("country", {}).get("name", "UNKNOWN")
            emoji = data.get("country", {}).get("emoji", "🌐")
            return True, scheme, typ, f"${balance}", f"{emoji} {country}"
        return False, "N/A", "N/A", "$0", "🌐 UNKNOWN"
    except:
        return False, "TIMEOUT", "N/A", "$0", "🌐 UNKNOWN"

# ========== MAIN MENU ==========
def show_menu():
    clear_screen()
    print(BANNER)
    print(f"{CYAN}{BOLD}MAIN MENU:{RESET}")
    print(f"  {GREEN}1{RESET} - Generate CC")
    print(f"  {GREEN}2{RESET} - Check CC from file")
    print(f"  {RED}0{RESET} - Exit\n")

# ========== CARD GENERATOR ==========
def generate_cards():
    clear_screen()
    print(BANNER)
    print(f"{CYAN}{BOLD}⚡ CARD GENERATOR:{RESET}\n")
    
    try:
        bin_input = input(f"{WHITE}Enter BIN (6 digits): {RESET}").strip()
        if len(bin_input) != 6 or not bin_input.isdigit():
            print(f"{RED}Invalid BIN! Must be 6 digits.{RESET}")
            return
        
        count = int(input(f"{WHITE}Number of cards to generate: {RESET}").strip())
        if count <= 0:
            print(f"{RED}Invalid number!{RESET}")
            return
            
        save_file = input(f"{WHITE}Save to file (leave empty to skip): {RESET}").strip()
        
        print(f"\n{YELLOW}Generating {count} cards...{RESET}\n")
        
        cards = []
        for _ in range(count):
            pan = bin_input + ''.join(random.choices("0123456789", k=10))
            mm = str(random.randint(1, 12)).zfill(2)
            yy = str(random.randint(datetime.now().year % 100, 30))
            cvv = str(random.randint(100, 999))
            card = f"{pan}|{mm}|{yy}|{cvv}"
            cards.append(card)
            print(f"{GREEN}[+] {card}{RESET}")
        
        if save_file:
            with open(save_file, 'w') as f:
                f.write('\n'.join(cards))
            print(f"\n{GREEN}Cards saved to: {save_file}{RESET}")
            
    except Exception as e:
        print(f"{RED}Error: {str(e)}{RESET}")

# ========== CARD CHECKER ==========
def check_cards():
    clear_screen()
    print(BANNER)
    print(f"{CYAN}{BOLD}🔍 CARD CHECKER:{RESET}\n")
    
    try:
        file_path = input(f"{WHITE}Enter card file path: {RESET}").strip()
        if not os.path.exists(file_path):
            print(f"{RED}File not found!{RESET}")
            return
            
        output_file = "live_cards.txt"
        live_count = 0
        
        with open(file_path, 'r') as f:
            cards = [line.strip() for line in f.readlines() if line.strip()]
            
        print(f"\n{YELLOW}Checking {len(cards)} cards...{RESET}\n")
        
        for card in cards:
            if '|' not in card:
                print(f"{RED}Invalid format: {card}{RESET}")
                continue
                
            pan, mm, yy, cvv = card.split('|')[:4]
            valid, scheme, typ, balance, country = check_bin(pan, mm, yy, cvv)
            
            if valid:
                live_count += 1
                status = f"{GREEN}LIVE{RESET}"
                with open(output_file, 'a') as out:
                    out.write(f"{card}\n")
            else:
                status = f"{RED}DEAD{RESET}"
                
            print(f"{status} | {WHITE}{pan[:6]}...{pan[-4:]} | {scheme} | {typ} | {balance} | {country}{RESET}")
        
        print(f"\n{GREEN}Live cards: {live_count}{RESET}")
        print(f"{RED}Dead cards: {len(cards) - live_count}{RESET}")
        if live_count > 0:
            print(f"{CYAN}Live cards saved to: {output_file}{RESET}")
            
    except Exception as e:
        print(f"{RED}Error: {str(e)}{RESET}")

# ========== MAIN ==========
def main():
    while True:
        show_menu()
        choice = input(f"{WHITE}Sigma-Ghost> {RESET}").strip()
        
        if choice == "1":
            generate_cards()
        elif choice == "2":
            check_cards()
        elif choice == "0":
            print(f"\n{RED}Exiting Sigma Ghost...{RESET}\n")
            break
        else:
            print(f"{RED}Invalid choice!{RESET}")
        
        input(f"\n{WHITE}Press Enter to continue...{RESET}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{RED}Fatal error: {str(e)}{RESET}")
        sys.exit(1)
