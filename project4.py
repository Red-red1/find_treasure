print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')
print("welcome to the Treasure Island. Your mission is to find the treasure.")

side=input('You are at a crossroad.which side you want to move first? if right then write "right" or write left for "left" turn:\n').lower()

if side=="left":
    what_next=input('You have to come to a lake.There is an island in the middle of the lake.do you want to swim or to wait?if swim then write "swim" or write " wait" to wait for a boat:\n ').lower()
    if what_next=="wait":
        which_door=input("You have reached the island unharmed.There is a house with 3 doors. what color you want to choose? red,blue,yellow or others: \n").lower()
        if which_door=="red":
            print("Burned by fire.Game over....")
        elif which_door=="blue":
            print("Eaten by beasts.Game Over.")
        elif which_door=="yellow":
            print("CONGRATULATIONS!!YOU WIN!! ")
        else:
            print("Game over")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("GAME OVER. Fall into a hole....")
