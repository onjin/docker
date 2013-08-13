FROM ubuntu

RUN apt-get install -y python git
RUN git clone https://bitbucket.org/paasmaker/paasmaker.git /var/lib/paasmaker
RUN cd /var/lib/paasmaker && ./install.py ./install/configs/example-paasmaker-hacking.yml


EXPOSE 42530

CMD cd /var/lib/paasmaker && ./pm-server.py --debug=1
