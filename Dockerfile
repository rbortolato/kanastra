FROM python:3.9.16-slim-buster

WORKDIR /app

COPY ./requirements.txt .

RUN python -m pip install --upgrade pip \
    && python -m pip install --upgrade setuptools \
    && python -m pip install --no-cache-dir -r requirements.txt \
    && pip install debugpy -t /tmp

CMD python /tmp/debugpy --listen 0.0.0.0:5678 -m uvicorn main:app --host 0.0.0.0 --port 4080 --workers 8 --reload
