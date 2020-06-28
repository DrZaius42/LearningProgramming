#!/bin/bash
count=$1
sh $(pwd)/stderrorTest.sh
status=$?
while [ echo $status ]
do
	count=$(( $count + 1 ))
	sh $(pwd)/stderrorTest.sh
	status=$?
done
echo $count
