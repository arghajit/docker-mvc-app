# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
ADD requirements.txt /code/
ADD . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python","manage.py","createsuperuser","--username","admin","--password","admin"]
CMD ["python","manage.py", "makemigrations","service"]
CMD ["python", "manage.py", "migrate","service"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]