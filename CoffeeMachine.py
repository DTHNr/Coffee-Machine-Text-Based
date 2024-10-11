import Menu
import CoffeeLogo

quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01

money = 0

def coffee_machine():
    global money
    CoffeeLogo
    print("Order your coffee")
    
    order = str(input("What would you like?: "))
    if order == "off":
        exit()

    elif order == "report":
        for ingredient, ingredient_amount in Menu.resources.items():
            print(f"{ingredient}: {ingredient_amount}")
        print(f"Money: ${money:.2f}")
        coffee_machine()

    elif order in Menu.menu:
        ordered_product = Menu.menu[order]["ingredients"]
        
        sufficent_resources = True

        for ingredient, ingredient_amount in ordered_product.items():
            if ingredient_amount > Menu.resources.get(ingredient, ingredient_amount):
                print("Sorry there is not enough resources.")
                sufficent_resources = False
                break

        if sufficent_resources:
            input_quarter = int(input("How many quarter?: ")) * quarter
            input_dime = int(input("How many dime?: ")) * dime
            input_nickle = int(input("How many nickle?: ")) * nickle
            input_penny = int(input("How many penny?: ")) * penny

        total_payment = input_quarter + input_dime + input_nickle + input_penny

        if total_payment < Menu.menu[order]["cost"]:
            print("Sorry, Not enough payment!\nMoney Refunded")

        else:
            change = total_payment - Menu.menu[order]["cost"]
            print(f"You have a total change of: ${change:.2f}")
        
        for ingredient, ingredient_amount in ordered_product.items():
            Menu.resources[ingredient] -= ingredient_amount
        
        money += Menu.menu[order]["cost"]

        print(f"Here is your {order}, please enjoy!")
        
        coffee_machine()
        


        

        

            


    
        
coffee_machine()