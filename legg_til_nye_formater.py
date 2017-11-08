def legg_til_nye_formater():
    """
Funksjon for å legge inn nye formater til eksisterende format-filer.
Brukes for å oppdatere årlig formater for NCxP og ICD10-koder.

Scriptet brukes på følgende måte:
```
python legg_til_nye_formater.py --original <originalfil> --ny <nye formater> --ut <>
```
    """

    import sys
    import argparse
    from subprocess import call
    import time

    parser = argparse.ArgumentParser(description='Konvertere tekstfil til SAS format-fil')

    parser.add_argument('--original', dest='original',
                        help='Originalfilen')

    parser.add_argument('--ny', dest='nyfil',
                        help='Nye formater')

    parser.add_argument('--ut', dest='ut',
                        help='Originalfil som også inneholder nye formater')

    args = parser.parse_args()

    original = open(args.original, "r")
    nye = open(args.nyfil, "r")

    org_linjer = original.readlines()
    nye_linjer = nye.readlines()

    original.close()
    nye.close()

    gml_verdi = []
    for i in org_linjer[2:]:
        gml_verdi.append(i.split("=")[0])

    innhold = "/*Nye formater fra fil {fil} lagt til {dato} */\n".format(fil=args.nyfil, dato=time.strftime("%d/%m/%Y"))
    for i in nye_linjer[2:]:
        ny_verdi = i.split("=")
        try:
            if (ny_verdi[0] not in gml_verdi) and (ny_verdi[1].strip() != '""'):
                innhold += i
        except IndexError:
            pass

    if (args.ut):
        ut = open(args.ut, "w")
        ut.write(innhold)
        ut.close()
    else:
        original = open(args.original, "a")
        original.write(innhold)
        original.close()


if __name__ == '__main__':
    legg_til_nye_formater()
