FROM tensorflow/tensorflow:latest-py3

RUN mkdir /usr/src/app
ADD requirements.txt /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install -r requirements.txt

COPY /Users/jb/preprocessors.py /docker_dev

EXPOSE 8888
EXPOSE 6006


