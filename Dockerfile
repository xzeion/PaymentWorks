FROM python:3.9
ENV PYTHONBUFFERED 1
WORKDIR /src
ADD requirements.txt /tmp
RUN pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt
add ./ /src/
