FROM debian:jessie
MAINTAINER Liz Rice <liz@force12.io>

ENV TELEGRAF_VERSION 0.2.4
RUN apt-get update && \
  apt-get install -y curl && \
  curl -s -o /tmp/telegraf_latest_amd64.deb http://get.influxdb.org/telegraf/telegraf_${TELEGRAF_VERSION}_amd64.deb && \
  dpkg -i /tmp/telegraf_latest_amd64.deb && \
  rm /tmp/telegraf_latest_amd64.deb && \
  rm -rf /var/lib/apt/lists/*

ADD telegraf.conf /config/telegraf.conf

CMD /etc/opt/telegraf/telegraf -config /config/telegraf.conf