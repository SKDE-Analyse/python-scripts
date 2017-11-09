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

    nytt_innhold_dato = "/*Nye formater fra fil {fil} lagt til {dato} */\n".format(fil=args.nyfil, dato=time.strftime("%d/%m/%Y"))
    nytt_innhold = ""
    for i in nye_linjer[2:]:
        ny_verdi = i.split("=")
        try:
            if (ny_verdi[0] not in gml_verdi) and (ny_verdi[1].strip() != '""') and (ny_verdi[1].strip() != ny_verdi[0].replace("'", '"')):
                nytt_innhold += i
        except IndexError:
            pass

    if nytt_innhold != "":

        if (args.ut):
            # Legg nye koder inn i egen fil
            ut = open(args.ut, "w")
            ut.write(nytt_innhold_dato + nytt_innhold)
            ut.close()
        else:
            # Legg til nye koder i gammel fil
            innhold = ""
            for i in org_linjer[0:2]:
                innhold += i
            for i in org_linjer[2:]:
                if i.strip() not in [";", "run;"]:
                    innhold += i
            innhold += nytt_innhold_dato + nytt_innhold
            innhold += """
;
run;
"""
            original = open(args.original, "w")
            original.write(innhold)
            original.close()


if __name__ == '__main__':
    legg_til_nye_formater()
