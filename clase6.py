class Modelo:
    def __init__(self):
        self.lista_modelos = []
        self.contador_id = 1

    def guardar(self, marca_id, nombre_modelo):
        nuevo_modelo = {
            "id": self.contador_id,
            "marca_id": marca_id,
            "nombre": nombre_modelo
        }
        self.lista_modelos.append(nuevo_modelo)
        print(f"\n[ÉXITO] Modelo '{nombre_modelo}' guardado con el ID: {self.contador_id}")
        self.contador_id += 1

    def actualizar(self, id_modelo, nuevo_nombre):
        encontrado = False
        for m in self.lista_modelos:
            if m["id"] == int(id_modelo):
                m["nombre"] = nuevo_nombre
                encontrado = True
                print(f"\n[ÉXITO] Modelo ID {id_modelo} actualizado a '{nuevo_nombre}'.")
                break
        
        if not encontrado:
            print("\n[ERROR] No se encontró ese modelo.")

    def eliminar(self, id_modelo):
        encontrado = False
        for m in self.lista_modelos:
            if m["id"] == int(id_modelo):
                self.lista_modelos.remove(m)
                encontrado = True
                print(f"\n[ÉXITO] Modelo ID {id_modelo} eliminado.")
                break
                
        if not encontrado:
            print("\n[ERROR] No se encontró ese modelo.")