class Multa:
    def __init__(self):
        self.lista_multas = []
        self.contador_id = 1

    def guardar(self, vehiculo_id, fecha, descripcion, monto, estado_pago_id):
        nueva_multa = {
            "id": self.contador_id,
            "vehiculo_id": vehiculo_id,
            "fecha": fecha,
            "descripcion": descripcion,
            "monto": monto,
            "estado_pago_id": estado_pago_id
        }
        self.lista_multas.append(nueva_multa)
        print(f"\n[ÉXITO] Multa guardada con el ID: {self.contador_id}")
        self.contador_id += 1

    def actualizar(self, id_multa, nuevo_estado_pago_id, nuevo_monto):
        encontrado = False
        for m in self.lista_multas:
            if m["id"] == int(id_multa):
                m["estado_pago_id"] = nuevo_estado_pago_id
                m["monto"] = nuevo_monto
                encontrado = True
                print(f"\n[ÉXITO] Multa ID {id_multa} actualizada.")
                break
        
        if not encontrado:
            print("\n[ERROR] No se encontró esa multa.")

    def eliminar(self, id_multa):
        encontrado = False
        for m in self.lista_multas:
            if m["id"] == int(id_multa):
                self.lista_multas.remove(m)
                encontrado = True
                print(f"\n[ÉXITO] Multa ID {id_multa} eliminada.")
                break
                
        if not encontrado:
            print("\n[ERROR] No se encontró esa multa.")