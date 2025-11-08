#!/bin/bash

# aguarda serviços opcionais (postgres) - simples/curto; em produção use healthchecks
sleep 3

# Executa migrations
echo "Running migrations..."
python manage.py migrate --noinput


# Executa o comando passado ao container (CMD)
exec "$@"
