# Inicio de la Aplicación con Docker

Este proyecto utiliza Docker y Docker Compose para facilitar el despliegue de la aplicación y sus servicios (como la base de datos). A continuación, encontrarás las instrucciones para configurarla y ejecutarla correctamente.

## Requisitos Previos

- Tener instalado [Docker](https://www.docker.com/products/docker-desktop)
- Tener instalado [Docker Compose](https://docs.docker.com/compose/)

## Archivos Importantes

- `docker-compose.yml`: Define los servicios (app, base de datos, etc.).
- `.env`: Contiene variables de entorno como credenciales de base de datos, puertos, etc. **No olvides crearlo antes de iniciar el entorno.**

## Estructura Básica del .env

Antes de iniciar, crea un archivo `.env` en la raíz del proyecto con contenido similar al siguiente:

```env
# Variables de entorno para la aplicación
APP_PORT=5000
APP_ENV=development

# Variables de entorno para la base de datos
DB_HOST=db
DB_PORT=5432
DB_NAME=mi_basedatos
DB_USER=usuario
DB_PASSWORD=contraseña

#Instrucciones para Iniciar la Aplicación

Para eliminar cualquier rastro anterior y arrancar la aplicación limpia, ejecuta los siguientes comandos:
docker-compose down -v

Este comando elimina contenedores y volúmenes antiguos.
docker-compose build

Reconstruye las imágenes de Docker.
docker-compose up

Inicia los contenedores. Si deseas ejecutarlo en segundo plano, puedes usar:
docker-compose up -d

# Detener y Limpiar Todo
Para detener los contenedores y limpiar los volúmenes de nuevo, ejecuta:
docker-compose down -v
