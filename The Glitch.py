"""Credit333s
Y e   Y i n t   A u n g   N a i n g 
 K a u n g   M y a t   S a n 
 K a u n g   N g w e   T o e 
 S w a m   H t e t   A u n g 
 L i n   T h i t   T h w e 
 S h o o n   P a   P a   H t e st"""
import random
import game
import time
#######
player_unit = []
enemy = []

#######
sec = time.time()
timenow = time.ctime(sec)
for i in timenow:
    if i == ":":
        x = timenow.replace(i, "-")
################################################################################################################################################################
def main():
    
    s_loop = 0
    j = "Welcome!!!!"
    print(*f"{j}")
    while s_loop == 0:## Game start Option
        print("1. Start Game.\n2. Support Developers.\n3. Credits.\n4. About Unit Types.\n5. Quit.")
        ask = input("-->")
        if ask == "1":
            gamefunction()    
        elif ask == "2":
            print("Thanks for consideration to support us!!")
        elif ask == "3":
            print(*"Thanks for Playing Our Game (- _ -)\nDeveloped by\nYe Yint Aung Naing\nKaung Myat San\nKaung Ngwe Toe\nSwam Htet Aung\nLin Thit Thwe\nShoon Pa Pa Htet\n")
        elif ask == "4":
            print("Warriors usually have high attack points[between 5 and 20] but have lower defense points[between 1 and 10]\nTanks usually have high defense point[between 5 and 15]but have lower attack points\n", end = "")
            print("Sorcerers are weak in both attack and defense points but they have special ability\nThey reduce defense of enemy, when out of defense they reduce exp instead.\n")
        elif ask =="5":
            break
      
            
################################################################################################################################################################
def gamefunction():
    #######Storyline

    filename = open(f"GameLog {x}.txt", "w")# GameLog write

    print("\t\t\tOne night, we, 6 members of group[4], were developing our game......\n", end = "")
    print("\t\tSuddenly the game was glitched all of us were sucked by unknown force into the game....\n", end = "")
    print("\t\t\tWe all lost our conciousness and became NPC........\n", end = "")
    print("\t\t\t\tFortunately the game file was sent to you\n", end = "")
    print("\t\t\tThe only way to free us is to defeat NPC form of us!\n", end = "")
    print("\t\t\t\t\tOur lives are in your hand!!!\n ")
    Game_over = False
    unitclone = ["W", "T"]
    
    unit_namelist = []
    anger = 0
################################################################################################################################################################
    while len(player_unit) < 3:
        unit_type = input("Choose your champion..[Warrior(W) or Tank(T)] or Sorcerer(S). or Return to main menu(R). \n\t->").upper()
        if unit_type == "W":
            while True:
                unit_name = input("Give your champion a name. \n\t->")
                if unit_name not in unit_namelist:
                    unit_namelist.append(unit_name)
                    troop = game.Game(unit_type, unit_name)
                    player_unit.append(troop)
                    break
                else:
                    print("\tTroops can't have Same name!")
                    
        elif unit_type == "T":
            while True:
                unit_name = input("Give your champion a name. \n\t->")
                if unit_name not in unit_namelist:
                    unit_namelist.append(unit_name)
                    troop = game.Game(unit_type, unit_name)
                    player_unit.append(troop)
                    break
                else:
                    print("\nTroops can't have Same name!")

        elif unit_type == "S":
            while True:
                unit_name = input("Give your champion a name. \n\t->")
                if unit_name not in unit_namelist:
                    unit_namelist.append(unit_name)
                    troop = game.Game(unit_type, unit_name)
                    player_unit.append(troop)
                    break
                else:
                    print("\nTroops can't have Same name!")
        elif unit_type == "R":
            while len(player_unit) != 0:
                player_unit.pop(0)
            return main()
            
        else:
            print("Invalid!")
            if anger == 1:
                print("Choose(W) or (T) or (S) Only!!!!")
            elif anger == 3:
                print("Cmon man! Choose from(W) or (T) or (S)")
            elif anger == 5:
                print("You are banned!!!!")
                while len(player_unit) != 0:
                    player_unit.pop(0)
                    
                return main() 
            anger += 1
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::\nYour Champions are here!!!!!!")
    filename.write("Your Champions are here!!!!!!\n\n")#GameLog
    for index in range(len(player_unit)):
        print(player_unit[index])
        filename.write(str(player_unit[index])+ "\n\n")#GameLog
###################################################################   
    print("------------------------------------------------------")
    print('Generating creepy Ai......\n')
################################################################################################################################################################
    AI_names = ["BotLin", "BotYeyint", "BotNgwe", "BotKaung", "BotShoon", "BotSwan"]
    
    while len(enemy) != 3 :
        name = random.choice(AI_names)
        AI_names.remove(name)
        ai = game.Game(random.choice(unitclone), name ) #randomized w or tank for AI
        enemy.append(ai)
    fixed = game.Game("S", "BotBoss" )
    enemy[random.randint(0,2)] = fixed #atleast one socerer in AI team
    for index in range(len(enemy)):
        print(enemy[index])
        filename.write(str(enemy[index])+ "\n\n")#GameLog
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    while True:
        k = input("Intimidating voices: Surrender or dieeee!!!!Hahahahaa...! Wanna Quit?[Y/N]")
        if k.lower() == "n":
            break
        elif k.lower() == "y":
            Game_over = True
            while len(player_unit) != 0:
                player_unit.pop(0)
            print("Oh hellll noo!!!I'm out!\nRedirecting to main menu........")
            filename.write("Oh hellll noo!!!I'm out!"+ "\n\n")#GameLog
            filename.close()
            break
        else:
            print("Just choose yes or no[Y/N]")
    
