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
    import codecs

    parser = argparse.ArgumentParser(description='Konvertere tekstfil til SAS format-fil')

    parser.add_argument('--original', dest='original',
                        help='Originalfilen')

    parser.add_argument('--ny', dest='nyfil',
                        help='Nye formater')

    parser.add_argument('--ut', dest='ut',
                        help='Originalfil som også inneholder nye formater')

    parser.add_argument('--value', dest='value',
                        help='Formatverdi (value i andre linje)')

    args = parser.parse_args()

    org_encoding = get_encoding(args.original)
    ny_encoding = get_encoding(args.nyfil)

    original = codecs.open(args.original, "r", org_encoding)
    nye = codecs.open(args.nyfil, "r", ny_encoding)

    org_linjer = original.readlines()
    nye_linjer = nye.readlines()

    original.close()
    nye.close()

    gml_verdi = []
    for i in org_linjer[2:]:
        gml_verdi.append(i.split("=")[0])

    nytt_innhold_dato = "/* Formater fra fil {fil} lagt til {dato} */\n".format(fil=args.nyfil, dato=time.strftime("%d/%m/%Y"))
    nytt_innhold = ""
    for i in nye_linjer[2:]:

        ny_verdi = i.split("=")
        try:
            if (ny_verdi[0] not in gml_verdi) and (ny_verdi[1].strip() != '""') and (ny_verdi[1].strip() != ny_verdi[0].replace("'", '"')):
                nytt_innhold += i
        except IndexError:
            pass

    if nytt_innhold != "":

        innhold = ""
        for i in org_linjer[0:2]:
            if args.value and i.split()[0].lower() == "value":
                i = i.replace(i.split()[1], args.value)
            innhold += i
        for i in org_linjer[2:]:
            if i.strip() not in [";", "run;", "run"]:
                innhold += i
        innhold += nytt_innhold_dato + nytt_innhold
        innhold += """
;
run;
"""

        if (args.ut):
            # Legg koder inn i egen fil
            ut = codecs.open(args.ut, "w", "Windows-1252")
        else:
            # Legg koder til original-fil
            ut = codecs.open(args.original, "w", org_encoding)

        ut.write(innhold)
        ut.close()


def get_encoding(filename):

    from chardet.universaldetector import UniversalDetector

    detector = UniversalDetector()
    detector.reset()
    for line in open(filename, 'rb').readlines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()

    encoding = detector.result["encoding"]
    if detector.result["encoding"] in [None, "ascii"]:
        encoding = "Windows-1252"
    elif detector.result["encoding"] == "ISO-8859-1":
        encoding = "latin-1"

    print("Encoding for file {file} found to be {encode}, with confidence {confidence}. Encoding {rtrn} returned.".format(file=filename, encode=detector.result["encoding"], confidence=detector.result["confidence"], rtrn=encoding))
    return(encoding)


if __name__ == '__main__':
    legg_til_nye_formater()
