FROM python:3.7-alpine

COPY requirements.txt /tmp/requirements.txt

RUN apk update \
    && apk add --update --no-cache --virtual .build-deps alpine-sdk python3-dev musl-dev postgresql-dev libffi-dev \
    && pip install -U setuptools \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && apk --purge del .build-deps

COPY . /src

WORKDIR /src

ENV PYTHONPATH=/src

# CMD ["python", "src/main.py"]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
