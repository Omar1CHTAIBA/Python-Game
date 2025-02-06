import turtle
import random
import math
import winsound

# Setup screen:


window = turtle.Screen() # display the screen
window.bgcolor("black") # define the baground color
window.bgpic("space.png")
window.setup(width=700, height=560) # define the with and height
window.tracer(4) # skip frames to have a good game-play
score = 0



# Draw borders
border = turtle.Turtle() # turtle is the module | Turtle is like a pen
border.speed(0) # Draw speed ; it's from0 to 10 but 0 is the fatest | by default the pen is on a cordinnate 0x&y
border.penup() # disable the pen
border.setposition(-300, -230) # The place where i want the pen to go in
border.pendown()# enable the pen 
border.pensize(5) # Somk dyal pen
border.color("red") # choosing the color of the pen
for i in (700, 560, 700, 560):
    border.forward(i - 100) # To make the pen or the turtle go
    border.left(90)
border.hideturtle()

# Draw score:
border.penup()
border.setposition(-300, 235)
border.color("white")
border.write(f"Score: {score}", align="left", font=("Courier", 22, 'bold'))

# Register the custom shape


spaceship_shape = ((-10, -10), (0, -5), (10, -10), (0, 10))
window.register_shape("spaceship", spaceship_shape)


# create player:


player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("spaceship")
player.color("white")
######################


player_speed = 0.4

#Creat a List of cercles
# Create One Cercles
cercles = []
cercle_count = 8
for i in range(cercle_count):
    cercles.append(turtle.Turtle())
    cercles[i].speed(0)
    cercles[i].penup() 
    cercles[i].shape("circle")
    cercles[i].color(random.choice(["yellow", "cyan", "#34eb5b", "#eb345c"]))
    cercles[i].setposition(random.randint(-285, 285), random.randint(-215, 215))

cercle_speed = 0.5


# ================= Game Functions ==================
def turn_left():
    player.left(30)


def turn_right():
    player.right(30)


def increase_speed():
    global player_speed
    player_speed += 0.1


def decrease_speed():
    global player_speed
    if player_speed < 0.1:
        return
    player_speed -= 0.1


def isCollision(player, cercle):
    distance = math.sqrt(
        math.pow(player.xcor() - cercle.xcor(), 2) + math.pow(player.ycor() - cercle.ycor(), 2)
    )
    if distance < 20:
        return True
    else:
        return False

# key bindings
window.listen()
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")
window.onkey(increase_speed, "Up")
window.onkey(decrease_speed, "Down")


# Game Loop:
while True:
    player.forward(player_speed) # moving player

    # Player and border collision 
    if player.xcor() > 285 or player.xcor() < -285:
        player.right(180)
    if player.ycor() > 215 or player.ycor() < -215:
        player.right(180)


    # Circules mouvement :
    for cercle in cercles:
        cercle.forward(cercle_speed) # moving Circules


    # Cercle and border collision :
        if cercle.xcor() > 285 or cercle.xcor() < -285:
            cercle.right(180)
        if cercle.ycor() > 215 or cercle.ycor() < -215:
            cercle.right(180)


        if isCollision(player, cercle):
            cercle.setposition(random.randint(-285, 285), random.randint(-215, 215))
            cercle.right(random.randint(0, 360))
            # Update Score :
            score += 1
            border.undo()
            border.write(f"Score: {score}", align="left", font=("Courier", 22, 'bold'))
            print(score)
            winsound.PlaySound('collision.wav', winsound.SND_ASYNC)


# Don't close the window (you can close it with the 'red-x'):
window.mainloop()