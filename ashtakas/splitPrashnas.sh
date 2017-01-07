#!/bin/bash
cp *.tex .old/
awk 'BEGIN{c=0; p=0}
/chapt/{c++;p=0}
/sect/{p++;}
/chapt/,/%%% END ASHTAKAM/{print > "TaittiriyaBrahmanam-Ashtakam-" c ".tex"}
/sect/,/prashnaend/{print > "TaittiriyaBrahmanam-" c "-" p ".tex"}' TaittiriyaBrahmanam-Ashtakams.tex
cd .old/
for x in *.tex; do diff $x ../$x -qs && mv -v $x ../; done
cd ..
