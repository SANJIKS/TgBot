FROM python:3.10-slim

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app /app/app
COPY main.py /app/main.py
COPY data/* /app/data/

WORKDIR /app

CMD ["python", "main.py"]