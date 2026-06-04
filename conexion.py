import mysql.connector
from mysql.connector import Error

class ConexionDB:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'tu_contraseña', # Cambia por tu contraseña
            'database': 'registroautomotriz'
        }

    def obtener_conexion(self):
        try:
            return mysql.connector.connect(**self.config)
        except Error as e:
            print(f"[ERROR BD] No se pudo conectar: {e}")
            return None