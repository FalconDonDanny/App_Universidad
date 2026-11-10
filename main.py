import sqlite3

from alumno import Alumno
from curso import Curso
from matricula import Matricula

# --------------------------------
CONEXION = sqlite3.connect("iancap.db")

print("Conexion realizada correctamente")

cursor = CONEXION.cursor()

print("Cursor creado correctamente")

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
