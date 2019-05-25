# Mac_Modifier
Mac_Modifier is a designed tool to change the mac address for any linux based operating system


#Requirements to Run the tool on kali linux:

Open kali linux terminal 

type "apt-get update" give enter

and

type "apt-get install figlet"


#Requirements to run tool on ubuntu:

open terminal on ubuntu

type "apt-get update"  then give enter

then 

type "apt-get install figlet" then give enter

and then 

type "apt install python-pip" then give enter


then download the tool run ./macmodifier.py --help  
this will show you how to use this tool.

How to change the mac address by user defined mac address by using macmodifier tool:

./macmodifier.py -i eth0 -m 00:11:22:33:44:55       (interface may be eth0 or wlan0) it depends up on your wish.

the above command can change your mac address on eth0 interface

-i - represent interface name

-m - represent mac address that you want to change

How to change the mac address randomly for any interface:

./macmodifier.py -i eth0 -r 0

the command which can change the mac address for my eth0 interface, but on this option it randomly picks a mac address where i have kept a list inside my tool and it assigned to the interface.

-r - mentions the random mac address option 

-r 0 - this flag contains the value is 0(zero) which enables the random mac changing.




