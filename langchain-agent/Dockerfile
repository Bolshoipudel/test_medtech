FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY agent.py tools.py examples.py data_loader.py ./

VOLUME ["/app/data"]

CMD ["python", "examples.py"]
