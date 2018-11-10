#!/bin/sh

DATE=`date +%Y-%m-%d`
echo $DATE

git add --all
git commit -am "${DATE} lesson"

git push
