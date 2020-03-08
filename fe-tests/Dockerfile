FROM selenium/standalone-chrome:3.4.0

USER root
# RUN mkdir code
WORKDIR /code
# ADD . /code
# RUN sudo apt-get remove python-pip python-dev python-pip
RUN sudo apt-get -y update && sudo apt-get -y upgrade
RUN apt-get install --yes python3 python3-pip
# RUN apt-get update && apt-get install python3 python3-pip

ADD requirements.txt /code/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# RUN apt-get update && apt-get install -y python3 python3-dev python3-pip
# RUN pip install --upgrade pip && pip install behave selenium
EXPOSE 3002
# ENTRYPOINT ["/bin/bash"]
