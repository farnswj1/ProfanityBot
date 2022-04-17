# base image
FROM python:3.8

# set environment variables
ENV PYTHONUNBUFFERED 1

# set directory
WORKDIR /app

# add application and install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile
RUN python -m spacy download en_core_web_sm
COPY . ./

# run the program
CMD ["supervisord", "-c", "supervisord.conf"]
