FROM ubuntu

RUN apt-get install -y wget make gcc

RUN wget http://download.redis.io/redis-stable.tar.gz -O /var/lib/redis-stable.tar.gz
RUN cd /var/lib/ && tar zxf /var/lib/redis-stable.tar.gz
RUN cd /var/lib/redis-stable && make

EXPOSE 6379

CMD cd /var/lib/redis-stable/src && ./redis-server
