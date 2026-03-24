class Contacto:
    def __init__(self, nombre, telefono, email, edad, residencia):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.edad = int(edad)
        self.residencia = residencia

    def to_dict(self):
        # Facilita la conversión a formato diccionario para guardar en JSON/CSV
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email,
            "edad": self.edad,
            "residencia": self.residencia
        }

    def __str__(self):
        return f"👤 {self.nombre} | 📞 {self.telefono} | ✉️ {self.email} | 🎂 {self.edad} años | 🏠 {self.residencia}"
