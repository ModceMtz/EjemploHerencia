# persona.py
class Persona:
    def __init__(self):
        self._nombre = ""
        self._apellido = ""
        self._edad = 0

    # Getters y Setters
    def get_nombre(self):
        if self._nombre == "":
            return "La persona no tiene nombre"
        else:
            return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        if self._apellido == "":
            return "La persona no tiene apellido"
        else:
            return self._apellido


    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_edad(self):
        if self._edad == 0:
            return "La persona no tiene edad"
        else:
            return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def mostrar_informacion(self):
        return f"Nombre: {self._nombre} {self._apellido}, Edad: {self._edad}"
