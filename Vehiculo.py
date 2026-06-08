from Administracion import Administracion

class Vehiculo(Administracion):

    @classmethod
    def guardar(cls, patente, vin, modelo_id,
                combustible_id, moneda_id,
                estado_id, anio, precio,
                fecha, propietario_id=None):

        conn = cls.obtener_conexion()

        if not conn:
            return

        try:
            cursor = conn.cursor()

            sql = """
            INSERT INTO vehiculos
            (
                patente_dominio,
                vin_chasis,
                modelo_id,
                combustible_id,
                moneda_id,
                estado_id,
                anio_fabricacion,
                precio_adquisicion,
                fecha_adquisicion,
                propietario_actual_id
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            cursor.execute(
                sql,
                (
                    patente,
                    vin,
                    modelo_id,
                    combustible_id,
                    moneda_id,
                    estado_id,
                    anio,
                    precio,
                    fecha,
                    propietario_id
                )
            )

            conn.commit()

            print("[ÉXITO] Vehículo registrado.")

        except Exception as e:
            print(f"[ERROR] {e}")

        finally:
            cursor.close()
            conn.close()

    @classmethod
    def listar_detallado(cls):

        conn = cls.obtener_conexion()

        if not conn:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
            SELECT
                v.vehiculo_id,
                v.patente_dominio,
                ma.nombre_marca,
                mo.nombre_modelo,
                v.anio_fabricacion
            FROM vehiculos v
            INNER JOIN modelos mo ON v.modelo_id = mo.modelo_id
            INNER JOIN marcas ma ON mo.marca_id = ma.marca_id
            WHERE v.deleted = 0
            """)

            registros = cursor.fetchall()

            for r in registros:
                print(r)

        except Exception as e:
            print(f"[ERROR] {e}")

        finally:
            cursor.close()
            conn.close()