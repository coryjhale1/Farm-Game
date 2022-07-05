import os
import time
import random


class Farmer:

    def __init__(self, input_name, input_money, owns_land):
        self.name = input_name
        self.money = input_money
        self.seeds = [[watermelon, 0], [carrot, 0], [lettuce, 0]]
        self.crops = []
        self.land = 0
        self.landOwner = owns_land

# A descriptive function for the farmer class
    def __repr__(self):
        os.system("clear")

        if (self.seeds[0][1] + self.seeds[1][1] + self.seeds[2][1]) > 1 or (self.seeds[0][1] + self.seeds[1][1] + self.seeds[2][1]) == 0:
            print("Farmer {name} has {acres} acres of land, {money} dollar, {seed_number} seeds, and {veg_number} veggies.".format(name=self.name, acres = self.land, money= self.money, seed_number = (self.seeds[0][1] + self.seeds[1][1] + self.seeds[2][1]),  veg_number = len(self.crops)))

        else:
            print("Farmer {name} has {acres} acres of land, {money} dollar, {seed_number} seed, and {veg_number} veggies.".format(name=self.name, acres = self.land, money= self.money, seed_number = (self.seeds[0][1] + self.seeds[1][1] + self.seeds[2][1]),  veg_number = len(self.crops)))


        any_key = input("Press enter to continue ")
        if any_key == "":
            return beginning()
        else:
            return beginning()
        return beginning()

# This function defines the land buying process
    def trade_land(self):

        os.system("clear")
        buy = input("\nWould you like to buy land? (Y/N) ")

        if (buy.upper() == "Y"):

            if (self.landOwner):
                extra_land = int(input("You already own {acres} acres. How much more would you like? ".format(acres = self.land)))
                land_cost = extra_land * 2
                if (extra_land == 0):
                    print("You have not bought anything.")
                    time.sleep(2)
                    return beginning()
                elif((extra_land) > 0):
                    if land_cost <= self.money:
                        self.land += extra_land
                        self.money -= land_cost
                        self.landOwner = True
                        print("You now have {acres} acres and ${money}!".format(acres = self.land, money = self.money))
                        time.sleep(2)
                        return beginning
                else:
                    print("You must own land to sell it.")
                    time.sleep(2)
                    return self.trade_land
                
                
            else:
                first_buy = int(input("Congrats! This is your first piece of land. Land costs $20/acre. You have ${money}. How much would you like to purchase? ".format(money = self.money)))
                land_cost = first_buy * 20
                if (first_buy == 0):
                    print("You have not bought anything.")
                    time.sleep(2)
                    return beginning()
                elif((first_buy) > 0):
                    if land_cost <= self.money:
                        self.land += first_buy
                        self.money -= land_cost
                        self.landOwner += True
                        print("You now have {acres} acres and ${money}!".format(acres = self.land, money = self.money))
                        time.sleep(2)
                        return beginning()
                    else:
                        print("You do not have enough money.")
                        time.sleep(2)
                        return self.trade_land
                else:
                    print("You must own land to sell it.")
                    time.sleep(2)
                    return self.trade_land
        elif (buy.upper() == "N"):
            not_buy = input("Would you like to sell land? (Y/N) ")
            if (not_buy.upper() == "Y"):
                if (self.landOwner):
                    sell_land = int(input("How much would you like to sell? You have {acres} acres and ${money}. You will only make part of your money back (1$/acre). ".format(acres = self.land, money = self.money)))
                    if sell_land > self.land:
                        print("You do not have enough land to sell.")
                        time.sleep(2)
                        return self.trade_land
                    else:
                        self.land -= sell_land
                        self.money += sell_land
                        if self.land == 0:
                            self.landOwner = False
                        print("You now have {acres} acres and ${money}!".format(acres = self.land, money = self.money))
                        time.sleep(2)
                        return beginning()
                else:
                    print("You must have land to sell.")
                    time.sleep(2)
                    return self.trade_land()
            elif (not_buy.upper() == "N"):
                return beginning()
            else:
                print("Invalid response")
                time.sleep(2)
                return self.trade_land
        else:
             print("Invalid Response")
             time.sleep(2)
             return self.trade_land()

