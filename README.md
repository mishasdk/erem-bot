# Erem-bot

### Starting bot from source code

1. Export telegram API token as an env variable 

```export TG_TOKEN_EREM_BOT=<you_tg_token_here>```

2. Setup your python virtual env

```python3 -m venv venv```

3. Activate virtualenv

```source venv/bin/activate```

4. Install python dependencies

```pip install -r requirements.txt```

5. Run bot start script

```bash tools/run_erem_bot.sh```

### Starting bot from docker container

1. Export telegram API token as an env variable 

```export TG_TOKEN_EREM_BOT=<you_tg_token_here>```

2. Download docker image from docker-hub

```docker pull mishasdk/erem-bot```

3. Run docker image

```docker run -e TG_TOKEN_EREM_BOT=${TG_TOKEN_EREM_BOT} mishasdk/erem-bot```

### Commands

```

start - Миша рад знакомству!
help - Миша всегда поможет!
ask_anime - Миша поможет провести досуг!
naruto - Миша поделится мудростью!
who_is_dumb - Миша решит кто виноват!
hello - Миша поздоровается с другом!
roll - Миша решит любой спор!

```
