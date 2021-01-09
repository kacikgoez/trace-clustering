FROM python:3.7
COPY . /trace_clustering
WORKDIR /trace_clustering
RUN pip3 install -r requirements.txt 
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;
EXPOSE 3000 
CMD [ "python3", "./main.py" ]