# This function will define buying seeds, where the farmer can buy his first seeds or any sets after his purchase assuming there is enough money in the money variable. It will check whether the farmer has any seeds and slightly change the prompt depending on the result.

    def buy_seed(self, seeds):

        #Gets the seed count for the seed input from the list
        os.system("clear")
        counted_seeds = self.seeds.count(seeds)
        print(counted_seeds)
        seed_count = self.seeds[counted_seeds][1]
        

        if (seed_count) == 0:
            how_many_input = input("Congrats! These are your first seeds! How many would you like? ").strip()
            if (how_many_input.isnumeric()):
                
                how_many = int(how_many_input)
                if how_many == 0:
                    print("You have not bought anything")
                    return beginning()
                else:
                    # checks for price of seeds
                    if (self.money < seeds.cost * how_many):
                        print("You do not have enough money")
                        return beginning()

                    # confirms purchase
                    price_confirmation = input("Ok! That will be ${price}. Do you want to buy? (Y/N)".format(price = seeds.cost * how_many))

                    # checks input for confirmation and adds seeds into farmers stock and subtracts money spent from wallet total amount
                    if (price_confirmation.upper().strip() == "Y" or "YES"):
                        self.money -= (seeds.cost * how_many)
                        self.seeds[counted_seeds][1] += how_many
                        seeds.stock -= how_many
                        print("You have bought {number} seeds.".format(number = how_many))
                        # print("You now have {number} {type} seeds and ${money}".format(number = self.seeds))
                        time.sleep(2)
                    elif (price_confirmation.upper() == "NO" or "N"):
                        return self.buy_seeds(seeds)
                    else:
                        print("Not a valid answer")
                        return self.buy_seeds(seeds)
            else:
                print("Invalid response")
                time.sleep(2)
                return self.buy_seed()

        else:

            how_many_input = input("How many would you like? ")
            if (how_many_input.isnumeric()):
                
                how_many = int(how_many_input)
                if how_many == 0:
                    print("You have not bought anything")
                    return beginning()
                else:
                    # checks for price of seeds
                    if (self.money < seeds.cost * how_many):
                        print("You do not have enough money")
                        return beginning()

                    # confirms purchase
                    price_confirmation = input("Ok! That will be ${price}. Do you want to buy? (Y/N)".format(price = seeds.cost * how_many))

                    # checks input for confirmation and adds seeds into farmers stock and subtracts money spent from wallet total amount
                    if (price_confirmation.upper().strip() == "Y" or "YES"):
                        self.money -= (seeds.cost * how_many)
                        self.seeds[counted_seeds][1] += how_many
                        seeds.stock -= how_many
                        print("You have bought seeds.")
                        # print("You now have {number} {type} seeds and ${money}".format(number = self.seeds))
                        time.sleep(2)
                    elif (price_confirmation.upper() == "NO" or "N"):
                        return self.buy_seeds(seeds)
                    else:
                        print("Not a valid answer")
                        return self.buy_seeds(seeds)
            else:
                print("Invalid response")
                time.sleep(2)
                return self.buy_seed()  


# Defines the planting function
    def plant_seeds(self, seeds):

        os.system("clear")
        counted_seeds = self.seeds.count(seeds)
        print(counted_seeds)
        seed_count = self.seeds[counted_seeds][1]

        # Error Message
        if ((self.seeds[0][1] + self.seeds[1][1] + self.seeds[2][1]) <= 0):
            print("You must first buy seeds.")
            return beginning()

        # Main Track
        else:
            if self.landOwner == True:

                how_many_input = input("How many would you like to plant? ")
                if (how_many_input.isnumeric()):

                    how_many = int(how_many_input)
                    if how_many > seeds.acre * self.land:
                        print("That many seeds wont fit on your land. Check carrying capacity and try again.")
                        time.sleep(2)
                        return beginning()

                    elif how_many <= 0:
                        print("You have not planted anything")
                        time.sleep(2)
                        return beginning()
                    
                    else:
                        seed_count -= how_many
                        seeds.grow()
                        print("You now have {number} {crop}".format(number = how_many, crop = self.seed[counted_seeds]))
                        time.sleep(2)
                        harvest = input("Time to harvest! Press any key to continue.")
                        if harvest == "":
                            seeds.harvest(self)
                        else:
                            seeds.harvest(self)
                    

                # Error Message
                else:
                    print("Invalid response")
                    time.sleep(2)
                    return self.plant_seeds()  

            # Error Message
            else:
                print("You must own land to plant seeds")
                time.sleep(2)
                return beginning()


