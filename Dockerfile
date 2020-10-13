FROM python:alpine

ADD . /example/

WORKDIR /example

EXPOSE 3060

CMD [ "python", "example.py" ]
