#!/bin/bash
find ../ashtakas -maxdepth 1 -name "*.tex" -newer TaittiriyaBrahmanam-Ashtakams.pdf | while read fpath
do
fname=`basename $fpath`
echo "---------------------------------------------------------------"
echo "File path         : $fpath"
jobname=`echo $fpath | sed 's/.tex//;s@.*ashtakas/@@'`
echo "PDF target        : $jobname.pdf"
mkdir -p `dirname $jobname`
if [[ $fpath -nt $jobname.pdf || ashtaka-kindle-template.tex -nt $jobname.pdf ]]
then
echo Rebuilding $jobname.pdf... > /dev/stderr
echo Rebuilding $jobname.pdf...
cat ashtaka-kindle-template.tex | sed "s@FPATH@$fpath@" | xelatex -jobname=$jobname
else
echo PDF up-to-date.
fi
done > tex2pdf.log
