class PlanAhorro:
    __Cant_cuotas_plan = 60
    __Cant_cuotas_licitar = 10
    
    def __init__(self, cod=0, modelo='', version='', valor=0.0):
        self.__codPlan = cod
        self.__modelo = modelo
        self.__Version = version
        self.__valor = valor

    def __str__(self):
        return f'cod: {self.__codPlan}, Modelo: {self.__modelo}, Version: {self.__Version}, valor: {self.__valor}'

    def actualizar_valor(self, nuevo_valor):
        self.__valor = nuevo_valor

    def valor_cuota(self):
        return (float(self.__valor) / 60) + float(self.__valor) * 0.10
    
    def getvalor(self):
        return self.__valor

    @classmethod
    def monto_licitacion(cls, importe_cuota):
        return cls.__Cant_cuotas_licitar * importe_cuota

    def get_cod(self):
        return self.__codPlan
    
    def set_cant_cuotas_licitar(cls, nuevas_cuotas):
        cls.__Cant_cuotas_licitar = nuevas_cuotas
        return cls.__Cant_cuotas_licitar
