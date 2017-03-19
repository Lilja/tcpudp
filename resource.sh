#!/bin/bash
files="100 1000 10000 100000 1000000 10000000 100000000"

test ! -d res && mkdir res
for file in $files
do
	test ! -f "res/${file}.res" && dd if=/dev/zero of="res/${file}.res" bs="${file}" count=1 || exit 0
done
