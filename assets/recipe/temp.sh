#!/bin/bash

for img in `find . -iname '*.JPG' -o -iname '*.jpg' -type f`
do
	convert /home/jinho/Dropbox/Projects/Icc/assets/recipe/$img -resize 200x200
done
