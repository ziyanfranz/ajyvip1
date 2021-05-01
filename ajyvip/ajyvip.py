#!/bin/python


#import module yang di butuhkan
import os
import random
import sys
import time
import getpass
from time import sleep
def arya(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

#username
x = "skuy"
#password
y = "arya"

def login():
 os.system("clear")
 arya("'\033[1;97m'+-------------------------------------------------------+")
 arya(" |            \033[1;94m       hallo   KIMAK     \033[1;97m                  |")
 arya(" +---------------------------+---------------------------+")
 arya(" |\033[1;93m      __________________   | \033[1;91m       ss               \033[1;97m   |")
 arya(" |\033[1;93m  ==c(______(o(______(_()  | \033[1;91m|------------|======[    \033[1;97m |")
 arya(" |\033[1;93m             )=\           | \033[1;91m|  EXPLOIT   \           \033[1;97m |")
 arya(" |\033[1;93m            // \\           | \033[1;91m|_____________\_______   \033[1;97m |")
 arya(" |\033[1;93m           //   \\          | \033[1;91m|==[msf >]============\   \033[1;97m|")
 arya(" |\033[1;93m          //     \\         | \033[1;91m|______________________\  \033[1;97m|")
 arya(" |\033[1;93m         // RECON \\        | \033[1;91m\(@)(@)(@)(@)(@)(@)(@)/  \033[1;97m |")
 arya(" |\033[1;93m        //         \\       |  \033[1;91m*********************   \033[1;97m |")
 arya("\033[1;97m +---------------------------+---------------------------+")
 arya("\033[1;97m |\033[1;96m      o O o                '\033[1;97m'|        \'\/\/\/'/         \033[1;97m |")
 arya("\033[1;97m |\033[1;96m              o O          '\033[1;97m'|         )======(          \033[1;97m|")
 arya("\033[1;97m |\033[1;96m                 o         '\033[1;97m'|       .'  LOOT  '.        \033[1;97m|")
 arya("\033[1;97m |\033[1;96m |^^^^^^^^^^^^^^|l___      '\033[1;97m'|      /    _||__   \       \033[1;97m|")
 arya(" \033[1;97m|\033[1;96 |    PAYLOAD     |""\___,  '\033[1;97m' |     /    (_||_     \      \033[1;97m|")
 arya("\033[1;97m | \033[1;96|________________|__|)__| '\033[1;97m'|    |     __||_)     |    \033[1;97m |")
 arya("\033[1;97m | \033[1;96|(@)(@)**|(@)(@)**|(@)    '\033[1;97m'|            ||             \033[1;97m|")
 arya(" \033[1;97m|  = = = = = = = = = = = =  |     '--------------'      \033[1;97m|")
 arya(" +---------------------------+---------------------------+\033[1;97m")
 arya(" =====================\033[1;95m<\033[1;97mLOGIN DULU ZEYENG\033[1;97m===================")
 username = raw_input(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mUsername:\033[1;92m ")
 password = getpass.getpass(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mPassword: ")
 if username == x and password == y:
   print(" \033[1;92mAccess Grented")
   time.sleep(1)
 else:
    print(" \033[1;91mAccess Denied")
    time.sleep(1)
    login()

login()

def warning():
 os.system("clear")
 arya("AUTHOR : ARYA N")
 arya("    WARNING")
 arya("dilarang menyalah gunakan tools ini")
 time.sleep(3)
 os.system("clear")
 print ("loading")
 arya("> > > > > > > > > > > > > > > > > > >]100%")

warning()

def menu():
 os.system("clear")
 arya(" _____________________________________________________________________________")
 arya("|                                                                              |")
 arya("|                   CYBER SCURITY INDONESIA                                    |")
 arya("|______________________________________________________________________________|")
 arya(" 1. HACK CCTV")
 arya(" 2. Retas Ponsel")
 arya(" 3. Spam Brutal")
 arya(" 4. exit/keluar")

 pilih = raw_input("Select@number> ")

 if pilih =="1":
     os.system("clear")
     arya(" MENDOWNLOAD TOOLS.....")
     time.sleep(2)
     arya("> > > > > > > > > > > > > > > >]100%"
     os.system('python2 scan.py')

 elif pilih =="2":
      os.system("clear")
      arya(" SEGERA ADA...")

 elif pilih =="3":
       os.system("clear")
       os.system("python dark_brutal.py")

 elif pilih =="4":
       arya(" Good bye ")

 else:
      arya("PILIH YANG BENER!!!")
      menu()

menu()
