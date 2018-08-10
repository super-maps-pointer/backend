FROM python:3.6

LABEL authors="kruupos"

# -- Install Pipenv:
RUN pip3 install pipenv

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# -- Install Application into container:
RUN set -ex && mkdir /back

WORKDIR /back

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system --ignore-pipfile

EXPOSE 8000/tcp
