#!/bin/bash
find ../mantras -name "*.tex" | while read fpath
do
fname=`basename $fpath`
echo "---------------------------------------------------------------"
echo "File path         : $fpath"
jobname=`echo $fpath | sed 's/.tex//;s@.*mantras/@@'`
echo "PDF target        : $jobname.pdf"
mkdir -p `dirname $jobname`
if [[ $fpath -nt $jobname.pdf || mantra-kindle-template.tex -nt $jobname.pdf ]]
then
echo Rebuilding $jobname.pdf... > /dev/stderr
echo Rebuilding $jobname.pdf...
cat mantra-kindle-template.tex | sed "s@FPATH@$fpath@" | xelatex -jobname=$jobname
else
echo PDF up-to-date.
fi
done > tex2pdf.log
