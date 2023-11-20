
class Animal:
    def __init__(self,codigo:str,raza:str,patas:int,peso:float, id:int=0):
        self.__codigo = codigo 
        self.__raza = raza
        self.__patas = patas
        self.__peso = peso
        self.__id = id

    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self,codigo):
        self.__codigo= codigo

    def get_id(self):
        return self.__id
    
    def set_id(self,id):
        self.__id= id

    def get_raza(self):
        return self.__raza
    
    def get_patas(self):
        return self.__patas

    def get_peso(self):
        return self.__peso
    
    def set_raza(self,raza):
        self.__raza = raza

    def set_patas(self,patas):
        self.__patas = patas

    def set_peso(self,peso):
        self.__peso = peso
    
    def __str__(self):
        t = f"ID: {self.__id}"
        t += f"\nCodigo: {self.__codigo}"
        t += f"\nRaza: {self.__raza}"
        t += f"\nPatas: {self.__patas}"
        t += f"\nPeso: {self.__peso}"
        return t