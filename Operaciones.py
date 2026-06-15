from Administracion import Administracion

class Operaciones:

    @classmethod
    def registrar_venta(
        cls,
        vehiculo_id,
        comprador_id,
        precio,
        moneda_id,
        vendedor_id=None
    ):
        conn = Administracion.obtener_conexion()
        if not conn:
            return

        cursor = None
        try:
            cursor = conn.cursor()
            # Añadido "registroautomotriz." para evitar errores de selección de BD
            cursor.execute("""
                INSERT INTO registroautomotriz.ventas
                (
                    vehiculo_id,
                    comprador_id,
                    precio_venta,
                    moneda_id,
                    vendedor_id
                )
                VALUES (%s,%s,%s,%s,%s)
            """, (
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
            if cursor:
                cursor.close()
            conn.close()

    @classmethod
    def registrar_multa(
        cls,
        vehiculo_id,
        fecha,
        descripcion,
        monto,
        estado_pago_id=1
    ):
        conn = Administracion.obtener_conexion()
        if not conn:
            return

        cursor = None
        try:
            cursor = conn.cursor()
            # Añadido "registroautomotriz." para asegurar la persistencia
            cursor.execute("""
                INSERT INTO registroautomotriz.multas
                (
                    vehiculo_id,
                    fecha_infraccion,
                    descripcion,
                    monto,
                    estado_pago_id
                )
                VALUES (%s,%s,%s,%s,%s)
            """, (
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
            if cursor:
                cursor.close()
            conn.close()

    @classmethod
    def ver_multas(cls):
        """Método que le faltaba a tu sistema para la opción 9"""
        conn = Administracion.obtener_conexion()
        if not conn:
            return

        cursor = None
        try:
            cursor = conn.cursor()
            # Traemos las multas activas (deleted = 0)
            cursor.execute("""
                SELECT multa_id, vehiculo_id, fecha_infraccion, descripcion, monto, estado_pago_id 
                FROM registroautomotriz.multas 
                WHERE deleted = 0
            """)
            
            multas = cursor.fetchall()

            if not multas:
                print("\n[INFO] No hay multas registradas en el sistema.")
            else:
                print(f"{'ID':<6} | {'Vehículo ID':<12} | {'Fecha':<20} | {'Monto':<10} | {'Descripción'}")
                print("-" * 80)
                for m in multas:
                    # m[2] suele ser un objeto datetime, lo formateamos a texto legible
                    fecha_str = m[2].strftime('%Y-%m-%d %H:%M') if hasattr(m[2], 'strftime') else str(m[2])
                    print(f"{m[0]:<6} | {m[1]:<12} | {fecha_str:<20} | ${m[4]:<9} | {m[3]}")
            
            # Pausa para que el usuario pueda leer los datos antes de que main.py limpie la pantalla
            input("\nPresione Enter para volver al menú...")

        except Exception as e:
            print(f"[ERROR al consultar multas] {e}")
            input("\nPresione Enter para continuar...")

        finally:
            if cursor:
                cursor.close()
            conn.close()