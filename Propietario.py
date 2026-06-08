from Administracion import Administracion

class Propietario(Administracion):

    @classmethod
    def guardar(cls, documento, nombre, apellido,
                telefono=None, email=None, direccion=None):

        conn = cls.obtener_conexion()

        if not conn:
            return

        try:
            cursor = conn.cursor()

            sql = """
            INSERT INTO propietarios
            (
                documento_identidad,
                nombre,
                apellido,
                telefono,
                email,
                direccion
            )
            VALUES (%s,%s,%s,%s,%s,%s)
            """

            cursor.execute(
                sql,
                (
                    documento,
                    nombre,
                    apellido,
                    telefono,
                    email,
                    direccion
                )
            )

            conn.commit()

            print(f"[ÉXITO] Propietario {nombre} {apellido} registrado.")

        except Exception as e:
            print(f"[ERROR] {e}")

        finally:
            cursor.close()
            conn.close()

    @classmethod
    def listar(cls):

        conn = cls.obtener_conexion()

        if not conn:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT propietario_id,
                       documento_identidad,
                       nombre,
                       apellido
                FROM propietarios
                WHERE deleted = 0
            """)

            registros = cursor.fetchall()

            for r in registros:
                print(r)

        except Exception as e:
            print(f"[ERROR] {e}")

        finally:
            cursor.close()
            conn.close()