from Administracion import Administracion


class Vehiculo:

    @classmethod
    def guardar(
        cls,
        patente,
        vin,
        modelo_id,
        combustible_id,
        moneda_id,
        estado_id,
        anio,
        precio,
        fecha,
        propietario_id=None
    ):

        # VALIDACIONES BÁSICAS
        if not patente.strip():
            print("[ERROR] La patente no puede estar vacía.")
            return

        if not vin.strip():
            print("[ERROR] El VIN no puede estar vacío.")
            return

        if not str(modelo_id).isdigit():
            print("[ERROR] modelo_id inválido.")
            return

        if not str(combustible_id).isdigit():
            print("[ERROR] combustible_id inválido.")
            return

        if not str(estado_id).isdigit():
            print("[ERROR] estado_id inválido.")
            return

        conn = Administracion.obtener_conexion()

        if not conn:
            return

        cursor = None

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

            cursor.execute(sql, (
                patente.strip(),
                vin.strip(),
                modelo_id,
                combustible_id,
                moneda_id,
                estado_id,
                anio,
                precio,
                fecha,
                propietario_id
            ))

            conn.commit()

            print("[ÉXITO] Vehículo registrado correctamente.")

        except Exception as e:
            print(f"[ERROR] No se pudo registrar el vehículo: {e}")

        finally:
            if cursor:
                cursor.close()
            conn.close()

    @classmethod
    def listar_detallado(cls):

        conn = Administracion.obtener_conexion()

        if not conn:
            return

        cursor = None

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    v.vehiculo_id,
                    v.patente_dominio,
                    ma.nombre_marca,
                    mo.nombre_modelo,
                    tc.nombre_combustible,
                    ev.nombre_estado,
                    v.anio_fabricacion,
                    v.precio_adquisicion
                FROM vehiculos v
                INNER JOIN modelos mo
                    ON v.modelo_id = mo.modelo_id
                INNER JOIN marcas ma
                    ON mo.marca_id = ma.marca_id
                INNER JOIN tipos_combustible tc
                    ON v.combustible_id = tc.combustible_id
                INNER JOIN estados_vehiculo ev
                    ON v.estado_id = ev.estado_id
                WHERE v.deleted = 0
                ORDER BY v.vehiculo_id
            """)

            registros = cursor.fetchall()

            if not registros:
                print("\n[AVISO] No hay vehículos registrados.")
                return

            print(
                f"\n{'ID':<4} | {'PATENTE':<15} | "
                f"{'MARCA':<15} | {'MODELO':<15} | "
                f"{'AÑO':<6} | {'PRECIO':<12}"
            )

            print("-" * 85)

            for r in registros:
                print(
                    f"{r[0]:<4} | "
                    f"{r[1]:<15} | "
                    f"{r[2]:<15} | "
                    f"{r[3]:<15} | "
                    f"{r[6]:<6} | "
                    f"{r[7]:<12}"
                )

        except Exception as e:
            print(f"[ERROR] No se pudieron listar los vehículos: {e}")

        finally:
            if cursor:
                cursor.close()
            conn.close()