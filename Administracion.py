from conexion import ConexionDB


class Administracion:

    @classmethod
    def obtener_conexion(cls):
        return ConexionDB().obtener_conexion()

    @classmethod
    def listar_marcas(cls):

        conn = cls.obtener_conexion()
        if not conn:
            return

        cursor = None

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT marca_id, nombre_marca
                FROM marcas
                WHERE deleted = 0
                ORDER BY nombre_marca
            """)

            marcas = cursor.fetchall()

            if not marcas:
                print("\n[AVISO] No hay marcas registradas.")
                return

            print(f"\n{'ID':<6} | {'NOMBRE DE LA MARCA':<25}")
            print("-" * 35)

            for marca_id, nombre in marcas:
                print(f"{marca_id:<6} | {nombre:<25}")

        except Exception as err:
            print(f"\n[ERROR] {err}")

        finally:
            if cursor:
                cursor.close()
            conn.close()

    @classmethod
    def listar_modelos(cls):

        conn = cls.obtener_conexion()
        if not conn:
            return

        cursor = None

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    mo.modelo_id,
                    ma.nombre_marca,
                    mo.nombre_modelo
                FROM modelos mo
                INNER JOIN marcas ma
                    ON mo.marca_id = ma.marca_id
                WHERE mo.deleted = 0
                ORDER BY ma.nombre_marca, mo.nombre_modelo
            """)

            modelos = cursor.fetchall()

            if not modelos:
                print("\n[AVISO] No hay modelos registrados.")
                return

            print(f"\n{'ID':<6} | {'MARCA':<20} | {'MODELO':<25}")
            print("-" * 60)

            for modelo_id, marca, modelo in modelos:
                print(f"{modelo_id:<6} | {marca:<20} | {modelo:<25}")

        except Exception as err:
            print(f"\n[ERROR] {err}")

        finally:
            if cursor:
                cursor.close()
            conn.close()

    @classmethod
    def agregar_marca(cls, nombre_marca):

        nombre = nombre_marca.strip()

        if not nombre:
            print("\n[ERROR] Debe ingresar un nombre válido.")
            return

        conn = cls.obtener_conexion()
        if not conn:
            return

        cursor = None

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO marcas (nombre_marca)
                VALUES (%s)
            """, (nombre,))

            conn.commit()

            print(f"\n[ÉXITO] Marca '{nombre}' agregada correctamente.")

        except Exception as err:
            print(f"\n[ERROR SQL] {err}")

        finally:
            if cursor:
                cursor.close()
            conn.close()

    @classmethod
    def agregar_modelo(cls, marca_id, nombre_modelo):

        nombre = nombre_modelo.strip()

        if not nombre:
            print("\n[ERROR] Debe ingresar un nombre válido.")
            return

        if not str(marca_id).isdigit():
            print("\n[ERROR] ID de marca inválido.")
            return

        conn = cls.obtener_conexion()
        if not conn:
            return

        cursor = None

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO modelos (marca_id, nombre_modelo)
                VALUES (%s, %s)
            """, (marca_id, nombre))

            conn.commit()

            print(f"\n[ÉXITO] Modelo '{nombre}' agregado correctamente.")

        except Exception as err:
            print(f"\n[ERROR SQL] {err}")

        finally:
            if cursor:
                cursor.close()
            conn.close()