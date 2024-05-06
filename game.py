import random
class Game:
    def __init__(self ,unit_type , unit_name):
        self.unit_type = ""
        self.unit_name = unit_name
        self.hp = 100
        self.ak = 0
        self.df = 0
        self.exp = 0
        self.rk = 1
        self.ability = ""
        self.damage = 0
        if unit_type == "W":
            self.warrior()
            
        elif unit_type == "T":
            self.tank()

        elif unit_type == "S":
            self.sorcerer()

    def warrior(self):
        self.unit_type = "Warrior"
        self.ak = random.randint(5, 20)
        self.df = random.randint(1, 10)

    def tank(self):
        self.unit_type = "Tank"
        self.ak = random.randint(1, 10)
        self.df = random.randint(5, 15)

    def sorcerer(self):
        self.unit_type = "Sorcerer"
        self.ak = random.randint(1,5)
        self.df = random.randint(1,10)
        self.ability = "Special: Reduce Enemy [def, Exp] on attack!"
    
    def attack(self, target):
        if self.unit_type == "Sorcerer":
            self.damage = self.ak - target.df + random.randint(-5, 10)
            
            if self.damage <= 0:
                self.damage = 0
                target.hp -= self.damage
                target.df -= random.randint(1,3)

                print(f"[Game Message]{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} Not even a scratch!!!!\nBut {self.unit_name} sealed {target.unit_name} with Holy magic and his stats is reduced!", end = " ")
                return (f"{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} Not even a scratch!!!!\nBut {self.unit_name} sealed {target.unit_name} with Holy magic and his stats is reduced!")
            elif self.damage <= 5:
                target.hp -= self.damage
                target.df -= random.randint(1,3)
                print(f"[Game Message]{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} That was weak!!!!\n{self.unit_name} sealed {target.unit_name} with Holy magic and his stats is reduced!", end = " ")
                return (f"{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} That was weak!!!!\n{self.unit_name} sealed {target.unit_name} with Holy magic and his stats is reduced!")
            elif self.damage <=20 and self.damage >= 6:
                target.hp -= self.damage
                target.df -= random.randint(1,3)
                print(f"[Game Message]{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} Impressive!!!!\n{self.unit_name} sealed {target.unit_name} with Holy magic and his defense is reduced!", end = " ")
                return (f"{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} Impressive!!!!\n{self.unit_name} sealed {target.unit_name} with Holy magic and his stats is reduced!")
            else:
                target.hp -= self.damage
                target.df -= random.randint(1,3)
                print(f"[Game Message]{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} That was brutal!!!!\n{self.unit_name} sealed {target.unit_name} with Holy magic and his stats is reduced!", end = " ")
                return (f"{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} That was brutal!!!!\n{self.unit_name} sealed {target.unit_name} with Holy magic and his stats is reduced!")
            
            
        
        else:
            self.damage = (self.ak - target.df + random.randint(-5, 10))
            if self.damage <= 0:
                self.damage = 0
                target.hp -= self.damage
                print(f"[Game Message]{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} Not even a scratch!!!!", end = " ")
                return (f"{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} Not even a scratch!!!!")
            elif self.damage <= 5:
                target.hp -= self.damage
                print(f"[Game Message]{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} That was weak!!!!", end = " ")
                return (f"{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} That was weak!!!!")
            elif self.damage <=20 and self.damage >= 6:
                target.hp -= self.damage
                print(f"[Game Message]{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} Impressive!!!!", end = " ")
                return (f"{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} Impressive!!!!")
            else:
                target.hp -= self.damage
                print(f"[Game Message]{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} That was brutal!!!!", end = " ")
                return (f"{self.unit_name} Dealed {self.damage:.2f} Dmg to {target.unit_name} That was brutal!!!!")
            
    def hp_out(self, listt, target):
        if target.hp <= 0:
            listt.remove(target)
            print(f"[Game Message]{target.unit_name} is dead!!\n")
            return (f"{target.unit_name} is dead!!\n")
        else:
            return " "

    def exp_gain(self, attacker, target):
        attacker.exp += attacker.damage
        if attacker.exp < 100:
            print(f"{attacker.unit_name} now has {attacker.exp:.2f} Experience Point!!!\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            
        if attacker.damage > 10:
            target.exp += (target.df * 1.2) # 20%
            if target.exp < 100:
                print(f"[Game Message]{target.unit_name} now has {target.exp:.2f} Experience Point!!!\n++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                return (f"{attacker.unit_name} now has {attacker.exp:.2f} Experience Point!!!\n{target.unit_name} now has {target.exp:.2f} Experience Point!!!")
        elif attacker.damage > 0 and attacker.damage <= 10:
            target.exp += target.df
            if target.exp < 100:
                print(f"[Game Message]{target.unit_name} now has {target.exp:.2f} Experience Point!!!\n++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                return (f"{target.unit_name} now has {target.exp:.2f} Experience Point!!!")
            
        elif attacker.damage <= 0:
            target.exp += (target.df * 1.5) # 50 %
            if target.exp < 100:
                print(f"[Game Message]{target.unit_name} now has {target.exp:.2f} Experience Point!!!\n++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                return (f"{target.unit_name} now has {target.exp:.2f} Experience Point!!!")
        
        
    def rank(self, attacker, target):
        if attacker.exp >= 100:
            attacker.exp -= 100
            attacker.hp = 100 #######
            attacker.ak += 5
            attacker.rk += 1
            print(f"[Game Message]{attacker.unit_name} is now Rank {attacker.rk}. Health is fully restored and +5 atk point!!")
            
        if target.exp >= 100:
            target.exp -= 100
            target.hp = 100 #######
            target.ak += 5
            target.rk += 1
            print(f"[Game Message]{target.unit_name} is now Rank {target.rk}. Health is fully restored and +5 atk point!!")
        return (f"{attacker.unit_name} is now Rank {attacker.rk}!!\n{target.unit_name} is now Rank {target.rk}!!")
    
    def ai_aim(self):
        return self.hp
        
    def __str__(self):
        text = f"({self.unit_type})Name: " + self.unit_name 
        text += "| Hp: " + str(self.hp) 
        text += "| Ak: " + str(self.ak) 
        text += "| Df: " + str(self.df)
        text += "| Rank: "+ str(self.rk)
        text += "| " + str(self.ability) + "\n"
        return text

class Game2:
    def __init__(self ,unit_type , unit_name):
        self.unit_type = ""
        self.unit_name = unit_name
        self.hp = 100
        self.ak = 0
        self.df = 0
        self.exp = 0
        self.rk = 1
        self.ability = ""
        self.damage = 0

kaung = Game ("W", "KMS")
print(kaung)






    


