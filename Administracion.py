import mysql.connector


class Administracion:

    @classmethod
    def obtener_conexion(cls):
        """
        Establece la conexión nativa con la base de datos MySQL
        """
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="tu_contraseña",  # Reemplaza por tu contraseña real
                database="registroautomotriz"
            )

        except Exception as e:
            print(
                f"\n[ERROR DE CONEXIÓN] "
                f"Comprueba si MySQL está encendido: {e}"
            )
            return None

    @classmethod
    def listar_marcas(cls):
        """
        Muestra las marcas registradas.
        Si la tabla está vacía, lo maneja sin romperse.
        """

        conn = cls.obtener_conexion()

        if not conn:
            return

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT marca_id, nombre_marca
                FROM marcas
                WHERE deleted = 0
                """
            )

            marcas = cursor.fetchall()

            if not marcas:
                print(
                    "\n[AVISO] No hay ninguna marca registrada "
                    "en la base de datos aún."
                )
                return

            print(f"\n{'ID':<6} | {'NOMBRE DE LA MARCA':<25}")
            print("-" * 35)

            for marca in marcas:
                print(f"{marca[0]:<6} | {marca[1]:<25}")

        except Exception as err:
            print(
                f"\n[ERROR] No fue posible listar las marcas: {err}"
            )

        finally:
            cursor.close()
            conn.close()

    @classmethod
    def listar_modelos(cls):
        """
        Muestra los modelos registrados.
        Soporta tablas vacías de forma segura.
        """

        conn = cls.obtener_conexion()

        if not conn:
            return

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT modelo_id, nombre_modelo
                FROM modelos
                WHERE deleted = 0
                """
            )

            modelos = cursor.fetchall()

            if not modelos:
                print(
                    "\n[AVISO] No hay ningún modelo registrado "
                    "en la base de datos aún."
                )
                return

            print(f"\n{'ID':<6} | {'NOMBRE DEL MODELO':<25}")
            print("-" * 35)

            for modelo in modelos:
                print(f"{modelo[0]:<6} | {modelo[1]:<25}")

        except Exception as err:
            print(
                f"\n[ERROR] No fue posible listar los modelos: {err}"
            )

        finally:
            cursor.close()
            conn.close()

    @classmethod
    def agregar_marca(cls, nombre_marca):
        """
        Inserta una nueva marca en la base de datos.
        """

        conn = cls.obtener_conexion()

        if not conn:
            return

        try:
            cursor = conn.cursor()

            sql = """
                INSERT INTO marcas (nombre_marca)
                VALUES (%s)
            """

            cursor.execute(sql, (nombre_marca,))
            conn.commit()

            print(
                f"\n[ÉXITO] Marca '{nombre_marca}' "
                f"agregada correctamente."
            )

        except Exception as err:
            print(
                f"\n[ERROR SQL] No se pudo guardar la marca: {err}"
            )

        finally:
            cursor.close()
            conn.close()

    @classmethod
    def agregar_modelo(cls, marca_id, nombre_modelo):
        """
        Inserta un nuevo modelo asociado a una marca.
        """

        conn = cls.obtener_conexion()

        if not conn:
            return

        try:
            cursor = conn.cursor()

            sql = """
                INSERT INTO modelos
                (marca_id, nombre_modelo)
                VALUES (%s, %s)
            """

            cursor.execute(
                sql,
                (marca_id, nombre_modelo)
            )

            conn.commit()

            print(
                f"\n[ÉXITO] Modelo '{nombre_modelo}' "
                f"agregado correctamente."
            )

        except Exception as err:
            print(
                "\n[ERROR SQL] No se pudo guardar el modelo "
                f"(verifica el ID de marca): {err}"
            )

        finally:
            cursor.close()
            conn.close()