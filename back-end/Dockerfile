FROM python:3.11-slim

ADD requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

ADD ./src/ /code/
WORKDIR /code

ENV DEBUG=1

ENV BACKEND_HOST=0.0.0.0
ENV BACKEND_PORT=8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]