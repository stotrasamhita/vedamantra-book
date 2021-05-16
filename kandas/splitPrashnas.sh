#!/bin/bash
mkdir -p .old/
mv TaittiriyaSamhita-Kandam-*.tex TaittiriyaSamhita-[1234567]*.tex .old/
awk 'BEGIN{c=0; p=0}
/chapt/{c++;p=0}
/sect/{p++;}
/chapt/,/%%% END KANDAM/{print > "TaittiriyaSamhita-Kandam-" c ".tex"}
/sect/,/%%% END PRASHNA/{print > "TaittiriyaSamhita-" c "-" p ".tex"}' TaittiriyaSamhita-Kandas.tex
# rm TaittiriyaSamhita-*0.tex
cp  TaittiriyaSamhita-Kandas*.tex .old/
cd .old/
for x in *.tex; do diff $x ../$x -q && mv -v $x ../; done
#for x in *.tex; do diff $x ../$x -qs && mv -v $x ../; done
cd ..
