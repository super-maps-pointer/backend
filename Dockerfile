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
RUN pipenv install --deploy --system --ignore-pipfile

# -- Adding script to wait for postgres to be ready
COPY utils/wait-for.sh utils/wait-for.sh
RUN chmod +x utils/wait-for.sh

EXPOSE 8000/tcp
