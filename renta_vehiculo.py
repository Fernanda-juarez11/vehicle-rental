import mysql.connector
from datetime import datetime

conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="renta"
)     


def calcular_precio(tipoVehiculo: str, diasRenta: int) -> float:
    if tipoVehiculo == "Car":
        return diasRenta * 200
    elif tipoVehiculo == "Motorcycle":
        return diasRenta * 100
    elif tipoVehiculo == "SUV":
        return diasRenta * 350
    else:
        raise ValueError("Tipo de vehículo inválido")

def calcular_estado(diasRenta: int) -> str:
    return "LongRental" if diasRenta >= 5 else "ShortRental"


class RentaCRUD:
    def __init__(self):
        self.rentas = []
        self.id_counter = 1

    # CREATE
    def crear_renta(self, nombreCliente: str, edad: int, tipoVehiculo: str, diasRenta: int):
        precioFinal = calcular_precio(tipoVehiculo, diasRenta)
        estado = calcular_estado(diasRenta)
        registro = {
            "id": self.id_counter,
            "nombreCliente": nombreCliente,
            "edad": edad,
            "tipoVehiculo": tipoVehiculo,
            "diasRenta": diasRenta,
            "precioFinal": precioFinal,
            "estado": estado
        }
        self.rentas.append(registro)
        self.id_counter += 1
        return registro

    # READ
    def leer_rentas(self):
        return self.rentas

    # UPDATE
    def actualizar_renta(self, id: int, diasRenta: int):
        for renta in self.rentas:
            if renta["id"] == id:
                renta["diasRenta"] = diasRenta
                renta["precioFinal"] = calcular_precio(renta["tipoVehiculo"], diasRenta)
                renta["estado"] = calcular_estado(diasRenta)
                return renta
        return None

    def eliminar_renta(self, id: int):
        self.rentas = [r for r in self.rentas if r["id"] != id]
