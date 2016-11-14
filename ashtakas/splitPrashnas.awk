#!/usr/bin/awk -f
BEGIN{c=0; p=0}
/chapt/{c++;p=0}
/sect/{p++;}
/chapt/,/%%% END ASHTAKAM/{print > "TaittiriyaBrahmanam-Ashtakam-" c ".tex"}
/sect/,/prashnaend/{print > "TaittiriyaBrahmanam-" c "-" p ".tex"}