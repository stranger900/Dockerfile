FROM debian:8

WORKDIR /opt
COPY ./greeter.py .

RUN apt-get  update
RUN apt-get install python3-pip -y

ENTRYPOINT ["python3", "greeter.py"]
CMD ["Andriy"]
