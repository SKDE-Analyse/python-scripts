import sys
import argparse

parser = argparse.ArgumentParser(description='Konvertere tekstfil til SAS format-fil')

parser.add_argument('-i', dest='innfil',
                    help='Tekstfilen som skal konverteres')

parser.add_argument('-o', dest='utfil',
                    help='Produsert SAS-formatfil')

parser.add_argument('--behold', dest='behold', action='store_true',
                    default=False,
                    help='Behold også koden/første ord i format-teksten (standard: %(default))')

parser.add_argument('--delim', dest = 'delim', 
                    default = '',
                    help = 'Mellomrom mellom ord i inputfil (standard er mellomrom)')


args = parser.parse_args()


filename = args.innfil
alle = args.behold
utfil = args.utfil


infile = open(filename,"r")

print("proc format;")
print("value $"+filename.split(".")[0]+"F")

k = 0
for i in infile.readlines():
    linje = i.replace('\t'," ")
    k += 1
    try:
        if args.delim != "":
            words = linje.split(args.delim)
        else:
            words = linje.split()
        if alle:
            text = linje.rstrip()
        else:
            text = " ".join(words[1:]).rstrip()
        newline = "'"+words[0].replace(" ", "")+"'"+'="'+text.replace('"',"'")+'"'
        print(newline)
    except:
        sys.stderr.write(i)

infile.close()

print(";")
print("run;")


