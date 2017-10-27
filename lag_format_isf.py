import sys


filename = sys.argv[1]

infile = open(filename,"r")

print("proc format;")
print("value $"+sys.argv[1].split(".")[0]+"F")

for i in infile.readlines():
    try:
        words = i.split(";")
        text = words[2]
        if text != "":
            newline = "'"+words[0].replace(" ", "")+"'"+'="DRG '+words[0].replace(" ", "")+" "+text+'"'
            print(newline)
    except:
        sys.stderr.write(i)

print(";")
print("run;")

