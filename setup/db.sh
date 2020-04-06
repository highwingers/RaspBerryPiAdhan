#!/bin/bash
dir=${PWD%/*}
file=$dir/www/data/adhan.db

if [ -f "$file" ]
then
	echo "$file found."
	python3 $dir/www/lib/sqllite.py True
else
	python3 $dir/www/lib/sqllite.py False
fi