class Seeds:
    def __init__(self, input_name, input_cost, stock_total, grow_time, per_acre, in_stock = True, growing = True):
        self.name = input_name
        self.cost = input_cost
        self.time = grow_time
        self.stock = stock_total
        self.acre = per_acre

    def grow (self, farmer):
        i = 0
        print("Seeds are growing!")
        while i < self.time:
            print(".")
            time.sleep(1)
            i += 1

    def harvest (self, farmer):
        rand = random.randint(0, 10) 
       
        

        
    



class Store:
    def restock_store(seeds):
        pass



# Seed Classes
watermelon = Seeds("watermelon", 3, 100, 20, 15)
carrot = Seeds("carrot", 1, 100, 10, 25)
lettuce = Seeds("lettuce", 2, 100, 15, 20)

# Start Screen setup
def beginning():

    os.system("clear")
    print(
        """
▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄   ▄▄ 
█       █      █   ▄  █ █  █▄█  █
█    ▄▄▄█  ▄   █  █ █ █ █       █
█   █▄▄▄█ █▄█  █   █▄▄█▄█       █
█    ▄▄▄█      █    ▄▄  █       █
█   █   █  ▄   █   █  █ █ ██▄██ █
█▄▄▄█   █▄█ █▄▄█▄▄▄█  █▄█▄█   █▄█

        """
    )
    start_screen = int(input("\nWhat would like to do? \n \nEnter:\n1 for TRADE LAND\n2 for BUY SEEDS\n3 for PLANT CROP\n4 for HARVEST CROP\n5 for SELL CROP\n6 for CHECK FARMER STATUS\n7 for QUIT GAME\n\n"))

    # Buy/Sell land
    if start_screen == 1:
        farmer.trade_land()
    
    # Buy Seeds
    if start_screen == 2:
        os.system("clear")
        print("""
 ____________________________________________________ 
|  ________________________________________________  |
| | _________________SEED PRICES___________________| |
                    
           SEED    |   PRICE   |     STOCK
        WATERMELON |    $3     |      {watermelon}
          CARROT   |    $1     |      {carrot}
         LETTUCE   |    $2     |      {lettuce}
| |________________________________________________| |
|____________________________________________________|
        """.format(watermelon = watermelon.stock, carrot = carrot.stock, lettuce = lettuce.stock))

        seed_choice = input("What kind of seeds would you like?\n\nEnter:\n{seed_1}\n{seed_2}\n{seed_3}\n\n".format(seed_1 = watermelon.name, seed_2 = carrot.name, seed_3 = lettuce.name))

        if seed_choice.lower().strip() == watermelon.name or carrot.name or lettuce.name:
            farmer.buy_seed(globals()[seed_choice.lower().strip()])
        else:
            print("Invalid response")
            time.sleep(2)
            return beginning()

    # Plant crops
    if start_screen == 3:
        seed_choice = input("What kind of seeds would you like to plant?\n\nEnter:\n{seed_1}\n{seed_2}\n{seed_3}\n\n".format(seed_1 = watermelon.name, seed_2 = carrot.name, seed_3 = lettuce.name))

        if seed_choice.lower().strip() == watermelon.name or carrot.name or lettuce.name:
            farmer.plant_seeds(globals()[seed_choice.lower().strip()])
            
        else:
            print("Invalid response")
            time.sleep(2)
            return beginning()

    # Harvest crops 
    if start_screen == 4:
        print("4")
        time.sleep(2)
        return beginning()

    # Sell Crops
    if start_screen == 5:
        print(farmer)
        return beginning()

    # Farmer status
    if start_screen == 6:
        print(farmer)
        return beginning()

    # Quit game
    if start_screen == 7:
        os.system("clear")
        quit()
    
    else:
        print("Not valid entry")
    os.system("clear")
    return beginning()

# GAME STARTUP

# os.terminal_size((80,80))

os.system("clear")

farmer_input = input("Howdy farmer! What is your name? ")
farmer_name = farmer_input.title().strip()
farmer = Farmer(farmer_name, 100, False)

beginning()
