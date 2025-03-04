from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


on_off = 'on'
continue_operation = True

while on_off == 'on':
    while True:
        coffee_type = input("What would you like? (espresso/latte/cappuccino/): ")
        if coffee_type == 'off':
            on_off = 'off'
            break
        elif coffee_type == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            if coffee_type == 'espresso' or coffee_type == 'latte' or coffee_type == 'cappuccino':
                menu_item = menu.find_drink(coffee_type)
                has_resources = coffee_maker.is_resource_sufficient(menu_item)
                if has_resources is False:
                    continue_operation = False

                else:
                    has_enough_money = money_machine.make_payment(menu_item.cost)
                    if has_enough_money is True and has_resources is True:
                        coffee_maker.make_coffee(menu_item)
