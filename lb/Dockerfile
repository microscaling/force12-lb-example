FROM nginx:1.7
MAINTAINER Liz Rice <liz@force12.io>

# With thanks to Shane Sveller <shane@bellycard.com> whose project http://github.com/bellycard/docker-loadbalancer 
# was the starting point for this project

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update -qq && \
    apt-get -y install curl runit unzip && \
    rm -rf /var/lib/apt/lists/*

ENV CT_URL https://github.com/hashicorp/consul-template/releases/download/v0.1.0/consul-template_0.1.0_linux_amd64.tar.gz
RUN curl -L $CT_URL | tar -C /usr/local/bin --strip-components 1 -zxf -

ADD nginx.service /etc/service/nginx/run
RUN chmod +x /etc/service/nginx/run
ADD consul-template.service /etc/service/consul-template/run
RUN chmod +x /etc/service/consul-template/run

RUN rm -v /etc/nginx/conf.d/*
ADD nginx.conf /etc/consul-templates/nginx.conf

EXPOSE 80
EXPOSE 8080

CMD ["/usr/bin/runsvdir", "/etc/service"]
