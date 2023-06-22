import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import zipfile

from time import sleep
import os
import subprocess

    #1. Spravit input pre VYBER Z MOZNOSTI
    #2. Po vybere nech sa spusti nejaka cast (NECH TO JE DALSI PYTHON SCRIPT ZVLAST)
    #3. 
    #4. 
    #5. 
    #6. 
    
# DEFKY FARBICIEK    
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
#orange = '\033[033m'
P = '\033[15m'  # purple
orange = '\033[38;5;208m'
magenta = '\033[35m'
cyan = '\033[36m'
reset = '\033[0m'

def MaILer_Logo():
    print(f"""
    + --------------------------------------------------------------------- +
    |   __  __           _____   _                                          |
    |  |  \/  |         |_   _| | |                                         |
    |  | \  / |   __ _    | |   | |        ___   _ __       _ __    _   _   |
    |  | |\/| |  / _` |   | |   | |       / _ \ | '__|     | '_ \  | | | |  |
    |  | |  | | | (_| |  _| |_  | |____  |  __/ | |     _  | |_) | | |_| |  |
    |  |_|  |_|  \__,_| |_____| |______|  \___| |_|    (_) | .__/   \__, |  |
    |                                                      | |       __/ |  |
    |                                                      |_|      |___/   |
    + --------------------------------------------------------------------- +
    """)

def EXITTING():
    print(f"""
          ------------------------------------------------
          ------------------( EXITTING )------------------
          ------------------------------------------------
          """)

sleep(1)
MaILer_Logo() + {orange}
sleep(2)
os.system("cls")
