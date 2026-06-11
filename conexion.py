import mysql.connector
from mysql.connector import Error


class ConexionDB:

    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "1234",  # Si usas XAMPP y no funciona, prueba dejándolo vacío: ''
            "database": "registroautomotriz",
        }

    def obtener_conexion(self):
        """Devuelve una conexión activa a MySQL utilizando el conector puro

        para evitar errores de compatibilidad en Python 3.14.
        """
        try:
            # Añadimos use_pure=True para solucionar el RuntimeError
            conexion = mysql.connector.connect(**self.config, use_pure=True)

            if conexion.is_connected():
                return conexion

            return None

        except Error as e:
            # Ahora este print sí se ejecutará y te dirá el problema real
            print(f"\n[ERROR BD] No se pudo conectar: {e}\n")
            return None

    def cerrar_conexion(self, conexion):
        """Cierra la conexión de forma segura."""
        if conexion and conexion.is_connected():
            conexion.close()