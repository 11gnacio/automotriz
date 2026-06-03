class Moneda:
    def __init__(self):
        self.lista_monedas = []

    def guardar(self, moneda_id, nombre_moneda):
        nueva_moneda = {
            "id": moneda_id, # Ejemplo: 'USD'
            "nombre": nombre_moneda # Ejemplo: 'Dólar'
        }
        self.lista_monedas.append(nueva_moneda)
        print(f"\n[ÉXITO] Moneda '{nombre_moneda}' registrada con el código: {moneda_id}")

    def actualizar(self, moneda_id_a_buscar, nuevo_nombre):
        encontrado = False
        for m in self.lista_monedas:
            if m["id"] == moneda_id_a_buscar:
                m["nombre"] = nuevo_nombre
                encontrado = True
                print(f"\n[ÉXITO] Moneda {moneda_id_a_buscar} actualizada a '{nuevo_nombre}'.")
                break
        
        if not encontrado:
            print("\n[ERROR] No se encontró la moneda con ese código.")

    def eliminar(self, moneda_id_a_buscar):
        encontrado = False
        for m in self.lista_monedas:
            if m["id"] == moneda_id_a_buscar:
                self.lista_monedas.remove(m)
                encontrado = True
                print(f"\n[ÉXITO] Moneda {moneda_id_a_buscar} eliminada.")
                break
                
        if not encontrado:
            print("\n[ERROR] No se encontró la moneda con ese código.")