FROM python:3.10-slim

WORKDIR /app

# Instalar postgresql-client para usar pg_isready
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY . .

CMD ["/wait-for-it.sh", "db", "5432", "python", "run.py"]

