class Propietario():
    def guardar(self, documento, nombre, apellido, telefono=None, email=None, direccion=None):
        sql = """INSERT INTO propietarios (documento_identidad, nombre, apellido, telefono, email, direccion) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        with self.obtener_conexion() as conn:
            if conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(sql, (documento, nombre, apellido, telefono, email, direccion))
                    conn.commit()
                    print(f"[ÉXITO] Propietario {nombre} {apellido} registrado.")
                except Exception as e:
                    print(f"[ERROR] Al registrar propietario: {e}")