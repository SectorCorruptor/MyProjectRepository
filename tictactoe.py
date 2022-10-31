# this is a comment, and Python skips to the next line when it encounters this (and we learnt that)

#=====================================================================================================================#

# tictactoe.py
# Basic graphic layout inspired by turtledemo's nim.py
# Mohammed Rizwan Niju

from turtle import *

mick = Turtle() # by the way, mick is only for detecting mouse position when clicked
mick.hideturtle() # oh, and his naming is inspired by the Python Docs, after one of their examples in the turtle folder 
mick.pu()
mick.speed(0)
ho = Turtle()
ho.hideturtle()
hideturtle()

class VarClass: # Variable Class
    screen = "home1"
    playerturn = 1
    mx = 200
    my = 200
    plays = ["", "", "", "", "", "", "", "",""]

def write_at(x, y, txt, move, align, size):
    wasspeed = speed()
    speed(0)
    pu()
    goto(x,y)
    write(txt, move, align, font=("Century Gothic", size, "normal"))
    speed(wasspeed)

def finish():
    u = VarClass.plays
    focus = "x"
    if (u[0] == focus and u[4] == focus and u[8] == focus) or (u[2] == focus and u[4] == focus and u[6] == focus) or (u[0] == focus and u[3] == focus and u[6] == focus) or (u[1] == focus and u[4] == focus and u[7] == focus) or (u[2] == focus and u[5] == focus and u[8] == focus) or (u[0] == focus and u[1] == focus and u[2] == focus) or (u[3] == focus and u[4] == focus and u[5] == focus) or (u[6] == focus and u[7] == focus and u[8] == focus):
        write_at(0, -250, "Player " + focus + " wins!", False, "center", 25)
    else:
        focus = "o"
        if (u[0] == focus and u[4] == focus and u[8] == focus) or (u[2] == focus and u[4] == focus and u[6] == focus) or (u[0] == focus and u[3] == focus and u[6] == focus) or (u[1] == focus and u[4] == focus and u[7] == focus) or (u[2] == focus and u[5] == focus and u[8] == focus) or (u[0] == focus and u[1] == focus and u[2] == focus) or (u[3] == focus and u[4] == focus and u[5] == focus) or (u[6] == focus and u[7] == focus and u[8] == focus):
            write_at(0, -250, "Player " + focus + " wins!", False, "center", 25)
        else:
            if u.count("") == 0:
                write_at(0, -250, "It's a draw.", False, "center", 25)
            else:
                pass

def drawtictactoe():
    speed(0)
    pu()
    pensize(15)
    pencolor("gray")
    goto(50, 150)
    pd()
    goto(50, -150)
    pu()
    goto(-50, 150)
    pd()
    goto(-50, -150)
    pu()
    goto(-150, 52)
    pd()
    goto(150, 52)
    pu()
    goto(150, -52)
    pd()
    goto(-150, -52)

def draw(let, x, y):
    ho.pu()
    ho.pencolor("gray")
    ho.pensize(10)
    ho.goto(x, y)
    if let == "x":
        write_at(x, y, "X", False, "center", 80)
    elif let == "o": # elif means 'else if' and we learned about this
        write_at(x, y, "O", False, "center", 80)
        # produces an o shape
        
