FROM python:3.12-slim

WORKDIR /app

COPY ./templates /app/templates
COPY ./app.py /app
COPY ./flag /flag
COPY ./requirements.txt /app

RUN python3 -m venv /app/venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PATH="/app/venv/bin:$PATH"

EXPOSE 5000

CMD ["flask", "run"]
