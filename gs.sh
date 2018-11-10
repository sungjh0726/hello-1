#!/bin/sh

DATE=`date +%Y-%m-%d`

git add --all
git commit -am "${DATE} lesson"

########## TTTTTTTTT

git push
