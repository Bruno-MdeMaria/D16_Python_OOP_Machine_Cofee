from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

dinheiro_maquina = MoneyMachine()
#dinheiro_maquina.report()   TEMP
coffee_maker = CoffeeMaker()
#coffee_maker.report()   TEMP
menu = Menu()

maquina_on = True

while maquina_on:
    opcoes = menu.get_items()
    escolha = input(f"Qual bebida? {opcoes}:")
    if escolha == "off":
        maquina_on = False
    elif escolha == "report":
        dinheiro_maquina.report()
        coffee_maker.report()
    else:
        bebida = menu.find_drink(escolha)
        #print(bebida) #TEMP
        recurso = coffee_maker.is_resource_sufficient(bebida)
        #print(recurso) #TEMP
        if recurso == True:
            if dinheiro_maquina.make_payment(bebida.cost):    #SE FOR VERDADEIRO TRUE O RESULTADO DA ACÃO DE VERIFCAR DINHEIRO SUFICIENTE:
                coffee_maker.make_coffee(bebida)

#OUTRA FORMA D SIMPLIFCAR O CÓDIGO É JUNTANDO AS DUAS VERIFICACOES IF:

#   if recurso = coffee_maker.is_resource_sufficient(bebida) and if dinheiro_maquina.make_payment(bebida.cost):
         # coffee_maker.make_coffee(bebida)

            
    

    

#input("Qual bebida? (espresso/latte/cappuccino): ")

