#!/usr/bin/env python
# The previous line ensures that this script is run under the context
# of the Python interpreter. Next, import the Scapy functions:
from scapy.all import *

import sys, re, time, random, argparse, logging
from argparse import ArgumentParser

parser = ArgumentParser(description='SSID spammer/fuzzer')
parser.add_argument('-i', metavar='interface', action="store", default=False, help='wireless interface', required=True)
args = parser.parse_args()

interface = args.i

conf.iface= interface
words = [line.strip() for line in open('/etc/dictionaries-common/words')]

ssid=	"example"	#we will try to fuzz this field
rates=""

def createSSID():
  "This creates a fake ssid and tries to connect. If successful, returns true"
  word1="'"
  word2="'"
  while "'" in word1:
    word1=(random.choice(words))
    print word1
  while "'" in word2:
    word2=(random.choice(words))
    print word2
  essid=str(word1)+""+str(word2)
  print str(essid)
  return essid  

def sendSSID(ssid):
#this link was very helpful in figuring some of this out: https://www.trustwave.com/Resources/SpiderLabs-Blog/Smuggler---An-interactive-802-11-wireless-shell-without-the-need-for-authentication-or-association/
  snd_addr=RandMAC()._fix()
  print str(snd_addr)
  i=0
  while i < 20:
    newtime = time.time()
    #TODO: Add code to randomly generate non-ascii ssid if option is chosen, but code is here for testing
    #ssid="\x00"*255
    sendp(RadioTap()/Dot11(addr1="ff:ff:ff:ff:ff:ff",addr2=str(snd_addr),addr3=str(snd_addr))/Dot11Beacon(timestamp=newtime,cap="ESS")/Dot11Elt(ID="SSID",len=len(ssid),info=ssid)/Dot11Elt(ID="Rates",info="\x01\x08\x82\x84\x8b\x96\x0c\x12\x18\x24")/Dot11Elt(ID="DSset",info="\x0B")/Dot11Elt(ID="TIM",info="\x00\x01\x00\x00")/Dot11Elt(ID=42,info="\x00")/Dot11Elt(ID="ESRates",info="\x30\x48\x60\x6c")/Dot11Elt(ID=221,info="\x00\x50\xf2\x02\x01\x01\x8a\x00\x03\xa4\x00\x00\x27\xa4\x00\x00\x42\x43\x5e\x00\x62\x32\x2f\x00")/Dot11Elt(ID=221,info="\x00\x03\x7f\x01\x01\x00\x00\xff\x7f")/Dot11Elt(ID=221,info="\x00\x50\xf2\x04\x10\x4a\x00\x01\x10\x10\x44\x00\x01\x01\x01\x10\x49\x00\x14\x00\x24\xe2\x60\x02\x00\x01\x01\60\x00\x00\x02\x00\x01\x60x\01\x01\x00\x02\x00\x01"),verbose=0)
    i+=1

while True:
  ssid=createSSID()
  sendSSID(str(ssid))