def gothere(x, y):
    mick.goto(x, y)
    VarClass.mx = x
    VarClass.my = y
    if VarClass.mx > 50 and VarClass.mx < 150:
        if VarClass.my > 52 and VarClass.my < 150  and VarClass.plays[2] == "":
            if VarClass.playerturn == 0:
                draw("x", 105, 60)
                VarClass.plays[2] = "x"
            else:
                draw("o", 105, 60)
                VarClass.plays[2] = "o"
            VarClass.playerturn = 1 - VarClass.playerturn
        elif VarClass.my > -52 and VarClass.my < 52  and VarClass.plays[5] == "":
            if VarClass.playerturn == 0:
                draw("x", 105, -65)
                VarClass.plays[5] = "x"
            else:
                draw("o", 105, -65)
                VarClass.plays[5] = "o"
            VarClass.playerturn = 1 - VarClass.playerturn
        elif VarClass.my > -150 and VarClass.my < -52 and VarClass.plays[8] == "":
            if VarClass.playerturn == 0:
                draw("x", 105, -165)
                VarClass.plays[8] = "x"
            else:
                draw("o", 105, -165)
                VarClass.plays[8] = "o"
            VarClass.playerturn = 1 - VarClass.playerturn
    elif VarClass.mx > -50 and VarClass.mx < 50:
        if VarClass.my > 52 and VarClass.my < 150 and VarClass.plays[1] == "":
            if VarClass.playerturn == 0:
                draw("x", 0, 60)
                VarClass.plays[1] = "x"
            else:
                draw("o", 0, 60)
                VarClass.plays[1] = "o"
            VarClass.playerturn = 1 - VarClass.playerturn
        elif VarClass.my > -52 and VarClass.my < 52 and VarClass.plays[4] == "":
            if VarClass.playerturn == 0:
                draw("x", 0, -65)
                VarClass.plays[4] = "x"
            else:
                draw("o", 0, -65)
                VarClass.plays[4] = "o"
            VarClass.playerturn = 1 - VarClass.playerturn
        elif VarClass.my > -150 and VarClass.my < -52 and VarClass.plays[7] == "":
            if VarClass.playerturn == 0:
                draw("x", 0, -165)
                VarClass.plays[7] = "x"
            else:
                draw("o", 0, -165)
                VarClass.plays[7] = "o"
            VarClass.playerturn = 1 - VarClass.playerturn
    elif VarClass.mx > -150 and VarClass.mx < -50:
        if VarClass.my > 52 and VarClass.my < 150 and VarClass.plays[0] == "":
            if VarClass.playerturn == 0:
                draw("x", -105, 60)
                VarClass.plays[0] = "x"
            else:
                draw("o", -105, 60)
                VarClass.plays[0] = "o"
            VarClass.playerturn = 1 - VarClass.playerturn
        elif VarClass.my > -52 and VarClass.my < 52 and VarClass.plays[3] == "":
            if VarClass.playerturn == 0:
                draw("x", -105, -65)
                VarClass.plays[3] = "x"
            else:
                draw("o", -105, -65)
                VarClass.plays[3] = "o"
            VarClass.playerturn = 1 - VarClass.playerturn
        elif VarClass.my > -150 and VarClass.my < -52 and VarClass.plays[6] == "":
            if VarClass.playerturn == 0:
                draw("x", -105, -165)
                VarClass.plays[6] = "x"
            else:
                draw("o", -105, -165)
                VarClass.plays[6] = "o"
            VarClass.playerturn = 1 - VarClass.playerturn
    finish()
def twop():
    VarClass.screen = "home2p"
    clear()
    home()
    drawtictactoe()
    mick.screen.bgcolor("orange")
    pencolor("black")
    hideturtle()
    mick.hideturtle()
    pu()
    mick.screen.onclick(gothere, 1, False)

def hometwo():
    VarClass.screen = "home2"
    clear()
    home()
    mick.screen.bgcolor("orange")
    drawtictactoe()
    pencolor("black")
    write_at(0, -250, "Select the number of players", False, "center", 25)
    write_at(0, -260, "Use 1 key for CPU against you. (Coming soon)", False, "center", 10)
    write_at(0, -275, "Use 2 key for 2 players.", False, "center", 10)
    onkey(twop, "2")

listen()
if VarClass.screen == "home1":
    ht()
    home()
    mick.screen.bgcolor("orange")
    drawtictactoe()
    pencolor("black")
    write_at(0,-250, "Tic Tac Toe", False, "center", 25)
    write_at(0,-260, "Press space to begin", False, "center", 10)
    onkey(hometwo, "space")


    
