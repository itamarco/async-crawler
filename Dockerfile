# Start with a base Python image
FROM python:3.9-slim-buster

# dependencies for psycog2
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

# Set environment variables for Poetry
ENV POETRY_VERSION=1.2.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="$POETRY_HOME/bin:$PATH"


RUN pip install poetry==${POETRY_VERSION}

RUN mkdir -p /tmp/webpages

WORKDIR /app


COPY ./pyproject.toml ./poetry.lock ./

# Install the dependencies without the development dependencies
RUN poetry install --only main

# Copy the app directory into the container
COPY ./app .


EXPOSE 80

# default command for fastapi app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]