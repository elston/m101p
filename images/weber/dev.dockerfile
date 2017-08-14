FROM python:3.6-slim

# ...
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
&& pip install --upgrade \
    pip \
    virtualenv \
&& pip install \
    virtualenvwrapper \
&& pip install --upgrade \
    virtualenvwrapper

#..
RUN touch ~/.bashrc \
&& echo " " >> ~/.bashrc \
&& echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

