#!/usr/bin/env python3
iplist = ["10.1.1.1", "10.2.2.2", "10.3.3.3"]

for ip in iplist:
    print(ip)

# open file in read mode
# dnsfile = open("dnsservers.txt", "r")
# create list of lines
# dnslist = dnsfile.readlines()
# loop over lines
# for svr in dnslist:
    #print and end without a newline
   #  print(svr, end="")
# close your file
# dnsfile.close()

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop over lines
    for svr in dnsfile:
        #print and end without a newline
        print(svr, end="")
# no need to close our file - closed automatically
        svr = svr.rstrip('\n')
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
