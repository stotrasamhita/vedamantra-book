#!/bin/bash
find ../kandas -maxdepth 1 -name "*.tex" -newer TaittiriyaSamhita-Kandas.pdf | while read fpath
do
fname=`basename $fpath`
echo "---------------------------------------------------------------"
echo "File path         : $fpath"
jobname=`echo $fpath | sed 's/.tex//;s@.*kandas/@@'`
echo "PDF target        : $jobname.pdf"
mkdir -p `dirname $jobname`
if [[ $fpath -nt $jobname.pdf || kanda-kindle-template.tex -nt $jobname.pdf ]]
then
echo Rebuilding $jobname.pdf... > /dev/stderr
echo Rebuilding $jobname.pdf...
cat kanda-kindle-template.tex | sed "s@FPATH@$fpath@" | xelatex -jobname=$jobname
else
echo PDF up-to-date.
fi
done > tex2pdf.log
