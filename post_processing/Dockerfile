FROM python:3.10-alpine

RUN addgroup -S app && adduser -S app app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /app/wait

RUN apk add -U --no-cache build-base && \
    apk add --no-cache bash && \
    apk del build-base

COPY ./requirements.txt /

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

COPY ./config /app/config 
COPY ./start.sh /app
COPY ./main.py /app

WORKDIR /app

RUN chmod +x /app/start.sh
RUN chmod +x /app/wait
CMD ["./start.sh"]
