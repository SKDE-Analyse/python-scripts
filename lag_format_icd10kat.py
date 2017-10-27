import sys
import roman

# gi to argumenter: input-fil og nivå man vil ha 
# formater for (0-3). Nivå 3 vil gi både nivå 2 og 3.

filename = sys.argv[1]

infile = open(filename,"r")
niva = sys.argv[2]

print("proc format;")
if niva == '0':
    formatNavn = 'ICD10kap2016F'
elif niva == '1':
    formatNavn = 'ICD10katblokk2016F'
    k = 0
else:
    formatNavn = sys.argv[1].split(".")[0]+"F"
print("value $"+formatNavn)

for i in infile.readlines():
    try:
        words = i.split(";")
        text = words[1]
        if text != "" and words[2] == niva:
            if niva == '0':
                print(str(roman.fromRoman(words[0].split()[1])) + '="' + words[0] + ": " + text + '"')
            elif niva == '1':
                k += 1
                print(str(k) + "='" + words[0].replace("(","").replace(")","") + " " + text + "'")
            else:
                print("'" + words[0].replace(".","") + "'" + '="' + words[0] + ": " + text + '"')
    except:
        sys.stderr.write(i)

print(";")
print("run;")

