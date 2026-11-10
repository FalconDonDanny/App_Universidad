
class Alumno:
    def __init__(self, id, nombre, email, edad):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.edad = edad

    def mostrar_info(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Edad: {self.edad}")