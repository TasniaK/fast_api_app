FROM python:3.7-alpine

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /src

WORKDIR /src

ENV PYTHONPATH=/src

CMD ["python", "src/main.py"]
