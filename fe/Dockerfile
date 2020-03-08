FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
ADD requirements.txt /code/
# ADD . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
# ENTRYPOINT['/bin/bash']
