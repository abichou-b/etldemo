FROM python:3.7


COPY requirements.txt /
RUN pip install requirements.txt

WORKDIR /demo
ADD . /demo
RUN pip install .


CMD demo