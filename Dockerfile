FROM ubuntu:latest
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y python3 python3-pip 
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD ["python3","backend.py"]