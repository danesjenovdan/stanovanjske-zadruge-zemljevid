FROM python:3.8

RUN apt-get update && \
    apt-get upgrade -y

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=api.settings

# this is the command for dev
CMD python manage.py runserver 0.0.0.0:8000
