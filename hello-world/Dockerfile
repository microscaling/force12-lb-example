FROM python:2.7
RUN pip install Flask

ADD hello.py .
ADD templates/hello.html ./templates/hello.html

ENV SERVICE_80_NAME http
ENV SERVICE_NAME app
ENV SERVICE_TAGS production
 
EXPOSE 5000

CMD python hello.py
