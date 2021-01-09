FROM python:3.7
COPY . /trace_clustering
WORKDIR /trace_clustering
RUN pip3 install -r requirements.txt 
EXPOSE 3000 
CMD [ "python3", "./main.py" ]

