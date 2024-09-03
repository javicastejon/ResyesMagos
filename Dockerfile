FROM ubuntu:16.04
VOLUME /uzsound
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev


FROM python:3.8.12
# copy the requirements file into the image
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

ENTRYPOINT [ "python" ]

EXPOSE 5000
CMD ["app.py" ]
