#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import codecs

sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')

svarita = '॑'
visarga = 'ः'
anudatta = '॒'
# print(svarita+visarga)


for fname in sys.argv[1:]:
    mantraFile = open(fname, encoding="utf8")

    outFile = open(fname[:-4]+'-new.tex', 'w')

    for i, line in enumerate(mantraFile.readlines()):
        if line.find(visarga+svarita) != -1 or line.find(visarga+anudatta) != -1:
            #print (i+1)
            pos = line.find(visarga+svarita)
            while pos != -1:
                line = line[:pos] + svarita + visarga + line[pos+2:]
                pos = line.find(visarga+svarita)
            pos = line.find(visarga+anudatta)
            while pos != -1:
                line = line[:pos] + '!' + anudatta + visarga + line[pos+2:]
                # Because this does not work properly, we use an ! to alert
                pos = line.find(visarga+anudatta)
            outFile.write(line)
        else:
            outFile.write(line)

    outFile.close()