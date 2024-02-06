FROM python:3.11

WORKDIR /code

RUN pip install --no-cache-dir --upgrade poetry
COPY . /code
RUN poetry install

EXPOSE 8000/tcp
CMD ["poetry", "run", "python", "src/main.py"]