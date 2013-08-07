FROM ubuntu

RUN apt-get install -y wget default-jre-headless

RUN wget http://www.us.apache.org/dist/lucene/solr/4.4.0/solr-4.4.0.tgz -O /tmp/solr-4.4.0.tgz
RUN cd /var/lib/ && tar zxf /tmp/solr-4.4.0.tgz
RUN cd /var/lib/solr-4.4.0/example/multicore && sed -i 's/persistent="false"/persistent="true"/' solr.xml

EXPOSE 8983

CMD cd /var/lib/solr-4.4.0/example && java -Dsolr.solr.home=multicore -jar start.jar
