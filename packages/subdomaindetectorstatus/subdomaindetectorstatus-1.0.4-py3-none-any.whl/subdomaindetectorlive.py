import csv
import os
import requests
from colorama import init
from termcolor import colored
import sys

def banner():
    print(colored("  __        __                  ___ ",'cyan'))
    print(colored(" /__` |  | |__) __ |    | \  / |__  ",'red'))
    print(colored(" .__/ \__/ |__)    |___ |  \/  |___ ",'green'))
    print("")
    print(colored("    Author: Hariharan\n",'green'))

def help():
    banner()
    print("Syntax = python3 subgen-live.py -d {domain} -org {organisation example: .com, .in, .edu, .gov.in, etc.,}\n")
    print("python3 subgen-live.py -d google -org .com\n")
def operation():
    print("")
    domain = sys.argv[2]
    print("")
    org = sys.argv[4]
    print("")
    with open('subdomain.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for line in csvreader:
            sub = line[0]
            url = ("https://"+sub+"."+domain+org)  #https://example.com
            print("")
            print(url)
            try:
                r = requests.get(url, allow_redirects=False)
                code = r.status_code
                stat = url + "   <---- [ {} ]".format(r.status_code)
                print(stat)
                f = open(domain+".txt", "a+")
                f.write(stat+ '\n')
            except:
                print("URL not found")

if (len(sys.argv)<=1):
    os.system("clear")
    banner()
    print("Try python3 subgen-live.py -h or --help\n")
    sys.exit()

if (str(sys.argv[1]) == "-h" or str(sys.argv[1]) =="--help"):
    help()
    sys.exit()

if (str(sys.argv[1]) == "-d") and (str(sys.argv[3]) == "-org"):
    banner()
    operation()
    sys.exit()
