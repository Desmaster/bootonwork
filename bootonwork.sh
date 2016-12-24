#!/bin/bash

dirname=`dirname "$(test -L "$0" && readlink "$0" || echo "$0")"`

bootscript=${dirname}/boot.sh
workscript=${dirname}/workday.py
vacation=${dirname}/vacation.flag

set -e 

if [ -f $vacation ]; then
    echo "Vacation flag detected!"
    exit 1
fi

$workscript

if [ -f $bootscript ]; then
    bash $bootscript
else
    echo "$bootscript doesn't exist"
    exit 1
fi

