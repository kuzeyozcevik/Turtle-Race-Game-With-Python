import random
from turtle import *
isContinue = False
screen = Screen()
screen.setup(500,400)
color_list = ["red","orange","yellow","green","blue","purple"]
turtle_list = []
num = -95
player_amount = screen.numinput("Player Count","How many player is going to play 1 or 2")
if player_amount == 1:
    guess1 = screen.textinput("Turtle","Which turtle is going to win? Enter a color")
    if guess1.lower() in color_list:
        isContinue = True
elif player_amount == 2:
    guess2 = screen.textinput("Turtle", "Player 1, Which turtle is going to win? Enter a color")
    guess3 = screen.textinput("Turtle", "Player 2, Which turtle is going to win? Enter a color")
    if guess2.lower() in color_list and guess3.lower() in color_list:
        isContinue = True
for n in color_list:
    kuzey = Turtle(shape="turtle")
    kuzey.color(n)
    kuzey.penup()
    kuzey.goto(-220,num)
    num += 40
    turtle_list.append(kuzey)

while isContinue:
    for n in turtle_list:
        if n.pos()[0] > 250-(63/2):
            isContinue = False
            turtle_list.clear()
            if player_amount == 1:
                if n.pencolor() == guess1:
                    print(f"You have guessed right! The {n.pencolor()} turtle won!")
                else:
                    print(f"You have guessed wrong! The {n.pencolor()} turtle won!")
            else:
                if n.pencolor() == guess2:
                    print(f"Player 1 has guessed right. The {n.pencolor()} turtle won!")
                elif n.pencolor() == guess3:
                    print(f"Player 2 has guessed right. The {n.pencolor()} turtle won!")
                else:
                    print(f"No one could guessed right. The {n.pencolor()} turtle won!")
        random_distance = random.randint(1, 10)
        n.forward(random_distance)
screen.mainloop()

