class Vehiculo:
    def __init__(self):
        # Esta lista simula la tabla de vehículos
        self.lista_vehiculos = []
        self.contador_id = 1

    def guardar(self, patente, vin, modelo, combustible, moneda, estado, anio, precio, fecha, propietario_id):
        nuevo_vehiculo = {
            "id": self.contador_id,
            "patente": patente,
            "vin": vin,
            "modelo": modelo,
            "combustible": combustible,
            "moneda": moneda,
            "estado": estado,
            "anio": anio,
            "precio": precio,
            "fecha": fecha,
            "propietario_id": propietario_id
        }
        self.lista_vehiculos.append(nuevo_vehiculo)
        print(f"\n[ÉXITO] Vehículo guardado con el ID: {self.contador_id}")
        self.contador_id += 1

    def actualizar(self, id_vehiculo, nuevo_estado, nuevo_propietario_id):
        encontrado = False
        for v in self.lista_vehiculos:
            if v["id"] == int(id_vehiculo):
                v["estado"] = nuevo_estado
                v["propietario_id"] = nuevo_propietario_id
                encontrado = True
                print(f"\n[ÉXITO] Vehículo con ID {id_vehiculo} actualizado.")
                break
        
        if not encontrado:
            print("\n[ERROR] No se encontró ese vehículo.")

    def eliminar(self, id_vehiculo):
        encontrado = False
        for v in self.lista_vehiculos:
            if v["id"] == int(id_vehiculo):
                self.lista_vehiculos.remove(v)
                encontrado = True
                print(f"\n[ÉXITO] Vehículo con ID {id_vehiculo} eliminado.")
                break
                
        if not encontrado:
            print("\n[ERROR] No se encontró ese vehículo.")