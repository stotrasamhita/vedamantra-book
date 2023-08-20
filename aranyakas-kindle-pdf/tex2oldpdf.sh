#!/bin/bash
find ../aranyakas -name "*.tex" | while read fpath
do
fname=`basename $fpath`
echo "---------------------------------------------------------------"
echo "File path         : $fpath"
jobname=`echo $fpath | sed 's/.tex//;s@.*aranyakas/@@'`
echo "PDF target        : $jobname.pdf"
mkdir -p `dirname $jobname`
if [[ $fpath -nt $jobname.pdf || aranyaka-oldkindle-template.tex -nt $jobname-old.pdf ]]
then
echo Rebuilding $jobname-old.pdf... > /dev/stderr
echo Rebuilding $jobname-old.pdf...
cat aranyaka-oldkindle-template.tex | sed "s@FPATH@$fpath@" | xelatex -jobname=$jobname-old
else
echo PDF up-to-date.
fi
done > tex2pdf.log
