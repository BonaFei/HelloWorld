#!/bin/bash

IFS=$'\n'
ls -a $PWD/*.mp4 > mp4
for i in `cat $PWD/mp4`
do
    ffmpeg -i $i -b:a 320k $i.mp3
done


ls -a $PWD/*.webm > webm
for j in `cat $PWD/webm`
do
    ffmpeg -i $j -b:a 320k $j.mp3
done
