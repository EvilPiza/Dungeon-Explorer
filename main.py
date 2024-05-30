#Dungeon Explorer Demo! (DgE for short) 


print("Welcome to Dungeon Explorer!")
print(" ")
print("This game is currently in it's Demo phase so bugs should be expected!")
print(" ")
print("If you don't know how to play put 'list' or 'lst' to see a list of the controls")
print(" ")
import random
import time

starting_pos = random.randint(1,3)
health = 100
new_pos = ""
facing = 0 #doesn't do anything yet so change it to whatever lol
#cheats = False WIP

def action():
    while health > 0:
        global fact
        inp = str(input("Action: "))
        if inp == "walk":
            walk()
        if inp == "look":
            look()
        if inp == "where":
            where_am_i()
        if inp == "list" or inp == "lst":
            lst()
        #if inp == "extras" or inp == "extra" or inp == "sss" or inp == "super secret settings":
            #extras()

def lst():
  print(" ")
  print("Action Controls")
  print("-'look' or 'l' to Look")
  print("-'walk' or 'w' to Walk")
  print("-'back' to exit the Look/Walk menu and go back to the Action menu")
  print(" ")
  print("Look/Walk Controls")
  print("-'left' or 'l' to Look/Walk Left")
  print("-'right' or 'r' to Look/Walk Right")
  print("-'forward' or 'f' to Look/Walk Forward")
  print("-'behind' or 'b' to Look/Walk behind yourself")
  print(" ")
  print("Question Controls")
  print("-'yes' or 'y' to respond Yes to a question")
  print("-'no' or 'n' to respond No to a question")
  print(" ")
  print("Make sure your input is ALWAYS LOWERCASE")
  print(" ")


def look():
    inp = str(input("Look: "))
    
    if inp == "right" or inp == "r":
        if starting_pos == 1:
            print("You look right.. You see a door.")
        if starting_pos == 2:
            print("You look right.. You see an empty hallway.")
        if starting_pos == 3:
            print("You look right.. You are in a rather large empty room.")
            
    if inp == "left" or inp == "l":
        if starting_pos == 1:
            print("You look left.. You see a narrow hallway.")
        if starting_pos == 2:
            print("You look left.. You see a hallway, there is something on the ground.")
        if starting_pos == 3:
            print("You look left.. You see the exit.")
    
    if inp == "forward" or inp == "front" or inp == "f":
        if starting_pos == 1:
            print("You look forward.. You are looking at a wall made of brick.")
        if starting_pos == 2:
            print("You look forward.. You see a very dark hallway. Something about it doesn't feel right..")
        if starting_pos == 3:
            print("You look forward.. You are in a rather large empty room.")
    
    if inp == "behind" or inp == "b":
        if starting_pos == 1:
            print("You look back.. You are looking at a wall made of brick.")
        if starting_pos == 2:
            print("You look back.. You see a dimly lit hallway.")
        if starting_pos == 3:
            print("You look back.. You are in a rather large empty room.")
    
def walk():
    inp = str(input("Walk: "))
    
    if inp == "left" or inp == "l":
        if starting_pos == 1:
            print("You walk left.. ")
        if starting_pos == 2:
            print("You walk left.. ")
        if starting_pos == 3:
            print("You walk left.. ")
            
    if inp == "right" or inp == "r":
        if starting_pos == 1:
            print("You walk right.. ")
            interact1()
        if starting_pos == 2:
            print("You walk right.. ")
        if starting_pos == 3:
            print("You walk right.. ")
    
    if inp == "forward" or inp == "front" or inp == "f":
        if starting_pos == 1:
            print("You walk forward.. ")
        if starting_pos == 2:
            print("You walk forward.. ")
        if starting_pos == 3:
            print("You walk forward.. ")
    
    if inp == "behind" or inp == "b":
        if starting_pos == 1:
            print("You walk backward.. ")
        if starting_pos == 2:
            print("You walk backward.. ")
        if starting_pos == 3:
            print("You walk backward.. ")
        
def where_am_i():
    global new_pos
    if new_pos == "":
        if starting_pos == 1:
            print("You are in a hallway.")
        if starting_pos == 2:
            print("You are in a 4-way hallway intersection.")
        if starting_pos == 3:
            print("You are in a large empty room.")
    if new_pos != "":
        print("You are in a " + new_pos)
            
def interact1():
    inp = str(input("Interact: "))
    if inp == "yes" or inp == "y":
        global new_pos
        new_pos = "large empty room"
        print("You open the door.. Your now in a large empty room.")

#super secret extras
def extras():
  global extras
  print("Just so you know, the Super Secret Settings ARE considered cheats")
  inp = str(input("Super Secret Settings? "))
  if inp == "yes" or "y":
    cheats = True
    sss()
  elif inp == "no" or "n":
    cheats = False

def sss():
  global health
  inp = str(input("Which settin' you needin' pluh? "))
  if inp == "list" or inp == "lst":
    print(" ")
    print("Super Secret Settings Controls")
    print("-'beatthegame' or 'btg' instantly beats the game for you!")
    print("-'infhealth' or 'ih' gives you infinite health!")
    print("-'i was just playin' cuh' exits the Super Secret Settings menu")
    print(" ")
  if inp == "beatthegame" or inp == "btg":
    health = 0 
    print("You lose!")
  if inp == "i was just playin' cuh":
    print(" ")
    print("ight i gotchu playa just lmk if you change yo mind")
    print(" ")
    action()
action()
