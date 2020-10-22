#random module used for game dynamics like damage dealt
import random

#dictionaries to allocate character atributes by discipline
fighter_dict = {'attack_mod': 2, 'defend_mod': 1, 'escape_mod': 0.5}
theif_dict = {'attack_mod': 0.75, 'defend_mod': .075, 'escape_mod': 2}
knight_dict = {'attack_mod': 1, 'defend_mod': 2, 'escape_mod': .05}

class Discipline():
    def __init__(self, discipline):
        self.discipline_dict = {}
        self.assign_dict(discipline)
        
    def assign_dict(self, discipline):
        if discipline == "Fighter":
            self.discipline_dict = fighter_dict
            self.attack_mod = fighter_dict["attack_mod"]
            self.defend_mod = fighter_dict["defend_mod"]
            self.escape_mod = fighter_dict["escape_mod"]
        elif discipline == "Theif":
            self.discipline_dict = theif_dict
            self.attack_mod = theif_dict["attack_mod"]
            self.defend_mod = theif_dict["defend_mod"]
            self.escape_mod = theif_dict["escape_mod"]
            
        elif discipline == "Knight":
            self.discipline_dict = knight_dict
            self.attack_mod = knight_dict['attack_mod']
            self.defend_mod = knight_dict['defend_mod']
            self.escape_mod = knight_dict['escape_mod']
            
    def attack(self, attacked):
        if attacked.status == "dead" or self.status == "dead":
            print("From attack() - Attacking this character will only make your sword harder to clean because they are already dead! Choose another.")
        else:
            damage1 = random.randint(1,10)
            if self.name == player.name:
                print ("\nYour damage roll was: " + str(damage1))
            else:
                print("\n" + str(self.name) + "'s damage roll was: " + str(damage1))
            damage = (damage1 * self.attack_mod)
            print("With Attack Modifier, {} dealt {} {} points of damage.".format(self.name, attacked.name, damage))
            attacked.health -= damage
            if attacked.health < 0:
                attacked.health = 0
            print("{} now has {} health points\n---------".format(attacked.name, attacked.health))
            return attacked.health
    
        

class Character(Discipline):               
    def __init__(self, discipline, weakness):
        super().__init__(discipline)
        self.weakness = weakness
        self.xp = 0
        self.gold = 100
        self.level = 1
        self.health = 100
        self.status = "alive"
        if weakness == True:
            self.health = self.health / 2
        else:
            self.health = self.health    

            
class Human(Character):
    def __init__(self, name, discipline, gender = "Male", skin_color = "Black", weakness = False):
        super().__init__(discipline, weakness)
        self.name = name
        self.discipline = discipline
        self.gender = gender
        self.skin_color = skin_color
        self.max_age = 100

class Elf(Character):
    def __init__(self, name, discipline, gender = "Female", skin_color = "White", weakness = True):
        super().__init__(discipline, weakness)
        self.name = name
        self.gender = gender
        self.skin_color = skin_color
        self.max_age = 700
     
class Dwarf(Character):
    def __init__(self, name, discipline, gender = "Male", skin_color = "Grey", weakness = False):
        super().__init__(discipline, weakness)
        self.name = name
        self.gender = gender
        self.skin_color = skin_color
        self.max_age = 300
        
      
#aggregates multiple attribute dictionaries into one dictionary for use in print_status() function.
def create_stat_dict(instance):
    instance.status_dict = {"xp": instance.xp, "gold": instance.gold, "level": instance.level, "health": instance.health, "status": instance.status}
    copy_discipline_dict = instance.discipline_dict.copy()
    copy_discipline_dict.update(instance.status_dict)
    stat_dict = copy_discipline_dict
    return stat_dict

