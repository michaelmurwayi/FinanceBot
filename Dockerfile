# Pull the base image
FROM python:3

# Set environment variables
# ensure no .pyc files are written
# ensure output is not bufferd with docker
ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1

RUN mkdir /finance
WORKDIR /finance
#Upgrade pip
RUN pip install pip -U
ADD . requirements.txt /finance/
#Install dependencies
RUN pip install -r requirements.txt
ADD . /finance/