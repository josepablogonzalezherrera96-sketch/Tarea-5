from models.contacto import Contacto
from services.archivos import GestorArchivos

class AgendaLogica:
    def __init__(self):
        self.contactos = []
        self.gestor_archivos = None

    def cargar_desde_archivo(self, tipo_archivo, ruta):
        self.gestor_archivos = GestorArchivos(tipo_archivo, ruta)
        datos_crudos = self.gestor_archivos.leer()
        
        self.contactos = [
            Contacto(d['nombre'], d['telefono'], d['email'], d['edad'], d['residencia'])
            for d in datos_crudos
        ]
        print(f"\n[+] Se cargaron {len(self.contactos)} contactos en memoria.")

    def agregar_contacto(self, nombre, telefono, email, edad, residencia):
        if not self.gestor_archivos:
            print("\n[!] Error: Primero debes cargar/crear un archivo (Opción 1) para saber dónde guardar.")
            return

        nuevo_contacto = Contacto(nombre, telefono, email, edad, residencia)
        self.contactos.append(nuevo_contacto)

        # Se guardan los datos para no perder registros anteriores [cite: 98, 112]
        datos_dict = [c.to_dict() for c in self.contactos]
        self.gestor_archivos.guardar(datos_dict)
        print("\n[+] Contacto agregado en memoria y guardado en archivo exitosamente.")

    def buscar_por_nombre(self, nombre_parcial):
        # Búsqueda parcial por nombre, sin importar mayúsculas/minúsculas [cite: 100, 101]
        return [c for c in self.contactos if nombre_parcial.lower() in c.nombre.lower()]

    def buscar_por_telefono(self, telefono_parcial):
        # Búsqueda parcial por teléfono [cite: 103]
        return [c for c in self.contactos if telefono_parcial in c.telefono]

    def promedio_edad(self):
        if not self.contactos:
            return 0
        suma_edades = sum(c.edad for c in self.contactos)
        return suma_edades / len(self.contactos)

    def mostrar_todos(self):
        return self.contactos
