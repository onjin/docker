FROM ubuntu

RUN echo 'deb http://archive.ubuntu.com/ubuntu quantal main universe multiverse' > /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN apt-get install -y python-pip python-dev libpq-dev build-essential make gcc
RUN pip --no-input --exists-action=w install --upgrade pip psycopg2
RUN pip --no-input --exists-action=w install --upgrade sentry

ADD sentry.conf.py /etc/sentry.conf.py

#RUN printf "no\n" | sentry --config=/etc/sentry.conf.py upgrade
#RUN printf "admin\nadmin\n" | sentry --config=/etc/sentry.conf.py createsuperuser --username=admin --email=admin@local.host
#RUN sentry --config=/etc/sentry.conf.py repair --owner=admin


EXPOSE 7365

ENTRYPOINT ["/usr/local/bin/sentry", "--config=/etc/sentry.conf.py"]

CMD ["upgrade"]
