FROM python:3.8-slim-buster

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD tools/run_erem_bot.sh
