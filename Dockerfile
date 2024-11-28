FROM --platform=linux/amd64 python:3.9.16-slim-bullseye
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "python3", "application.py" ]

ARG newrelic_license

##Confguración New Relic
RUN pip install newrelic
ENV NEW_RELIC_APP_NAME="docker"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
#INGEST_License
ENV NEW_RELIC_LICENSE_KEY=$newrelic_license
ENV NEW_RELIC_LOG_LEVEL=info

ENTRYPOINT [ "newrelic-admin", "run-program" ]

