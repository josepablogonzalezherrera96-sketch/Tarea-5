import json
import csv
import os

class GestorArchivos:
    def __init__(self, tipo_archivo, ruta):
        self.tipo_archivo = tipo_archivo.lower()
        self.ruta = ruta

    def leer(self):
        contactos = []
        # Si el archivo no existe aún, retorna lista vacía
        if not os.path.exists(self.ruta):
            return contactos

        if self.tipo_archivo == 'json':
            with open(self.ruta, 'r', encoding='utf-8') as f:
                try:
                    contactos = json.load(f)
                except json.JSONDecodeError:
                    contactos = []
                    
        elif self.tipo_archivo == 'csv':
            with open(self.ruta, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                contactos = list(reader)
                
        return contactos

    def guardar(self, datos):
        if self.tipo_archivo == 'json':
            with open(self.ruta, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4)
                
        elif self.tipo_archivo == 'csv':
            if not datos:
                return
            campos = ["nombre", "telefono", "email", "edad", "residencia"]
            with open(self.ruta, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                writer.writerows(datos)
