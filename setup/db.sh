#!/bin/bash
dir=${PWD%/*}
file=$dir/www/data/adhan.db
if [ -f "$file" ]
then
	echo "$file found."
else
	python3 $dir/www/data/db.py
fi

