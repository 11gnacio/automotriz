class Vehiculo():
    def guardar(self, patente, vin, modelo_id, combustible_id, moneda_id, estado_id, anio, precio, fecha, propietario_id=None):
        sql = """INSERT INTO vehiculos (patente_dominio, vin_chasis, modelo_id, combustible_id, moneda_id, 
                 estado_id, anio_fabricacion, precio_adquisicion, fecha_adquisicion, propietario_actual_id) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        with self.obtener_conexion() as conn:
            if conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(sql, (patente, vin, modelo_id, combustible_id, moneda_id, estado_id, anio, precio, fecha, propietario_id))
                    conn.commit()
                    print(f"[ÉXITO] Vehículo con patente {patente} registrado.")
                except Exception as e:
                    print(f"[ERROR] Al registrar vehículo: {e}")

    def listar_detallado(self):
        sql = """
            SELECT v.vehiculo_id, v.patente_dominio AS Patente, ma.nombre_marca AS Marca, mo.nombre_modelo AS Modelo,
                   tc.nombre_combustible AS Combustible, ev.nombre_estado AS Estado_Vehiculo, v.anio_fabricacion AS Anio,
                   CONCAT(p.nombre, ' ', p.apellido) AS Propietario_Actual
            FROM vehiculos v
            INNER JOIN modelos mo ON v.modelo_id = mo.modelo_id
            INNER JOIN marcas ma ON mo.marca_id = ma.marca_id
            INNER JOIN tipos_combustible tc ON v.combustible_id = tc.combustible_id
            INNER JOIN estados_vehiculo ev ON v.estado_id = ev.estado_id
            LEFT JOIN propietarios p ON v.propietario_actual_id = p.propietario_id
            WHERE v.deleted = 0;
        """
        with self.obtener_conexion() as conn:
            if conn:
                cursor = conn.connector.cursor(dictionary=True) if hasattr(conn, 'connector') else conn.cursor(dictionary=True)
                cursor.execute(sql)
                return cursor.fetchall()
        return []