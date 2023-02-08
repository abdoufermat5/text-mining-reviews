###############
# BUILD IMAGE #
###############
FROM python:3.8.2-slim-buster AS build

# virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# add and install requirements
RUN pip install --upgrade pip

# add non-root user and give permissions to workdir
RUN mkdir /usr/src/app

# set working directory
WORKDIR /usr/src/app

# add requirements
COPY . /usr/src/app

# install requirements
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN python -m pip install pymongo[srv]

# disables lag in stdout/stderr output
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Path
ENV PATH="/opt/venv/bin:$PATH"