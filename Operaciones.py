class Operaciones():
    def registrar_venta(self, vehiculo_id, comprador_id, precio, moneda_id, vendedor_id=None):
        sql = """INSERT INTO ventas (vehiculo_id, comprador_id, precio_venta, moneda_id, vendedor_id) 
                 VALUES (%s, %s, %s, %s, %s)"""
        with self.obtener_conexion() as conn:
            if conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(sql, (vehiculo_id, comprador_id, precio, moneda_id, vendedor_id))
                    # Opcional: Podríamos actualizar automáticamente el propietario_actual_id en la tabla vehículos aquí mismo
                    conn.commit()
                    print("[ÉXITO] Venta registrada en el sistema.")
                except Exception as e:
                    print(f"[ERROR] Al procesar la venta: {e}")

    def registrar_multa(self, vehiculo_id, fecha, descripcion, monto, estado_pago_id=1):
        sql = """INSERT INTO multas (vehiculo_id, fecha_infraccion, descripcion, monto, estado_pago_id) 
                 VALUES (%s, %s, %s, %s, %s)"""
        with self.obtener_conexion() as conn:
            if conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(sql, (vehiculo_id, fecha, descripcion, monto, estado_pago_id))
                    conn.commit()
                    print(f"[ÉXITO] Infracción cargada al vehículo ID {vehiculo_id}.")
                except Exception as e:
                    print(f"[ERROR] Al registrar multa: {e}")