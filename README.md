# BACKEND of SUPER MAPS POINTER

Super maps pointer is yet another game intended to upgrade your geography skills :earth_africa: while having fun! :smile:

### With what technologies?

* Flask version 1.0.2
* Angular version version 6.1.2 (in frontend repository)

### Requierments

* Docker
* Docker-compose

## Setup

#### 1. Clone this repository. 

```bash
# create new folder for the project because it will contain multiple repositories
mkdir super-maps-pointer && cd super-maps-pointer
# clone the repository
git clone https://github.com/super-maps-pointer/backend.git
```

#### 2. Install Docker

This app is running with `Docker`. This [link](https://docs.docker.com/docker-for-windows/) for how to install it.

#### 3. Initialize volume and databases using docker-compose

You will have to do it once.
In order to Initialize volume and databases, launch the following command:

```bash
docker-compose up --build
```

### 4. Run the app

```bash
docker-compose up flask
# or
docker-compose up
```

If all containers are up without problems:
  - `backend_flask`
  - `postgres:10`

Then you can now starting using the API. See the welcome page in [localhost:8000](http://127.0.0.1:8000)

### Reload the app

1. Shut down the container with `docker-compose down`
2. Reload the containers with `docker-compose up`

**Note**: If you are using `docker-compose up -d` do not forget to kill the containers with `docker-compose down` to avoid stupid conflicts of having two apps running in parallel on the same ports.

**Note for windows users**: sometimes Docker for windows have trouble copying the files into the containers, most of the time you just have to restart Docker to make it work.

## About this stack

Using [Flask](http://flask.pocoo.org/) the python microframework.

* With Python version 3.6

### Database

* postgreSQL using [SQLAlchemy](https://www.sqlalchemy.org/) version 1.2.10

### Developper Setup

A `Pipfile` have been used instead of old `requirements.txt` and `venv`.
Therefore, to install new packages, one need to use `pipenv install <package>` instead of `pip install <package>`.

1. Make sure you have python 3.6 installed on your machine
2. Install pipenv

In backend folder, uses
```bash
pip3 install pipenv
```

That's it. after installing or removing a package using `Pipenv`, just relaunch the `docker-compose up` command from repository root `super_maps_pointer` folder.

**Or** you can enter the container using `docker`.

#### Debugger

A debugger called: `Python: Attach debugger` is set up with **VS Code**, to use it:

1. launch the app with `docker-compose up`.
2. set any breakpoints you need.
3. launch the debugger.

### Unit Tests

```bash
docker-compose -f ./docker-compose.test.yml run --rm pytest
```
