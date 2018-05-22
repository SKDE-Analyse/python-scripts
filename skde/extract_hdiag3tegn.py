#!/usr/bin/env python


def extract_hdiag3tegn():
    """Extract Hdiag3tegn from a ICD-10 text file

    The text file is copy-and-pasted from a pdf, and
    contains all the ICD-10 codes.
    """
    import sys
    import re

    file = open(sys.argv[1], "r")

    lines = file.readlines()

    newfile = '''proc format;
value $hdiag3tegn
'''

    for i in lines:
        if re.match(r'[A-Z][0-9][0-9] ', i[0:5]):
            newfile += "'{0}'=".format(i.split()[0]) + '"{0}"'.format(i.rstrip()) + "\n"

    newfile += ''';
run;
'''
    print(newfile)


if __name__ == '__main__':
    extract_hdiag3tegn()
