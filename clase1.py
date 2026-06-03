class Propietario:
    def __init__(self):
        # Esta lista simula la tabla de propietarios
        self.lista_propietarios = []
        self.contador_id = 1

    def guardar(self, documento, nombre, apellido, telefono, email, direccion):
        nuevo_propietario = {
            "id": self.contador_id,
            "documento": documento,
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
            "email": email,
            "direccion": direccion
        }
        self.lista_propietarios.append(nuevo_propietario)
        print(f"\n[ÉXITO] Propietario guardado con el ID: {self.contador_id}")
        self.contador_id += 1

    def actualizar(self, id_a_modificar, nuevo_tel, nuevo_email, nueva_dir):
        encontrado = False
        for p in self.lista_propietarios:
            if p["id"] == int(id_a_modificar):
                p["telefono"] = nuevo_tel
                p["email"] = nuevo_email
                p["direccion"] = nueva_dir
                encontrado = True
                print(f"\n[ÉXITO] Propietario con ID {id_a_modificar} actualizado.")
                break
        
        if not encontrado:
            print("\n[ERROR] No se encontró ningún propietario con ese ID.")

    def eliminar(self, id_a_eliminar):
        encontrado = False
        for p in self.lista_propietarios:
            if p["id"] == int(id_a_eliminar):
                self.lista_propietarios.remove(p)
                encontrado = True
                print(f"\n[ÉXITO] Propietario con ID {id_a_eliminar} eliminado.")
                break
        
        if not encontrado:
            print("\n[ERROR] No se encontró ningún propietario con ese ID.")