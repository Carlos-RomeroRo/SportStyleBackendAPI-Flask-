#!/bin/bash

# Verificar si se pasaron al menos 3 argumentos: host, puerto, y comando
if [ "$#" -lt 3 ]; then
  echo "Uso: $0 <host> <puerto> <comando...>"
  exit 1
fi

HOST=$1
PORT=$2
shift 2

echo "⏳ Esperando a que PostgreSQL esté disponible en $HOST:$PORT..."

until pg_isready -h "$HOST" -p "$PORT"; do
  sleep 1
done

echo "✅ PostgreSQL está disponible, ejecutando: $@"
exec "$@"
