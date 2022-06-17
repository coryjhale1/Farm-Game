import os
import time


class Farmer:

    def __init__(self, input_name, input_money, planted_seeds = 0, owns_land = False):
        self.name = input_name
        self.money = input_money
        self.seeds = []
        self.crops = []
        self.land = 0
        self.landOwner = owns_land
        self.planted = planted_seeds
        self.ownsLand = owns_land
  
    def __repr__(self):
        os.system("clear")
        print("Farmer {name} has {acres} acres of land, {money} dollar, {seed_number} kinds of seeds, and {veg_number} veggies.".format(name=self.name, acres = self.land, money= self.money, seed_number = len(self.seeds),  veg_number = len(self.crops)))
        any_key = input("Enter any key to continue ")
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
                first_buy = int(input("Congrats! This is your first piece of land. Land costs $2/acre. You have ${money}. How much would you like to purchase? ".format(money = self.money)))
                land_cost = first_buy * 2
                if (first_buy == 0):
                    print("You have not bought anything.")
                    time.sleep(2)
                    return beginning()
                elif((first_buy) > 0):
                    if land_cost <= self.money:
                        self.land += first_buy
                        self.money -= land_cost
                        self.landOwner = True
                        print("You now have {acres} acres and ${money}!".format(acres = self.land, money = self.money))
                        time.sleep(2)
                        return beginning
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
        os.system("clear")
        if (len(self.seeds) == 0):
            how_many = input("Congrats! These are your first seeds! How many would you like? ")

            # checks for price of seeds
            if (self.money < seeds.cost * how_many):
                print("You do not have enough money")
                return beginning()

            # confirms purchase
            price_confirmation = input("Ok! That will be {price}. Do you want to buy? ".format(price = seeds.cost * how_many))

            # checks input for confirmation and adds seeds into farmers stock and subtracts money spent from wallet total amount
            if (price_confirmation.upper() == "YES"):
                self.money -= (seeds.cost * how_many)
                self.seeds += zip(seeds.name, how_many)
                seeds.stock -= how_many
                print("you have bought seeds.")
                # print("You now have {number} {type} seeds and ${money}".format(number = self.seeds))
                time.sleep(2)
            elif (price_confirmation.upper() == "No"):
                return self.buy_seeds()
            else:
                print("Not a valid answer")
                return self.buy_seeds()
        else:

            how_many = input("How many would you like? ")

            # checks for price of seeds
            if (self.money < seeds.price * how_many):
                print("You do not have enough money")
                return self.buy_seed()

            # confirms purchase
            price_confirmation = input("Ok! That will be {price}. Do you want to buy? ".format(price = seeds.cost * how_many))

            # checks input for confirmation and adds seeds into farmers stock and subtracts money spent from wallet total amount
            if (price_confirmation.upper() == "YES"):
                self.money -= (seeds.cost * how_many)
                self.seeds = {key: value for key, value in zip(first_seeds_kind, how_many)}
            elif (price_confirmation.upper() == "No"):
                return
            else:
                print("Not a valid answer")
                return  

    def plant_seeds(self, seeds):
        if (len(self.seeds == 0)):
            print("You must first buy seeds.")
            return 
        else:
            if (self.seeds == 0):
                print("You do not have any of that seed")
                return 
            else:
                self.seeds -=  how_many
                print("Seeds planted!")
                return 
            return seed_option


class Seeds:

  def __init__(self, input_name, input_cost, input_growth, stock_total, in_stock = True):
    self.name = input_name
    self.cost = input_cost
    self.growth = input_growth
    self.stock = stock_total


# main gameplay setup
watermelon = Seeds("watermelon", 3, 20, 100)
carrot = Seeds("carrot", 1, 5, 100)
lettuce = Seeds("lettuce", 2, 3, 100)

def beginning():
    os.system("clear")
    start_screen = int(input("\nWhat would like to do? \n \nEnter:\n1 for TRADE LAND\n2 for BUY SEEDS\n3 for HARVEST CROP\n4 for SELL CROP\n5 for CHECK FARMER STATUS\n6 for QUIT GAME\n\n"))

    if start_screen == 1:
        # print("1")
        farmer.trade_land()
    
    if start_screen == 2:
        seed_choice = input("What kind of seeds would you like?\n\nEnter:\n1 for {seed_1}\n2 for {seed_2}\n3 for {seed_3}\n ".format(seed_1 = watermelon.name, seed_2 = carrot.name, seed_3 = lettuce.name))
        farmer.buy_seed(seed_choice)

    if start_screen == 3:
        print("1")
     
    if start_screen == 4:
        print("1")

    if start_screen == 5:
        print(farmer)
        return beginning
        
    if start_screen == 6:
        os.system("clear")
        quit()
    
    else:
        print("Not valid entry")
    os.system("clear")
    return beginning()

# Game startup2

# os.terminal_size((80,80))

os.system("clear")

farmer_input = input("Hello farmer! What is your name? ")
farmer_name = farmer_input.title().strip()
farmer = Farmer(farmer_name, 100)

beginning()
