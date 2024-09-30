FROM python:latest

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN git clone "https://github.com/VladiqDanilov/cool_web_appVL.git"

RUN apt-get install -y curl


ENV COOL_PORT 8888
ENV COOL_IP 0.0.0.0
ENV COOL_LOG logs
EXPOSE 8888/tcp





RUN mkdir logs
RUN mkdir /usr/share/cool-app
RUN echo "Running web-app from docker" > /usr/share/cool-app/cool-text.txt


CMD ["python3", "cool_web_appVL/run.py"]
