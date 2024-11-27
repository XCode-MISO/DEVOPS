FROM --platform=linux/amd64 python:3.9.16-slim-bullseye
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .



EXPOSE 5000
CMD [ "python3", "application.py" ]

RUN pip install newrelic
ENV NEW_RELIC_APP_NAME="PythonAPP"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LICENSE_KEY=65C1B1C0D884CF28347FDC64E7D041EF02597B9D37F1440A276EB77B110AEA4A
ENV NEW_RELIC_LOG_LEVEL=info

ENTRYPOINT [ "newrelic-admin", "run-program" ]

