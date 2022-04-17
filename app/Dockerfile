# base image
FROM python:3.8

# set environment variables
ENV PYTHONUNBUFFERED 1

# set directory
WORKDIR /app

# add application and install dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
COPY . ./
RUN python -m spacy download en_core_web_sm

# run the program
CMD ["supervisord", "-c", "supervisord.conf"]
