# https://docs.docker.com/samples/django/
FROM python:3.10

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /code/