#prints current aggregated attributes for a character based on dictionary created above.
def print_status():
    legolas_dict = create_stat_dict(Legolas)
    gimly_dict = create_stat_dict(Gimly)
    aragorn_dict = create_stat_dict(Aragorn)
    print("Legolas Stats = " + str(legolas_dict))
    print("Gimly Stats = " + str(gimly_dict))
    print("Aragorn Stats = " + str(aragorn_dict))
    

    

#instantiate character instances for gameplay
Legolas = Elf('Legolas', "Theif", gender = "Male", weakness = True)
Gimly = Dwarf("Gimly", "Knight")
Aragorn = Human("Aragorn", "Fighter")
print("Character Stats\n------------------------------")
print_status()
print("\n---------------------------------")

#entry point for program
if __name__ == '__main__':
    player = input("Would you like to play as Aragorn, Gimly or Legolas?")
        
#player and attacked were resolving to strings instead of one of the
#congruently named instantiated classes above, so converted string to instance variable.
    while player != Aragorn and player != Legolas and player != Gimly:
        if player in ["Aragorn", "aragorn", "A", "a"]:
            player = Aragorn
        elif player in ["Legolas", "legolas", "L", "l"]:
            player = Legolas
        elif player in ["Gimly", "gimly", "G", "g"]:
            player = Gimly
        else:
            print("The name you entered is not valid.  Please try again and enter carefully.")
            player = input("Would you like to play as Aragorn, Gimly or Legolas?")
        
    
    def attack_input():
        a = input("Who would you like to attack? (Choose from Aragorn, Gimly or Legolas.)")
        return a
    attacked = attack_input()
    while attacked != Aragorn and attacked != Gimly and attacked != Legolas:
        if attacked in ["Aragorn", "aragorn", "A", "a"]:
            attacked = Aragorn
        elif attacked in ["Legolas", "legolas", "L", "l"]:
             attacked = Legolas
        elif attacked in ["Gimly", "gimly", "G", "g"]:
            attacked = Gimly
        else:
            print("You entered a name that doesn't belong to any of the people waiting to be attacked : )  Please try again more carefully.")
            attacked = input("Who would you like to attack? (Choose from Aragorn, Gimly or Legolas.)")
            
    player.attack(attacked)
    while attacked.health >= 0:
        attacked = input("Who would you like to attack? (Choose from 'a' for Aragorn, 'g' for Gimly or 'l' for Legolas.)")
        if attacked in ["Aragorn", "aragorn", "A", "a"]:
            attacked = Aragorn
        if attacked in ["Legolas", "legolas", "L", "l"]:
            attacked = Legolas
        if attacked in ["Gimly", "gimly", "G", "g"]:
            attacked = Gimly
#make attack on player specified in input statement at program entry point.
        player.attack(attacked)
        if attacked.status == "dead":
#            print("From 'Player.attack' - Attacking this character will only make your sword harder to clean "\
#                 "because they are already dead! Choose another.")
            print("test 1")
        if attacked.health <= 0:
            attacked.status = "dead"
            print("test 2")
            print("You have killed {}".format(attacked.name))
            print("test 3")
        attacked.attack(player)
        print("test 4")
        if player.health <= 0:
            player.status = "dead"
            print("You are dead.")
            break
        

        

    

    
    
    
    
















#old code to validate that attributes are being passed between classes correctly 
"""print("Legolas' Attack Modifier is: " + str(Legolas.attack_mod) + ", Defend Modifier is: " + str(Legolas.defend_mod) + ", Escape Modifier is: " + str(Legolas.escape_mod) + ", Health: " + str(Legolas.health))

Gimly = Dwarf("Gimly", "Knight")
print("Gimly's Attack Modifier is: " + str(Gimly.attack_mod) + "\nGimly's Health is: " + str(Gimly.health))
Aragorn = Human("Aragorn", "Fighter", skin_color = "White")
print(Gimly.attack_mod)
print(Aragorn.attack_mod)
print(Gimly.escape_mod)
print(Aragorn.discipline_dict['escape_mod'])"""
        
