#!/bin/sh

for i in `cat $PWD/downloadList`
do
    youtube-dl -F $i >> $PWD/format
    tail -n 1 format | awk '{print $1}' > $PWD/best
    j=`cat $PWD/best`
    echo 'Best Format is: ' $j
    youtube-dl -f $j $i
done
