FROM python:3.10

RUN apt-get update; apt-get clean

WORKDIR /app

COPY ./main/requirements.txt /app/main/

RUN pip install -r main/requirements.txt

COPY ./main /app/main

# CMD python3 /app/main/src/start.py
CMD pytest -v /app/main/src/tests/*; python3 /app/main/src/start.py
# CMD /app/main/entrypoint.sh