from ClassPlanAhorro import PlanAhorro
import csv

class lista:
    __lista=[]
    def __init__(self):
        self.__lista = []

    def testlista(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            cod= int(fila[0])
            modelo = fila[1]
            version = fila[2]
            valor = int(fila[3])
            plan = PlanAhorro(cod, modelo, version, valor)
            self.__lista.append(plan)
        archivo.close()

    def __str__(self):
        s = ""
        for plan in self.__lista:
            s += str(plan) + '\n'
        return s

    def actualizar(self):
        for plan in self.__lista:
            print(plan)
            nuevo_valor = float(input('Ingrese nuevo valor para modificarlo en el plan: '))
            plan.actualizar_valor(nuevo_valor)

    def mostrar_plan_cuota_inf(self, valor):
        for plan in self.__lista:
            if plan.getvalor() == valor and plan.valor_cuota()<valor:
                print(f"Valor de la cuota: {plan.valor_cuota():.2f}")
                print(plan)
            elif plan.getvalor() == valor and plan.valor_cuota()>valor:
                print("El valor de la cuota es inferior al valor dado")

    def modificar_cuotas_licitar(self, cod_plan, nuevas_cuotas):
        for plan in self.__lista:
            if plan.get_cod() == cod_plan:
                plan.set_cant_cuotas_licitar(nuevas_cuotas)
                print("Cantidad de cuotas para licitar actualizada.")
                

    def mostrar(self):
        for plan in self.__lista:
            print(plan)