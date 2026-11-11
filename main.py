import sqlite3

from alumno import Alumno
from curso import Curso
from matricula import Matricula

DB_NAME = "inacap.db"
CONEXION = sqlite3.connect(DB_NAME)

# --------------------------------
# CONEXION
# --------------------------------
print("Conexion realizada correctamente")

# -----------------------------------
# CREAR CURSOR
# -----------------------------------
cursor = CONEXION.cursor()
print("Cursor creado correctamente")

# ------------------------------------
# CREAR TABLA ALUMNO
# ------------------------------------
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS alumno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL,
        edad INTEGER NOT NULL
    )
    """
)
print("Tabla alumno creada correctamente")

# ------------------------------------
# CREAR TABLA CURSO
# ------------------------------------
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS curso (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT NOT NULL
    )
    """
)
print("Tabla curso creada correctamente")

# ------------------------------------
# CREAR TABLA MATRICULA
# ------------------------------------
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS matricula (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alumno_id INTEGER NOT NULL,
        curso_id INTEGER NOT NULL,
        fecha_matricula TEXT NOT NULL,
        FOREIGN KEY (alumno_id) REFERENCES alumno(id),
        FOREIGN KEY (curso_id) REFERENCES curso(id)
    )
    """
)
print("Tabla matricula creada correctamente")

# ==============================================
# GUARDAR
# ==============================================
CONEXION.commit()
CONEXION.close()
print("Conexion cerrada correctamente")
