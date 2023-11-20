from Animal import Animal
import Credenciales
import mysql.connector

class DAO:
    def __init__(self):
        pass
    
    def __conectar(self):
        self.__conexion = mysql.connector.connect(**Credenciales.get_credenciales())
        self.__cursor = self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()
    
    def registrar_animal(self, a: Animal):
        self.__conectar()
        sql = "INSERT INTO animal (codigo, raza, patas, peso) VALUES (%s, %s, %s, %s)"
        values = (a.get_codigo(), a.get_raza(), a.get_patas(), a.get_peso())
        self.__cursor.execute(sql, values)
        self.__cerrar()

    def buscar_animal(self, codigo: str) -> Animal:
        self.__conectar()
        sql = "SELECT * FROM animal WHERE codigo = %s"
        values = (codigo,)
        self.__cursor.execute(sql, values)
        respuesta = self.__cursor.fetchone()
        self.__cerrar()
        if respuesta is not None:
            a = Animal(respuesta[1], respuesta[2], respuesta[3], respuesta[4], respuesta[0])
            return a
        else:
            return None

    def modificar_animal(self, a: Animal):
        self.__conectar()
        sql = "UPDATE animal SET codigo = %s, raza = %s, peso = %s, patas = %s WHERE id = %s"
        values = (a.get_codigo(), a.get_raza(), a.get_peso(), a.get_patas(), a.get_id())
        self.__cursor.execute(sql, values)
        self.__cerrar()
    
    def eliminar_animal(self, id: int):
        self.__conectar()
        sql = "DELETE FROM animal WHERE id = %s"
        values = (id,)
        self.__cursor.execute(sql, values)
        self.__cerrar()

    def mostrar_animales(self):
        self.__conectar()
        sql = "SELECT * FROM animal"
        self.__cursor.execute(sql)
        resultado = self.__cursor.fetchall()
        animales = []
        for tupla in resultado:
            a = Animal(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
            animales.append(a)
        self.__cerrar()
        return animales

