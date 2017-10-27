#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

filename = sys.argv[1]

infile = open(filename,"r")

bohf = "qwerty"
bohf_lang = "Helse qwerty HF"
first = True
innhold = ""
kommuner = ""

print(infile)

linjer = infile.readlines()

for i in linjer:
   words = i.split(";")
   if (bohf != words[0]) and not first:
      tmp = '''
Opptaksområde {0}
Bor i opptaksområde for {1}
Kortnavn opptaksområde: {0}
      
'''.format(bohf, bohf_lang.split("-")[0])
      utfiltekst = tmp + kommuner
      filnavn = bohf.replace(" ","")
      utfil = open(filnavn + ".txt", "w")
      utfil.write(utfiltekst)
      utfil.close()
      kommuner = ""
   kommuner += words[1] + "\n"
   if words[2] != ".":
      kommuner += "   " + words[2] + "\n"
   bohf_lang = words[3]
   bohf = words[0]
   first = False


tmp = '''
Opptaksområde {0}
Bor i opptaksområde for {1}
Kortnavn opptaksområde: {0}
      
'''.format(bohf, bohf_lang.split("-")[0])
utfiltekst = tmp + kommuner
filnavn = bohf.replace(" ","")
utfil = open(filnavn + ".txt", "w")
utfil.write(utfiltekst)
utfil.close()

print("test")

