import turtle
import os
import math
import random
import pygame

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space.gif")
def playsound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
#Register the shapes
turtle.register_shape("space invaders.gif")
turtle.register_shape("aircraft.gif")

#border
border_pen =turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
#set the score
score=0
#music
pygame.init()
playsound("alien-spaceship_daniel_simion.wav")
#Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring ="Score: "+ str(score)
score_pen.write(scorestring,False, align = "left",font=("Arial",14,"normal"))
score_pen.hideturtle()

#create player turtle

player =turtle.Turtle()
player.color("blue")
player.shape("aircraft.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#choose no of enemies
number_of_enemies = 5
#empty list of enemies
enemies=[]
#Add enemies
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("space invaders.gif")
    enemy.penup()
    enemy.speed(0)
    x= random.randint(-200,200)
    y= random.randint(100,250)
    enemy.setposition(x,y)
enemyspeed = 2

#create players bullet
bullet= turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20
#define bullet state
#ready -ready to fire
#fire - bullet is firing
bulletstate="ready"
#move player left and right
def move_left():
    x = player.xcor()
    x-=playerspeed
    if x<-280:
        x = -280
    player.setx(x)
def move_right():
    x = player.xcor()
    x+=playerspeed
    if x>280:
        x=280
    player.setx(x)
def fire_bullet():
    #declare bulletstate as global if it needs to be changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #move the bullet to just above the player
        x = player.xcor()
        y = player.ycor()+ 10
        bullet.setposition(x,y)
        bullet.showturtle()
def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
                         
    
#create keyboard binding
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")
turtle.listen()
#main game loop
while True:
    for enemy in enemies:
        #move enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
        #move the enemy
        if enemy.xcor()>280:
            for e in enemies:
                y= enemy.ycor()
                y-=40
                e.sety(y)
            enemyspeed*=-1
                
        if enemy.xcor()<-280:
            for e in enemies:
                y=enemy.ycor()
                y-=40
                e.sety(y)
            enemyspeed*=-1
        #check for collision between bullet and enemy
        if isCollision(bullet,enemy):
            #reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #reset the enemy
            x= random.randint(-200,200)
            y= random.randint(100,250)
            enemy.setposition(x,y)
            score+=10
            scorestring = "Score: " +str(score)
            score_pen.clear()
            score_pen.write(scorestring,False, align = "left",font=("Arial",14,"normal"))
            
        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            Print("Game Over")
            breakpoint
    #move bullet
    if bulletstate =="fire":
        y = bullet.ycor()
        y+= bulletspeed
        bullet.sety(y)
    #check if the bullet has gone top
    if bullet.ycor()> 275:
        bullet.hideturtle()
        bulletstate ="ready"

