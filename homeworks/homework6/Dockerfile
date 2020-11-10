FROM python:3.7.6-buster

ARG TRG_ENV
ARG PG_HOST

ENV TRG_ENV=${TRG_ENV:-dev} \
  PG_HOST=${PG_HOST:-127.0.0.1} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PATH="/root/.poetry/bin:${PATH}" \ 
  POETRY_VERSION=1.1.4

# Don't want to install poetry from web directly, using pip
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY ship-showdown/poetry.lock ship-showdown/pyproject.toml ./

# Container already isolated, skip venv
RUN poetry config virtualenvs.create false
# Check env and install accordingly
RUN poetry install $(if [ "$TRG_ENV" = "prod" ]; then echo "--no-dev"; fi) --no-interaction --no-ansi

COPY ship-showdown .

EXPOSE 5000/tcp

# Prepare data in DB
# ENTRYPOINT "pg-check.sh ${PG_HOST} && python -m flask db upgrade && python main.py"
#RUN ["python", "-m", "flask", "db", "upgrade"]

# Run main app file
CMD ["bash", "./startup.sh"]

# Run container with 
# docker run -p 5000:5000 --name <container_name> <image>:<tag>