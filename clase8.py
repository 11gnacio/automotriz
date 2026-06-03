class EstadoPagoMulta:
    def __init__(self):
        self.lista_estados_pago = []
        self.contador_id = 1

    def guardar(self, nombre_estado):
        nuevo_estado = {
            "id": self.contador_id,
            "nombre": nombre_estado
        }
        self.lista_estados_pago.append(nuevo_estado)
        print(f"\n[ÉXITO] Estado de pago '{nombre_estado}' guardado con el ID: {self.contador_id}")
        self.contador_id += 1

    def actualizar(self, id_estado, nuevo_nombre):
        encontrado = False
        for e in self.lista_estados_pago:
            if e["id"] == int(id_estado):
                e["nombre"] = nuevo_nombre
                encontrado = True
                print(f"\n[ÉXITO] Estado de pago ID {id_estado} actualizado a '{nuevo_nombre}'.")
                break
        
        if not encontrado:
            print("\n[ERROR] No se encontró ese estado de pago.")

    def eliminar(self, id_estado):
        encontrado = False
        for e in self.lista_estados_pago:
            if e["id"] == int(id_estado):
                self.lista_estados_pago.remove(e)
                encontrado = True
                print(f"\n[ÉXITO] Estado de pago ID {id_estado} eliminado.")
                break
                
        if not encontrado:
            print("\n[ERROR] No se encontró ese estado de pago.")