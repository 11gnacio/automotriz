class TipoCombustible:
    def __init__(self):
        self.lista_combustibles = []
        self.contador_id = 1

    def guardar(self, nombre_combustible):
        nuevo_combustible = {
            "id": self.contador_id,
            "nombre": nombre_combustible
        }
        self.lista_combustibles.append(nuevo_combustible)
        print(f"\n[ÉXITO] Combustible '{nombre_combustible}' guardado con el ID: {self.contador_id}")
        self.contador_id += 1

    def actualizar(self, id_combustible, nuevo_nombre):
        encontrado = False
        for c in self.lista_combustibles:
            if c["id"] == int(id_combustible):
                c["nombre"] = nuevo_nombre
                encontrado = True
                print(f"\n[ÉXITO] Combustible ID {id_combustible} actualizado.")
                break
        
        if not encontrado:
            print("\n[ERROR] No se encontró ese tipo de combustible.")

    def eliminar(self, id_combustible):
        encontrado = False
        for c in self.lista_combustibles:
            if c["id"] == int(id_combustible):
                self.lista_combustibles.remove(c)
                encontrado = True
                print(f"\n[ÉXITO] Combustible ID {id_combustible} eliminado.")
                break
                
        if not encontrado:
            print("\n[ERROR] No se encontró ese tipo de combustible.")