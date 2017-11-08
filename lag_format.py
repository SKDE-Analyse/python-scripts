#!/usr/bin/env python
# -*- coding: utf-8 -*-


def lagFormat():
    """Script for å lage sas-format-filer ut fra csv-fil TEST"""

    import sys
    import argparse
    from subprocess import call

    parser = argparse.ArgumentParser(description='Konvertere tekstfil til SAS format-fil')

    parser.add_argument('-i', dest='innfil',
                        help='Tekstfilen som skal konverteres')

    parser.add_argument('-o', dest='utfil',
                        help='Produsert SAS-formatfil')

    parser.add_argument('--behold', dest='behold', action='store_true',
                        default=False,
                        help='Behold også koden/første ord i format-teksten (standard: %(default))')

    parser.add_argument('--delim', dest='delim',
                        default='',
                        help='Mellomrom mellom ord i inputfil (standard er mellomrom)')

    args = parser.parse_args()

    filename = args.innfil
    alle = args.behold
    utfil = args.utfil

    infile = open(filename, "r")

    utTekst = "proc format;\n"
    utTekst += "value $" + filename.split(".")[0] + "F\n"

    k = 0
    for i in infile.readlines():
        linje = i.replace('\t', " ")
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
            newline = "'" + words[0].replace(" ", "") + "'" + '="' + text.replace('"', "'") + '"\n'
            utTekst += newline
        except IndexError:
            sys.stderr.write(i)

    infile.close()

    utTekst += '''
;
run
'''

    # utTekst = utTekst.encode("cp1252")

    utfil = open(args.utfil, "w", encoding='cp1252')  # , newline='\r\n')
    utfil.write(utTekst)
    utfil.close()

    # call(["iconv","-f","utf-8","-t","cp1252","--unicode-subst=''",args.utfil,">","tmp"], shell=True)
    # call(["mv","tmp",args.utfil])
    # call(["rm","tmp"])


if __name__ == '__main__':
    """ TEST """
    lag_format()
