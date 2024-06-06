#!/usr/bin/env bash

NAME="lifsim"
DJANGODIR=/src/lifsim/mathlab
ENVBIN=/src/lifsim_env/bin
DJANGO_SETTINGS_MODULE=mathlab.settings

echo "starting $NAME"

source $ENVBIN/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

export  PYTHONPATH=$DJANGODIR:$PYTHONPATH

exec   $ENVBIN/uwsgi --ini /src/lifsim/deployment