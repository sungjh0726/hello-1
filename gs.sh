#!/bin/sh

DATE=`date +%Y-%m-%d" "%H:%M`
MSG="$DATE lesson"
if [ $# -gt 0 ]; then
    MSG="$DATE - $1"
fi

git add --all
git commit -am "${DATE} lesson"

git push