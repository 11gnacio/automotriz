class Venta:
    def __init__(self):
        self.lista_ventas = []
        self.contador_id = 1

    def guardar(self, vehiculo_id, comprador_id, precio_venta, moneda_id, vendedor_id):
        nueva_venta = {
            "id": self.contador_id,
            "vehiculo_id": vehiculo_id,
            "comprador_id": comprador_id,
            "precio_venta": precio_venta,
            "moneda_id": moneda_id,
            "vendedor_id": vendedor_id
        }
        self.lista_ventas.append(nueva_venta)
        print(f"\n[ÉXITO] Venta guardada con el ID: {self.contador_id}")
        self.contador_id += 1

    def actualizar(self, id_venta, nuevo_precio, nueva_moneda):
        encontrado = False
        for v in self.lista_ventas:
            if v["id"] == int(id_venta):
                v["precio_venta"] = nuevo_precio
                v["moneda_id"] = nueva_moneda
                encontrado = True
                print(f"\n[ÉXITO] Venta ID {id_venta} actualizada.")
                break
        
        if not encontrado:
            print("\n[ERROR] No se encontró esa venta.")

    def eliminar(self, id_venta):
        encontrado = False
        for v in self.lista_ventas:
            if v["id"] == int(id_venta):
                self.lista_ventas.remove(v)
                encontrado = True
                print(f"\n[ÉXITO] Venta ID {id_venta} eliminada.")
                break
                
        if not encontrado:
            print("\n[ERROR] No se encontró esa venta.")