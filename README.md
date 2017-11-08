[![Build Status](https://travis-ci.org/SKDE-Analyse/python-scripts.svg?branch=master)](https://travis-ci.org/SKDE-Analyse/python-scripts/builds)

# Samling med python script, SKDE

Sannsynligvis kun skrevet av Arnfinn

## Diverse kommandoer

```
python fix.py 2016_SPSS_Labels_52.0.2.txt > testing/52.0.2.txt
python fix.py 2015_SPSS_Labels_51.1.2.txt > testing/51.1.2.txt
python fix.py 2015_SPSS_Labels_51.1.1.txt > testing/51.1.1.txt
python fix.py 2014_SPSS_Labels_50.0.0.txt > testing/50.0.0.txt
python fix.py 2014_SPSS_Labels_50.0.1.txt > testing/50.0.1.txt
python fix.py 2013_SPSS_Labels_49.0.0.txt > testing/49.0.0.txt
python fix.py 2013_SPSS_Labels_49.0.1.txt > testing/49.0.1.txt
python fix.py 2012_SPSS_Labels\(48.0.1\).txt > testing/48.0.1.txt
python fix.py 2012_SPSS_Labels\(47.0.5\).txt > testing/47.0.5.txt
python fix.py 2011_SPSS_Labels\(47.0.3\).txt > testing/47.0.3.txt
python fix.py 2011_SPSS_Labels\(47.0.4\).txt > testing/47.0.4.txt
python fix.py 2011_SPSS_Labels\(47.0.6\).txt > testing/47.0.6.txt


# Lage formater av ICD og NC*M txt-filer


for i in 1 2 3 4 5; do python /e/ANALYSE/Data/python/script/lag_format.py -i 201${i}.txt --behold > /e/ANALYSE/Data/SAS/Formater/master/icd10/icd10_201${i}_medKode.sas; done


python /e/ANALYSE/Data/python/script/lag_format.py -i samlet.txt --behold > /e/ANALYSE/Data/SAS/Formater/master/icd10_medKode.sas


for i in 1 2 3 4 5; do for j in NCMP_201 NCSP_201; do python /e/ANALYSE/Data/python/script/lag_format.py -i ${j}${i}.txt --behold > /e/ANALYSE/Data/SAS/Formater/master/Prosedyrekoder/${j}${i}_medKode.sas; done; done
```
