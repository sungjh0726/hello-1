#!/bin/sh

#DATE=`date +%Y-%m-%d" "%H:%M`
DATE=`date +%Y-%m-%d`
MSG="$DATE lesson"
if [ $# -gt 0 ]; then
    MSG="$1"
fi

git add --all
git commit -am "${MSG}"

git push
