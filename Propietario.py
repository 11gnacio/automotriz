from Administracion import Administracion


class Propietario:

    @classmethod
    def guardar(
        cls,
        documento,
        nombre,
        apellido,
        telefono=None,
        email=None,
        direccion=None
    ):

        if not documento.strip():
            print("[ERROR] Documento inválido.")
            return

        if not nombre.strip():
            print("[ERROR] Nombre inválido.")
            return

        if not apellido.strip():
            print("[ERROR] Apellido inválido.")
            return

        conn = Administracion.obtener_conexion()

        if not conn:
            return

        cursor = None

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

            cursor.execute(sql, (
                documento.strip(),
                nombre.strip(),
                apellido.strip(),
                telefono,
                email,
                direccion
            ))

            conn.commit()

            print(f"[ÉXITO] Propietario {nombre} {apellido} registrado.")

        except Exception as e:
            print(f"[ERROR] {e}")

        finally:
            if cursor:
                cursor.close()
            conn.close()

    @classmethod
    def listar(cls):

        conn = Administracion.obtener_conexion()

        if not conn:
            return

        cursor = None

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    propietario_id,
                    documento_identidad,
                    nombre,
                    apellido,
                    telefono,
                    email
                FROM propietarios
                WHERE deleted = 0
                ORDER BY apellido, nombre
            """)

            registros = cursor.fetchall()

            if not registros:
                print("\n[AVISO] No hay propietarios registrados.")
                return

            print(
                f"\n{'ID':<5} | {'DOCUMENTO':<12} | "
                f"{'NOMBRE':<15} | {'APELLIDO':<15}"
            )

            print("-" * 60)

            for r in registros:
                print(
                    f"{r[0]:<5} | {r[1]:<12} | "
                    f"{r[2]:<15} | {r[3]:<15}"
                )

        except Exception as e:
            print(f"[ERROR] {e}")

        finally:
            if cursor:
                cursor.close()
            conn.close()