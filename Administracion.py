# Administracion.py
import mysql.connector

class Administracion:

    @classmethod
    def obtener_conexion(cls):
        """Establece la conexión nativa con la base de datos MySQL"""
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="tu_contraseña",  # REEMPLAZA AQUÍ CON TU CONTRASEÑA REAL
                database="registroautomotriz"
            )
        except Exception as e:
            print(f"\n[ERROR DE CONEXIÓN] Comprueba si MySQL está encendido: {e}")
            return None

    @classmethod
    def listar_marcas(cls):
        """Muestra las marcas registradas. Si la tabla está vacía, lo maneja sin romperse."""
        conn = cls.obtener_conexion()
        if not conn:
            return

        try:
            # Usamos el cursor tradicional (sin diccionarios) para máxima estabilidad
            cursor = conn.cursor()
            cursor.execute("SELECT marca_id, nombre_marca FROM marcas WHERE deleted = 0;")
            marcas = cursor.fetchall()
            
            # CONTROL CRÍTICO: Validamos si la lista está vacía antes de procesar nada
            if not marcas or len(marcas) == 0:
                print("\n[AVISO] No hay ninguna marca registrada en la base de datos aún.")
                cursor.close()
                return

            print(f"\n{'ID':<6} | {'NOMBRE DE LA MARCA':<25}")
            print("-" * 35)
            
            # Como es un cursor tradicional, leemos por índices numéricos m[0], m[1]
            for m in marcas:
                print(f"{m[0]:<6} | {m[1]:<25}")
                    
            cursor.close()
        except Exception as err:
            print(f"\n[AVISO] La tabla de marcas está vacía o inaccesible temporalmente.")
        finally:
            conn.close()

    @classmethod
    def listar_modelos(cls):
        """Muestra los modelos registrados. Soporta tablas vacías de forma segura."""
        conn = cls.obtener_conexion()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT modelo_id, nombre_modelo FROM modelos WHERE deleted = 0;")
            modelos = cursor.fetchall()
            
            # CONTROL CRÍTICO: Validamos si la lista está vacía
            if not modelos or len(modelos) == 0:
                print("\n[AVISO] No hay ningún modelo registrado en la base de datos aún.")
                cursor.close()
                return

            print(f"\n{'ID':<6} | {'NOMBRE DEL MODELO':<25}")
            print("-" * 35)
            
            for mod in modelos:
                print(f"{mod[0]:<6} | {mod[1]:<25}")
                    
            cursor.close()
        except Exception as err:
            print(f"\n[AVISO] La tabla de modelos está vacía o inaccesible temporalmente.")
        finally:
            conn.close()

    @classmethod
    def agregar_marca(cls, nombre_marca):
        """Inserta una nueva marca en la base de datos"""
        conn = cls.obtener_conexion()
        if not conn:
            return
            
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO marcas (nombre_marca) VALUES (%s);"
            cursor.execute(sql, (nombre_marca,))
            conn.commit()
            print(f"\n[ÉXITO] Marca '{nombre_marca}' agregada correctamente.")
            cursor.close()
        except Exception as err:
            print(f"\n[ERROR SQL] No se pudo guardar la marca: {err}")
        finally:
            conn.close()

    @classmethod
    def agregar_modelo(cls, marca_id, nombre_modelo):
        """Inserta un nuevo modelo asociado a un ID de marca"""
        conn = cls.obtener_conexion()
        if not conn:
            return
            
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO modelos (marca_id, nombre_modelo) VALUES (%s, %s);"
            cursor.execute(sql, (marca_id, nombre_modelo))
            conn.commit()
            print(f"\n[ÉXITO] Modelo '{nombre_modelo}' agregado correctamente.")
            cursor.close()
        except Exception as err:
            print(f"\n[ERROR SQL] No se pudo guardar el modelo (verifica si el ID de Marca existe): {err}")
        finally:
            conn.close()