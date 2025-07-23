# SportStyleBackendAPI-Flask-
# 🏬 SportStyle - Backend API

Una API RESTful construida con **Flask** para la gestión integral de una tienda de ropa deportiva. Permite operaciones CRUD sobre productos, categorías, órdenes y usuarios, incluyendo autenticación con JWT y control de inventario.

---

## 🎯 Objetivo General

Desarrollar una API RESTful con Flask que gestione el **catálogo, inventario y operaciones de una tienda de ropa deportiva**, permitiendo operaciones CRUD, autenticación y simulación de pedidos.

---

## 📦 Alcance del Proyecto

- Registrar y consultar productos deportivos.
- Gestionar categorías y subcategorías.
- Controlar inventario por producto.
- Manejar usuarios (clientes y administradores).
- Procesar órdenes de compra (simuladas).
- Historial básico de transacciones.
- Autenticación con JWT.

---

## 🗂️ Estructura del Proyecto (Sugerida)


---

## 🧩 Modelado de Datos

### 🔹 Producto
- `id`: int  
- `nombre`: string  
- `descripcion`: string  
- `precio`: float  
- `stock`: int  
- `categoria_id`: FK  
- `talla`: string  
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
- `rol`: string (admin / cliente)

### 🔹 Orden
- `id`: int  
- `usuario_id`: FK  
- `productos`: lista con cantidades  
- `total`: float  
- `fecha`: datetime  
- `estado`: string

### 🔹 OrderItem
- `id`: int  
- `order_id`: FK  
- `product_id`: FK  
- `cantidad`: int

Relaciones clave:
- `user_id` conecta orden con usuario.
- `product_id` en `OrderItem` define los productos de cada orden.

---

## 🔐 Autenticación y Autorización

Autenticación con **JWT (JSON Web Token)**:
- **Admin:** puede crear, actualizar y eliminar productos, ver todas las órdenes.
- **Cliente:** puede ver productos, crear órdenes y ver su historial.

---

## 📮 Principales Endpoints

### 🛍️ Productos
| Método | Ruta                 | Descripción                  |
|--------|----------------------|------------------------------|
| GET    | `/api/products`      | Lista todos los productos    |
| GET    | `/api/products/<id>` | Obtiene un producto específico |
| POST   | `/api/products`      | Crear producto (admin)       |
| PUT    | `/api/products/<id>` | Actualizar producto (admin)  |
| DELETE | `/api/products/<id>` | Eliminar producto (admin)    |

### 📁 Categorías
| Método | Ruta                 | Descripción                  |
|--------|----------------------|------------------------------|
| GET    | `/api/categories`    | Lista todas las categorías   |
| POST   | `/api/categories`    | Crear categoría (admin)      |

### 👤 Usuarios
| Método | Ruta                 | Descripción                     |
|--------|----------------------|---------------------------------|
| POST   | `/api/register`      | Registro de nuevos usuarios     |
| POST   | `/api/login`         | Login y generación de JWT       |
| GET    | `/api/user/profile`  | Perfil del usuario (con token)  |

### 🧾 Órdenes
| Método | Ruta                 | Descripción                          |
|--------|----------------------|--------------------------------------|
| GET    | `/api/orders`        | Ver órdenes del usuario logueado     |
| POST   | `/api/orders`        | Crear nueva orden                    |
| GET    | `/api/orders/all`    | Ver todas las órdenes (admin)        |

---

## 🧪 Testing

- Pruebas unitarias con `pytest`
- Mock de base de datos y servicios
- Casos de prueba por:
  - Modelo
  - Servicio
  - Rutas

---

## 🧱 Base de Datos

- **PostgreSQL** (o **SQLite** en desarrollo)
- ORM: **SQLAlchemy**
- Migraciones: **Flask-Migrate / Alembic**

---

## 🔧 Herramientas y Librerías Clave

- `Flask`
- `Flask-JWT-Extended`
- `Flask-SQLAlchemy`
- `Flask-Migrate`
- `Marshmallow`
- `pytest`
- `python-dotenv`
- `requests`
- `psycopg2-binary`

---

## 📌 Notas Finales

- Arquitectura modular y escalable.
- Soporte para tallas y colores.
- Preparado para agregar filtros, búsquedas y paginación.
- Posibilidad de crecimiento hacia pagos o paneles administrativos.

---

## 🚀 Cómo empezar

```bash
# Clona el repositorio
git clone https://github.com/tuusuario/sportstyle_api.git
cd sportstyle_api

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la app
flask run
