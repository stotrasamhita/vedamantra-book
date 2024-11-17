#!/bin/bash
mkdir -p .old/
mv TaittiriyaBrahmanam-Ashtakam-*.tex TaittiriyaBrahmanam-[123]*.tex Achchhidrashvamedha.tex .old/
awk 'BEGIN{c=0; p=0}
/chapt/{c++;p=0}
/sect/{p++;}
/chapt/,/%%% END ASHTAKAM/{print > "TaittiriyaBrahmanam-Ashtakam-" c ".tex"}
/sect/,/prashnaend/{print > "TaittiriyaBrahmanam-" c "-" p ".tex"}' TaittiriyaBrahmanam-Ashtakams.tex
cat TaittiriyaBrahmanam-3-[789].tex > Achchhidrashvamedha.tex
cd .old/
for x in *.tex; do diff $x ../$x -q && mv $x ../; done
#for x in *.tex; do diff $x ../$x -qs && mv -v $x ../; done
cd ..
