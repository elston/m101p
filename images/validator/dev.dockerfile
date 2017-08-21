FROM python:2.7-slim

# ...  libgcc-4.9-dev
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    curl \
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

