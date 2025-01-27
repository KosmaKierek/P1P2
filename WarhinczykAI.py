from flask import Flask, Blueprint, render_template, render_template_string, redirect, request, session, redirect, url_for
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

#app setup
WarhinczykAI = Blueprint("WarhinczykAI", __name__, static_folder="static", template_folder="templates")
#Scss(WarhinczykAI)

#WarhinczykAI.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

#WarhinczykAI.secret_key = 'BAD_SECRET_KEY'
#-------------------------------------------------------------------------
class Game:
    def __init__(self, field):
        self.field=field

class Player:
    def __init__(self, pionki):
        self.pionki=pionki
        self.current=0
        self.score=0

player1=Player([1,2,3])
player2=Player([4,5,6])
fields=Game([0,0,0,0,0,0,0,0,0,0])

pionki = {
    1: player1.pionki[0],
    2: player1.pionki[1],
    3: player1.pionki[2],
    4: player2.pionki[0],
    5: player2.pionki[1],
    6: player2.pionki[2]
}

@WarhinczykAI.route("/gameAI", methods=["POST","GET"])
def game():
    if request.method == "GET":
        fields.field=[0,0,0,0,0,0,0,0,0,0]
        player1.current=0
        player2.current=0
        player1.score=0
        player2.score=0
    return render_template('graAI/game.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
#rzut kostka, ruchy w /game/<costam>

@WarhinczykAI.route("/gameAI/p1", methods=["POST","GET"])
def movep1():
    if request.method == "POST":
        for i in fields.field:
            if fields.field[i]==pionki[1]:
                player1.current=i
            if fields.field[i]==pionki[4]:
                player2.current=i
        if player1.current==0:
            now=random.randint(1, 2)
        else:
            now=random.randint(1, 3)
        #
        #  wygrana do wyboru jaki pionek przez wygranego
        #
        if player1.current>=len(fields.field):
            player1.score+=10
            if player1.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P1win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/win.html')
        elif player1.current+now>=len(fields.field):
            player1.score+=10
            if player1.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P1win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/win.html')
        elif player2.current>=len(fields.field):
            player2.score+=10
            if player2.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P2win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/loose.html')
        elif player1.current+now<len(fields.field):
            if (fields.field[player1.current+now]==fields.field[player2.current] and player2.current!=0):
                fields.field[player1.current]=0
                player1.current=0
            else:
                fields.field[player1.current+now]=pionki[1]
                fields.field[player1.current]=0
                player1.current=player1.current+now
    return render_template('graAI/gamep2_1.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score,now=now)

@WarhinczykAI.route("/gameAI/p2", methods=["POST","GET"])
def movep2():
    if request.method == "POST":
        for i in fields.field:
            if fields.field[i]==pionki[2]:
                player1.current=i
            if fields.field[i]==pionki[5]:
                player2.current=i
        if player1.current==0:
            now=random.randint(1, 2)
        else:
            now=random.randint(1, 3)
        #
        #  wygrana do wyboru jaki pionek przez wygranego
        #
        if player1.current>=len(fields.field):
            player1.score+=10
            if player1.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P1win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/win.html')
        elif player1.current+now>=len(fields.field):
            player1.score+=10
            if player1.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P1win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/win.html')
        elif player2.current>=len(fields.field):
            player2.score+=10
            if player2.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P2win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/loose.html')
        elif player1.current+now<len(fields.field):
            if (fields.field[player1.current+now]==fields.field[player2.current] and player2.current!=0):
               fields.field[player2.current]=0
               player2.current=0
               fields.field[player1.current+now]=pionki[2]
               fields.field[player1.current]=0
               player1.current=player1.current+now
            else:
               fields.field[player1.current+now]=pionki[2]
               fields.field[player1.current]=0
               player1.current=player1.current+now
    return render_template('graAI/gamep2_2.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score,now=now)

@WarhinczykAI.route("/gameAI/p3", methods=["POST","GET"])
def movep3():
    if request.method == "POST":
        for i in fields.field:
            if fields.field[i]==pionki[3]:
                player1.current=i
            if fields.field[i]==pionki[6]:
                player2.current=i
        if player1.current==0:
            now=random.randint(1, 2)
        else:
            now=random.randint(1, 3)
        #
        #  wygrana do wyboru jaki pionek przez wygranego
        #
        if player1.current>=len(fields.field):
            player1.score+=10
            if player1.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P1win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/win.html')
        elif player1.current+now>=len(fields.field):
            player1.score+=10
            if player1.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P1win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/win.html')
        elif player2.current>=len(fields.field):
            player2.score+=10
            if player2.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P2win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/loose.html')
        elif player1.current+now<len(fields.field):
            if (fields.field[player1.current+now]==fields.field[player2.current] and player2.current!=0):
                fields.field[player1.current]=0
                fields.field[player1.current+now-1]=pionki[3]
                player1.current=player1.current+now-1
            else:
                fields.field[player1.current+now]=pionki[3]
                fields.field[player1.current]=0
                player1.current=player1.current+now
    return render_template('graAI/gamep2_3.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score,now=now)

#----------------------------------------------------------------------------------

@WarhinczykAI.route("/gameAI/p4", methods=["POST","GET"])
def movep4():
    if request.method == "POST":
        for i in fields.field:
            if fields.field[i]==pionki[1]:
                player1.current=i
            if fields.field[i]==pionki[4]:
                player2.current=i
        if player2.current==0:
            now=random.randint(1, 2)
        else:
            now=random.randint(1, 3)
        if player2.current>=len(fields.field):
            player2.score+=10
            if player2.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P2win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/loose.html')
        elif player2.current+now>=len(fields.field):
            player2.score+=10
            if player2.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P2win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/loose.html')
        elif player1.current>=len(fields.field):
            player1.score+=10
            if player1.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P1win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/win.html')
        elif player2.current+now<len(fields.field):
            if (fields.field[player2.current+now]==fields.field[player1.current] and player1.current!=0):
                fields.field[player2.current]=0
                player2.current=0
            else:
                fields.field[player2.current+now]=pionki[4]
                fields.field[player2.current]=0
                player2.current=player2.current+now
    return render_template('graAI/gamep1_1.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score,now=now)

@WarhinczykAI.route("/gameAI/p5", methods=["POST","GET"])
def movep5():
    if request.method == "POST":
        for i in fields.field:
            if fields.field[i]==pionki[2]:
                player1.current=i
            if fields.field[i]==pionki[5]:
                player2.current=i
        if player2.current==0:
            now=random.randint(1, 2)
        else:
            now=random.randint(1, 3)
        if player2.current>=len(fields.field):
            if player2.score<35:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               player2.score+=10
               return render_template('graAI/P2win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/loose.html')
        elif player2.current+now>=len(fields.field):
            player2.score+=10
            if player2.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P2win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/loose.html')
        elif player1.current>=len(fields.field):
            player1.score+=10
            if player1.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P1win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/win.html')
        elif player2.current+now<len(fields.field):
            if (fields.field[player2.current+now]==fields.field[player1.current] and player1.current!=0):
                fields.field[player1.current]=0
                player1.current=0
                fields.field[player2.current+now]=pionki[5]
                fields.field[player2.current]=0
                player2.current=player2.current+now
            else:
                fields.field[player2.current+now]=pionki[5]
                fields.field[player2.current]=0
                player2.current=player2.current+now
    return render_template('graAI/gamep1_2.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score,now=now)

@WarhinczykAI.route("/gameAI/p6", methods=["POST","GET"])
def movep6():
    if request.method == "POST":
        for i in fields.field:
            if fields.field[i]==pionki[3]:
                player1.current=i
            if fields.field[i]==pionki[6]:
                player2.current=i
        if player2.current==0:
            now=random.randint(1, 2)
        else:
            now=random.randint(1, 3)
        if player2.current>=len(fields.field):
            player2.score+=10
            if player2.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P2win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/loose.html')
        elif player2.current+now>=len(fields.field):
            player2.score+=10
            if player2.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P2win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/loose.html')
        elif player1.current>=len(fields.field):
            player1.score+=10
            if player1.score<30:
               fields.field=[0,0,0,0,0,0,0,0,0,0]
               player1.current=0
               player2.current=0
               return render_template('graAI/P1win.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score)
            else:
               return render_template('graAI/win.html')
        elif player2.current+now<len(fields.field):
            if (fields.field[player2.current+now]==fields.field[player1.current] and player1.current!=0):
                fields.field[player2.current]=0
                fields.field[player2.current+now-1]=pionki[6]
                player2.current=player2.current+now-1
            else:
                fields.field[player2.current+now]=pionki[6]
                fields.field[player2.current]=0
                player2.current=player2.current+now
    return render_template('graAI/gamep1_3.html',fields=fields.field,pionki=pionki,P1score=player1.score,P2score=player2.score,now=now)


#@Warhinczyk.route("/game", methods=["POST","GET"])
#def game():
#    player1=[1]
#    pola = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#
#    if request.method == "POST":
#        current_field=current_field+1
#        pola[current_field]=1
#
#   return render_template('game.html', player1=player1, current_field=current_field, pola=pola )


#if __name__ in "__main__":
 #   WarhinczykAI.run(debug=True)