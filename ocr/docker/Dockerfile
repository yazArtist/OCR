FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install poetry

RUN poetry install

CMD ["poetry", "run", "python", "main.py"]

EXPOSE 8000
