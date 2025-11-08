# Dockerfile
FROM python:3.12-slim

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências do SO necessárias (ex: gcc, libs)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements e instala
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copia o projeto
COPY . /app

# Dá permissão e torna entrypoint executável
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

# Entrada padrão — o entrypoint cuida de migrations, etc.
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "cryptotracker.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]