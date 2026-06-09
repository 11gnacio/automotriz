import mysql.connector
from mysql.connector import Error


class ConexionDB:

    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '1234',
            'database': 'registroautomotriz'
        }

    def obtener_conexion(self):
        """
        Devuelve una conexión activa a MySQL.
        """

        try:
            conexion = mysql.connector.connect(**self.config)

            if conexion.is_connected():
                return conexion

            return None

        except Error as e:
            print(f"[ERROR BD] No se pudo conectar: {e}")
            return None

    def cerrar_conexion(self, conexion):
        """
        Cierra la conexión de forma segura.
        """

        if conexion and conexion.is_connected():
            conexion.close()