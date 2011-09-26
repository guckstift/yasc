#!/bin/sh

if [ -n "$(lsb_release -i | grep Arch)" ]; then
	python2 pybin/main.pyc
else
	python pybin/main.pyc
fi
