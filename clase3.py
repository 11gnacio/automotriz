class Marca:
    def __init__(self):
        # Esta lista simula la tabla de marcas
        self.lista_marcas = []
        self.contador_id = 1

    def guardar(self, nombre_marca):
        nueva_marca = {
            "id": self.contador_id,
            "nombre": nombre_marca
        }
        self.lista_marcas.append(nueva_marca)
        print(f"\n[ÉXITO] Marca '{nombre_marca}' guardada con el ID: {self.contador_id}")
        self.contador_id += 1

    def actualizar(self, id_marca, nuevo_nombre):
        encontrado = False
        for m in self.lista_marcas:
            if m["id"] == int(id_marca):
                m["nombre"] = nuevo_nombre
                encontrado = True
                print(f"\n[ÉXITO] Marca ID {id_marca} actualizada a '{nuevo_nombre}'.")
                break
        
        if not encontrado:
            print("\n[ERROR] No se encontró esa marca.")

    def eliminar(self, id_marca):
        encontrado = False
        for m in self.lista_marcas:
            if m["id"] == int(id_marca):
                self.lista_marcas.remove(m)
                encontrado = True
                print(f"\n[ÉXITO] Marca ID {id_marca} eliminada.")
                break
                
        if not encontrado:
            print("\n[ERROR] No se encontró esa marca.")