################################################################################################################################################################
    rounds = 1
    loop = 0
    loop1 = 0


    while not Game_over:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"|||<<<<<<<<<<<<<<<<<<<<< Round{rounds} >>>>>>>>>>>>>>>>>>>>>|||")
        if rounds % 2 == 1: #odd
            
            while loop == 0:

                attunit_ipt = input("Choose ur unit [1, 2, 3] : ")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                
                if attunit_ipt.isdigit() == True:
                    attunit = (int(attunit_ipt))-1              
                    if attunit in range(len(player_unit)) :
                        while loop1 == 0:
                            target_ipt = input("Choose ur target unit [1, 2, 3] : ")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                            if target_ipt.isdigit() == True:
                                target = (int(target_ipt))-1
                                if target in range(len(enemy)):
                                    #player_unit[attunit].attack(enemy[target])# Player attack to AI
                                    filename.write(str(player_unit[attunit].attack(enemy[target]))+ "\n\n")# GameLog
                                    
                                    filename.write(str(troop.exp_gain(player_unit[attunit], enemy[target]))+ "\n\n")# Exp method #GameLog

                                    filename.write(str(troop.rank(player_unit[attunit], enemy[target]))+ "\n\n")# Rank method ##GameLog
                                    loop1 = 1
                                else:
                                    print("Choose Remaining Unit!")
                            else:   
                                print("Invalid:")
                        loop = 1
                    else:
                        print("Choose remaining unit!")
                else:
                    print("Invalid:")
            
            for i in enemy:
                filename.write(str(troop.hp_out(enemy, i))+ "\n\n")
            for j in range(len(enemy)):
                print(enemy[j])
            
            rounds += 1
################################################################################################################################################################           
        else:###Ai round
            loopai = 0
            if loopai == 0:
                for a in player_unit:
                    if a.ai_aim() <= 80:
                        filename.write(str(random.choice(enemy).attack(a))+ "\n\n") ##Ai eyes on first hp lower than 80
                        filename.write(str(troop.exp_gain(random.choice(enemy), a))+ "\n\n")#GameLog
                        filename.write(str(troop.rank(random.choice(enemy), a))+ "\n\n")#GameLog
                        loopai = 1
                        break
                        

            if loopai == 0:
                aia = random.choice(enemy)
                ait = random.choice(player_unit)
                filename.write(str(aia.attack(ait))+ "\n\n")#GameLog
                filename.write(str(troop.exp_gain(aia, ait))+ "\n\n")#GameLog
                filename.write(str(troop.rank(aia, ait))+ "\n\n")#GameLog
                    
 
            for i in player_unit:
                
                filename.write(str(troop.hp_out(player_unit, i))+ "\n\n")
            for j in range(len(player_unit)):
                print(player_unit[j])

            rounds += 1
            loop = 0
            loop1 = 0
################################################################################################################################################################
                
        if len(enemy) == 0:   # Enemy out of troop Player wins
            Game_over = True
            while len(player_unit) != 0:
                
                player_unit.pop(0)
            print("You Win! Thanks For Playing Our Game!!\nRedirecting to main menu...")
            filename.write("You Win! Thanks For Playing Our Game!!Redirecting to main menu..." + "\n\n")#GameLog
            s_loop = 0
        elif len(player_unit) == 0 : # Player out of troop Enemy wins
            Game_over = True
            while len(enemy) != 0:
                
                enemy.pop(0)
            print("You Lose!\nRedirecting to main menu... ")
            filename.write("You Lose! Redirecting to main menu... " + "\n\n")#GameLog
            s_loop = 0
################################################################################################################################################################
        while True:
            if rounds % 5 == 0: # Game option in every 5th Round
                print("Options")
                askk = input("1. Continue.\n2. Unit Info.\n3. Surrender.\n4. Credits.\n")
                if askk == "1":
                    break
                elif askk == "2":
                    for index in range(len(player_unit)):
                        print(player_unit[index])
                    for index in range(len(enemy)):
                        print(enemy[index])
                elif askk == "3":
                    Game_over = True
                    while len(player_unit) != 0:
                        player_unit.pop(0)
                    while len(enemy) != 0:
                        enemy.pop(0)
                    print("Redirecting to main menu... ")
                    filename.close()
                    break
                
                elif askk == "4":
                    print(*"Thanks for Playing Our Game (- _ -)\nDeveloped by\nYe Yint Aung Naing\nKaung Myat San\nKaung Ngwe Toe\nSwam Htet Aung\nLin Thit Thwe\nShoon Pa Pa Htet\n")

                
                else:
                    print("invalid")
            else:
                break
################################################################################################################################################################                    
                         
    filename.close()
main()
    
    
