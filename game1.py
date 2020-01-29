import turtle
import os
import sys

wn=turtle.Screen()
wn.title("Badminton")
wn.bgcolor("blue")
wn.setup(width=500,height=700)
wn.tracer(0)

#padleA
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("red")
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=5,stretch_wid=1)
paddle_a.penup()
paddle_a.goto(0,330)
score_a=0

#padleB
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("red")
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=5,stretch_wid=1)
paddle_b.penup()
paddle_b.goto(0,-330)
score_b=0

#ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=0.1

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.goto(0,0)
pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center", font=("Courrier",20,"normal"))
pen.hideturtle()

def paddle_a_left():
    x=paddle_a.xcor()
    if x<-250:
        return
    x-=20
    paddle_a.setx(x)
    

def paddle_a_right():
    x=paddle_a.xcor()
    if x>250:
        return
    x+=20
    paddle_a.setx(x)


def paddle_b_left():
    x=paddle_b.xcor()
    if x<-250:
        return
    x-=20
    paddle_b.setx(x)

def paddle_b_right():
    x=paddle_b.xcor()
    if x>250:
        return
    x+=20
    paddle_b.setx(x)




#keyboardbinding

wn.listen()
wn.onkeypress(paddle_a_left,"a")
wn.onkeypress(paddle_a_right,"d")
wn.onkeypress(paddle_b_left,"Left")
wn.onkeypress(paddle_b_right,"Right")


while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #boarder cheching
    if ball.ycor()>340:
        ball.goto(0,0)
        ball.dx*=-1
        ball.dy*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(str(score_a),str(score_b)),align="center", font=("Courrier",20,"normal"))

    if ball.ycor()<-340:
        ball.goto(0,0)
        ball.dx*=-1
        ball.dy*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(str(score_a),str(score_b)),align="center", font=("Courrier",20,"normal"))

    if ball.xcor()>240:
        ball.dx*=-1

    if ball.xcor()<-240:
        ball.dx*=-1


    if (ball.xcor()>paddle_a.xcor()-50 and ball.xcor()<paddle_a.xcor()+50) and (ball.ycor() >310):
        ball.dy*=-1

    if (ball.xcor()>paddle_b.xcor()-50 and ball.xcor()<paddle_b.xcor()+50) and (ball.ycor() <-310):
        ball.dy*=-1


    if score_a==3:
        pen.clear()
        pen.write("Player A Wins",align="center",font=("Courrier",20,"normal"))
        sys.exit()
        

    if score_b==3:
        pen.clear()
        pen.write("Player B Wins",align="center",font=("Courrier",20,"normal"))
        sys.exit()
        

    