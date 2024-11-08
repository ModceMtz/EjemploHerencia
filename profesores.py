# profesores.py
from persona import Persona

class Profesores(Persona):
    def __init__(self):
        super().__init__()
        self._departamento = ""
        self._categoria = ""
        self._maxgradoestudios = ""

    # Getter y Setter
    def get_departamento(self):
        if self._departamento == "":
            return "El departamento no se ha asignado"
        else:
            return self._departamento

    def set_departamento(self, departamento):
        self._departamento = departamento


    def get_categoria(self):
        if self._categoria == "":
            return "La categoría no se ha asignado"
        else:
            return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria


    def get_maxgradoestudios(self):
        if self._maxgradoestudios == "":
            return "El máximo grado de estudios no se ha asignado"
        else:
            return self._maxgradoestudios

    def set_maxgradoestudios(self, maxgradoestudios):
        self._maxgradoestudios = maxgradoestudios

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Departamento: {self._departamento}, Categoría: {self._categoria}, Máximo grado de estudios: {self._maxgradoestudios}"
