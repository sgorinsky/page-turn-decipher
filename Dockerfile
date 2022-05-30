#Create a ubuntu base image with python 3 installed.
FROM python:3.9

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR "/page-turn-decipher"
COPY . .

ENV POETRY_VERSION=1.1.8

RUN apt-get install gunicorn -y
RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

# docker -it -p 80:5000 page-turn-decipher
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app", "--workers=2"]
