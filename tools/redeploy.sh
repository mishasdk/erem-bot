#!/usr/bin/env bash

docker pull mishasdk/erem-bot
docker stop erem-bot
docker system prune -f
docker run -d \
    -e TG_TOKEN_EREM_BOT=${TG_TOKEN_EREM_BOT} \
    --name=erem-bot \
    mishasdk/erem-bot
