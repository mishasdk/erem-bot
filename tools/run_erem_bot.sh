#!/usr/bin/env bash

DIR=$(cd `dirname $0` && pwd)
APP_DIR=${DIR}'/../src/app'

python3 $APP_DIR/main.py \
    --tg_token $TG_TOKEN_EREM_BOT
