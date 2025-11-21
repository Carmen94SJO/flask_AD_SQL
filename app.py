# Importamos Flask y funciones necesarias
from flask import Flask, render_template, request
# Importamos MySQLdb para conectar con MySQL
import MySQLdb

# Creamos la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos

app.config['MYSQL_HOST'] = 'localhost'       # Host de la base de datos
app.config['MYSQL_USER'] = 'Carmenflask'     # Usuario de MySQL
app.config['MYSQL_PASSWORD'] = '1234'        # Contraseña del usuario
app.config['MYSQL_DB'] = 'sakila'            # Nombre de la base de datos

# ===========================
# Función para crear una nueva conexión a la base de datos
# ===========================
def get_connection():
    """Crea y devuelve una nueva conexión MySQL"""
    return MySQLdb.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        passwd=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB']
    )

# ===========================
# Ruta principal de la aplicación
# ===========================
@app.route('/', methods=['GET', 'POST'])
def index():
    # Variables iniciales
    query = None        # Consulta SQL que ingresa el usuario
    columns = []        # Nombres de columnas de la tabla de resultados
    rows = []           # Filas resultantes de la consulta
    error = None        # Mensajes de error

    # Datos para gráfico de top 5 categorías
    chart_labels = []   # Nombres de categorías
    chart_values = []   # Cantidad de películas por categoría

    try:
        # Abrimos la conexión y creamos un cursor
        conn = get_connection()
        cursor = conn.cursor()

        # ===========================
        # Consulta SQL para el gráfico de top 5 categorías
        # ===========================
        cursor.execute("""
            SELECT c.name, COUNT(*) as total
            FROM film_category fc
            JOIN category c ON fc.category_id = c.category_id
            GROUP BY c.name
            ORDER BY total DESC
            LIMIT 5
        """)
        # Obtenemos todos los resultados
        result = cursor.fetchall()
        # Guardamos los nombres y cantidades en listas para Chart.js
        chart_labels = [r[0] for r in result] if result else ["Sin datos"]
        chart_values = [r[1] for r in result] if result else [0]

        # ===========================
        # Ejecución de la consulta ingresada por el usuario
        # ===========================
        if request.method == 'POST':
            # Obtenemos la consulta del formulario y eliminamos espacios
            query = request.form.get('query', '').strip()

            # Validación básica de seguridad para evitar comandos peligrosos
            forbidden = ['drop', 'truncate']
            if any(query.lower().startswith(f) for f in forbidden):
                error = "No se permite ejecutar comandos peligrosos."
            elif not query:
                error = "Por favor, ingresa una consulta SQL válida."
            else:
                # Ejecutamos la consulta
                cursor.execute(query)
                if cursor.description:  # Si devuelve filas (SELECT)
                    columns = [desc[0] for desc in cursor.description]  # Nombres de columnas
                    rows = cursor.fetchall()  # Datos
                else:  # Si es INSERT, UPDATE, DELETE
                    conn.commit()  # Guardamos cambios
                    rows = [("Consulta ejecutada correctamente.",)]

    # ===========================
    # Manejo de errores específicos
    # ===========================
    except MySQLdb.OperationalError as e:
        error = "Error de conexión: " + str(e)
    except MySQLdb.ProgrammingError as e:
        error = "Error en la consulta SQL: " + str(e)
    except Exception as e:
        error = "Error inesperado: " + str(e)
    finally:
        # Cerramos cursor y conexión de forma segura
        try:
            cursor.close()
            conn.close()
        except:
            pass

    # Renderizamos el template y pasamos todas las variables necesarias
    return render_template(
        'dashboard.html',
        query=query,
        columns=columns,
        rows=rows,
        error=error,
        chart_labels=chart_labels,
        chart_values=chart_values
    )

# ===========================
# Ejecutamos la app en modo debug
# ===========================
if __name__ == '__main__':
    app.run(debug=True)
