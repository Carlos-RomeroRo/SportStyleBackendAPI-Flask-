# 🏬 SportStyle - Backend API

SportStyle es una API RESTful desarrollada con Flask para gestionar el catálogo, inventario y operaciones de una tienda de ropa deportiva. Está diseñada para manejar productos, usuarios, pedidos y autenticación mediante JWT.

---

## 🎯 Objetivo General

Desarrollar una API RESTful con Flask que gestione el catálogo, inventario y operaciones de una tienda de ropa deportiva (camisas, pantalones, medias, zapatos y accesorios), permitiendo operaciones CRUD, gestión de stock, categorías y pedidos.

---

## 📦 Alcance del Proyecto

La API permite:

- Registrar y consultar productos deportivos.
- Gestionar categorías y subcategorías.
- Controlar inventario disponible por producto.
- Manejar usuarios (clientes y administradores).
- Procesar órdenes de compra (simulación).
- Llevar un historial básico de transacciones.
- Autenticación básica mediante JSON Web Tokens (JWT).


---

## 🧩 Modelado de Datos

### 🔹 Producto
- `id`: int
- `nombre`: string
- `descripcion`: string
- `precio`: float
- `stock`: int
- `categoria_id`: FK
- `talla`: string (opcional)
- `color`: string

### 🔹 Categoría
- `id`: int
- `nombre`: string
- `descripcion`: string

### 🔹 Usuario
- `id`: int
- `nombre`: string
- `email`: string
- `password_hash`: string
- `rol`: string (`admin` / `cliente`)

### 🔹 Orden
- `id`: int
- `usuario_id`: FK
- `productos`: lista de productos con cantidad
- `total`: float
- `fecha`: datetime
- `estado`: string (`pendiente`, `pagado`, `enviado`)

### 🔹 Order Item
- `id`: int
- `order_id`: FK
- `product_id`: FK
- `cantidad`: int

---

## 🔐 Autenticación y Autorización

Se implementa mediante **JWT (JSON Web Token)**.

- **Administradores** pueden:
  - Crear, actualizar y eliminar productos.
  - Ver todas las órdenes.

- **Clientes** pueden:
  - Ver productos.
  - Crear una orden.
  - Consultar sus órdenes.

---

## 🧪 Testing

- Pruebas unitarias con **pytest**.
- Mockeo de servicios y base de datos.
- Casos de prueba para:
  - Modelos
  - Servicios
  - Rutas (Endpoints)

---

## 🧱 Base de Datos

- **PostgreSQL** (producción) o **SQLite** (local/desarrollo)
- ORM: **SQLAlchemy**
- Migraciones: **Flask-Migrate** o **Alembic**
- Relaciones bien definidas entre productos, categorías, usuarios y órdenes.

---

## 🔧 Herramientas y Librerías Clave

- **Flask**
- **Flask-RESTful** o **Flask-Router**
- **Flask-JWT-Extended**
- **SQLAlchemy**
- **Marshmallow**
- **Flask-Migrate**
- **Pytest**

---

## 🚀 Ejecución con Docker

### Requisitos:

- Docker y Docker Compose instalados

### Pasos:

```bash
docker-compose down -v          # Elimina contenedores y volúmenes antiguos
docker-compose build            # Construye las imágenes
docker-compose up               # Inicia la aplicación

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
