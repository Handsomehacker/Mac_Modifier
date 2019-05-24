#!/usr/bin/env python
import subprocess
import random
from pip._vendor.distlib.compat import raw_input
import optparse
import re

subprocess.call("figlet Mac_Modifier", shell=True)#cool printing
print("                                                     Created by Muthu")


def gettingargs():
    parse=optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="interface to change")
    parse.add_option("-m","--mac",dest="address",help="mac address to change")
    parse.add_option("-r","--random",dest="random",help="to mention you want to change the mac randomly")
    return parse.parse_args()

# interface=raw_input("Interface >>")
# address=raw_input("New Mac address >>")

# subprocess.call("ifconfig "+args.interface+" down", shell=True) #this put down your ethernet interface
# subprocess.call("ifconfig "+args.interface+" hw ether "+args.address,shell=True) #this have changed your mac address
# subprocess.call("ifconfig "+args.interface+" up",shell=True)

def checking_args(inter,add):
    if (args.interface):

        if (args.address and args.random):

            print(
                "[+] Either you can mention -m to use your manual mac address or you can use -r for random mac address")

        elif (args.address or args.random):

            if(args.random):

                random_mac_change()
            else:
                changing(args.interface,args.address)
        else:
            print("[+] mention mac address or use random mac address option")
    else:
        print("[+] Please mention the interface to change the mac address")
def changing(iface,addr):
    subprocess.call(["ifconfig",iface,"down"])
    subprocess.call(["ifconfig",iface,"hw","ether",addr])
    subprocess.call(["ifconfig",iface,"up"])
def checking_mac_changed():
    address_display=subprocess.check_output(["ifconfig",args.interface])
    extracted_address=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",address_display)
    # print(extracted_address.group(0))
    # print(args.address)
    if(args.random):

        print("[+] your mac address changed successfully")
        print("[+] your new mac address is "+ extracted_address.group(0))

    else:

        if(extracted_address.group(0)==args.address):
            print("[+] Your Mac Address successfully changed")
            print("[+] Your new mac address is "+ extracted_address.group(0))
        else:
            print("[+] No your Mac Address is not changed please check the format of your given mac address")

def random_mac_change():
    f=open("imp.txt","r")
    line=f.read().splitlines()
    #print(random.choice(line))
    three_oct=random.choice(line).strip()
    new_mac=three_oct+":22:33:44"
    changing(args.interface,new_mac)



(args,values)=gettingargs()
checking_args(args.interface,args.address)
checking_mac_changed()

