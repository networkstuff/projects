# an import of the OS module is done to allow to run the commands of linux
import os

# A prompt will appear asking for the phishing site
phishing_site = input("what is the phishing site?:\n ")

# this will send 3 pings to the phishing site from the given input above, Once this is done
# a filter is applied to give the first 4 lines then filter once more to give out the last line
# from here a redirection is done to the file phishingip.txt
a = os.system(f'ping -c 3 {phishing_site} | head --lines 4 | tail -1 > phishingip.txt')
# the whois is used to give us the abuseinformation and redirect the results to abuseinformation.txt
os.system(f'whois {phishing_site} | grep abuse > abuseinformation.txt')
#a print is done to tell the user that the python script is done
print("commands are done")


#####################################################################


#/bin/bash


wait

mkdir phishing

wait

mv phishingip.txt > phishing

wait

mv abuseinformation.txt > phishing
