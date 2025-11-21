# SQL Dashboard - Sakila Database

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.x-green)
![MySQL](https://img.shields.io/badge/mysql-8.x-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Tabla de Contenidos
1. [Descripción General](#descripción-general)
2. [Características Principales](#características-principales)
3. [Tecnologías Utilizadas](#tecnologías-utilizadas)
4. [Requisitos Previos](#requisitos-previos)
5. [Instalación](#instalación)
6. [Configuración del Entorno Virtual (venv)](#configuración-del-entorno-virtual-venv)
7. [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)
8. [Estructura del Proyecto](#estructura-del-proyecto)
9. [Dependencias](#dependencias)
10. [Tablas Accesibles](#tablas-accesibles)
11. [Puesta en Marcha](#puesta-en-marcha)
12. [Uso de la Aplicación](#uso-de-la-aplicación)
13. [Gestión y Control de Errores](#gestión-y-control-de-errores)
14. [Funcionalidades Adicionales](#funcionalidades-adicionales)
15. [Capturas de Pantalla](#capturas-de-pantalla)
16. [Autoría](#autoría)

---

## Descripción General

**SQL Dashboard** es un proyecto que permite la ejecución y visualización de consultas SQL sobre la base de datos de ejemplo **Sakila**. La aplicación ofrece:

- Ejecución de consultas personalizadas desde el navegador.
- Acceso a un conjunto de consultas predefinidas.
- Visualización de métricas mediante gráficos dinámicos interactivos.

El sistema está desarrollado con **Flask** como framework web, **MySQL** como motor de base de datos, **Tailwind CSS** para el diseño de la interfaz y **Chart.js** para las visualizaciones.

---

## Características Principales

- Ejecución de consultas SQL desde la interfaz web.
- Resultados presentados en tablas HTML dinámicas y adaptativas.
- Conjunto de consultas rápidas accesibles desde el menú lateral.
- Gráficos automáticos con las cinco categorías que contienen más películas.
- Gestión de errores SQL y bloqueo de comandos destructivos.
- Interfaz ligera, responsiva y orientada a fines académicos o de demostración.

---

## Tecnologías Utilizadas

- **Python 3.x**
- **Flask**
- **MySQL Server**
- **mysqlclient** (MySQLdb para Python)
- **HTML5 / Tailwind CSS**
- **Chart.js**
- **Visual Studio Code**

---

## Requisitos Previos

1. Python 3.8 o superior.
2. MySQL Server con la base de datos **Sakila** importada.
3. Dependencias de Python (instaladas dentro del entorno virtual):

```bash
pip install -r requirements.txt
```

---

## Instalación

Clona el repositorio y accede al proyecto:

```bash
git clone https://github.com/usuario/sql-dashboard.git
cd sql-dashboard
```

---

## Configuración del Entorno Virtual (venv)

1. Abrir terminal y navegar a la carpeta del proyecto:

```powershell
cd C:\Users\Usuario\Desktop\2.DAM\my_flask_app
```

2. Crear un entorno virtual:

```powershell
python -m venv venv
```

3. Activar el entorno virtual:

| Sistema   | Comando                    |
| --------- | -------------------------- |
| Windows   | `.\venv\Scripts\activate`  |
| Linux/Mac | `source venv/bin/activate` |

4. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

> Nota: Siempre activa el entorno virtual antes de trabajar en el proyecto.

---

## Configuración de la Base de Datos

1. Inicia MySQL Server.
2. Crear un usuario con permisos sobre la base de datos Sakila (opcional):

```sql
CREATE USER 'Carmenflask'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON sakila.* TO 'Carmenflask'@'localhost';
FLUSH PRIVILEGES;
```

3. Ajusta los parámetros de conexión en `app.py` o usando un archivo `.env`:

```env
MYSQL_HOST=localhost
MYSQL_USER=Carmenflask
MYSQL_PASSWORD=1234
MYSQL_DB=sakila
```

---

## Estructura del Proyecto

```text
my_flask_app/
├── venv/                  # Entorno virtual
├── static/                # Archivos CSS, JS, imágenes
├── templates/             # Plantillas HTML
│   └── dashboard.html
├── app.py                 # Aplicación principal
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación
```

> Para ver la estructura completa en PowerShell:
>
> ```powershell
> tree /F
> ```

---

## Dependencias

Archivo `requirements.txt`:

```
blinker==1.9.0
click==8.3.0
colorama==0.4.6
Flask==3.1.2
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
mysql-connector-python==9.5.0
setuptools==65.5.0
Werkzeug==3.1.3
```

> Instala estas dependencias dentro del entorno virtual antes de ejecutar la aplicación.

---

## Tablas Accesibles

| Tabla    | Descripción               |
| -------- | ------------------------- |
| actor    | Información sobre actores |
| film     | Información de películas  |
| category | Categorías de películas   |
| customer | Clientes registrados      |
| rental   | Historial de alquileres   |

---

## Puesta en Marcha

1. Activar el entorno virtual:

```powershell
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

2. Ejecutar la aplicación:

```powershell
python app.py
```

3. Abrir navegador y acceder a:

```
http://127.0.0.1:5000/
```

---

## Uso de la Aplicación

### Dashboard Principal

<img src="static/images/img%20%282%29.png" alt="Dashboard principal" width="600">

* Selecciona consultas SQL predefinidas desde el menú lateral.
* Ejecuta consultas personalizadas en el área principal.
* Visualiza resultados en tablas HTML dinámicas.
* Los gráficos de categorías se actualizan automáticamente según los datos de la base.

---

## Gestión y Control de Errores

* Bloqueo de comandos destructivos como `DROP` o `TRUNCATE`.
* Mensajes informativos al ejecutar consultas incorrectas.
* Notificación directa de problemas de conexión a la base en la interfaz.

---

## Funcionalidades Adicionales

* Visualización de métricas mediante **Chart.js**.
* Estilo moderno implementado con **Tailwind CSS**.
* Interfaz responsiva para distintos tamaños de pantalla.
* Arquitectura preparada para añadir nuevas consultas o gráficos.

---

## Capturas de Pantalla

<img src="static/images/img%20%283%29.png" alt="Consultas predefinidas" width="600">
<img src="static/images/img%20%281%29.png" alt="Resultados de consultas" width="600">

---

## Autoría

Desarrollado como proyecto académico y de portfolio con **Flask**, **SQL** y visualización de datos.

**Carmen Victoria Casas Novas Garcia**
