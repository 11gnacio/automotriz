from Administracion import Administracion

class Operaciones(Administracion):

    @classmethod
    def registrar_venta(cls, vehiculo_id, comprador_id,
                         precio, moneda_id,
                         vendedor_id=None):

        conn = cls.obtener_conexion()

        if not conn:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO ventas
                (
                    vehiculo_id,
                    comprador_id,
                    precio_venta,
                    moneda_id,
                    vendedor_id
                )
                VALUES (%s,%s,%s,%s,%s)
            """,
            (
                vehiculo_id,
                comprador_id,
                precio,
                moneda_id,
                vendedor_id
            ))

            conn.commit()

            print("[ÉXITO] Venta registrada.")

        except Exception as e:
            print(f"[ERROR] {e}")

        finally:
            cursor.close()
            conn.close()

    @classmethod
    def registrar_multa(cls, vehiculo_id,
                         fecha,
                         descripcion,
                         monto,
                         estado_pago_id=1):

        conn = cls.obtener_conexion()

        if not conn:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO multas
                (
                    vehiculo_id,
                    fecha_infraccion,
                    descripcion,
                    monto,
                    estado_pago_id
                )
                VALUES (%s,%s,%s,%s,%s)
            """,
            (
                vehiculo_id,
                fecha,
                descripcion,
                monto,
                estado_pago_id
            ))

            conn.commit()

            print("[ÉXITO] Multa registrada.")

        except Exception as e:
            print(f"[ERROR] {e}")

        finally:
            cursor.close()
            conn.close()