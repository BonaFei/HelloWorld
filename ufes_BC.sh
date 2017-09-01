#!/bin/bash

cat /dev/null > $PWD/ufes_BC

for i in `cat $PWD/pool`
    do
		for j in `cat $PWD/LbList`
			do
				cat $j.conf | grep $i | grep add | grep -v bind  >> ufes_BC
				echo "" >> ufes_BC
			done
	done
