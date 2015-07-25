#!/bin/bash
find | grep pdf$ | awk -F '/' '
FNR==1{print ("\n### Suktas/Mantras")}
{	
	mantraName=$2
	sub(/.pdf/,"",mantraName)
	gsub(/[A-Z]/," &",mantraName)
	print ("*" mantraName, "[A5](https://github.com/stotrasamhita/vedamantra-book/raw/master/mantras-pdf/" $2 ")", "[Kindle PDF](https://github.com/stotrasamhita/vedamantra-book/raw/master/mantras-kindle-pdf/" $2 ")")
}'

