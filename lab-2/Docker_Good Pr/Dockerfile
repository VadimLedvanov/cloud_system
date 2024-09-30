FROM python:3.10

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN mkdir -p logs /usr/share/cool-app
RUN echo "Running web-app from docker" > /usr/share/cool-app/cool-text.txt

ENV COOL_PORT 8888
ENV COOL_IP 0.0.0.0
ENV COOL_LOG logs
EXPOSE 8888/tcp
CMD ["python3", "run.py"]
