from time import time
import turtle
import colorsys
import phonenumbers
from phonenumbers import carrier,geocoder,timezone

def Nr_1():
    t= turtle.Turtle()
    s = turtle.Screen()  
    s.bgcolor('black')
    t.speed(0)
    n = 200
    h= 0
    for i in range(360):
        t.begin_fill()
        for j in range(2):
            c = colorsys.hsv_to_rgb(h,1,0.8)
            h+= 1/n
            t.color(c)
            t.left(20)
            t.forward(i-j)
        t.end_fill()


def Nr2():
    t= turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor('black')
    t.speed(0)
    n = 50
    h= 0
    for i in range(360):
        c = colorsys.hsv_to_rgb(h,1, 0.8)
        h +=1/n
        t.color(c)
        t.forward(i*2)
        t.left(145)

def Phonenumber():
    mobileNo = input("Enter Mobile Number with Country Code: ")
    mobileNo = phonenumbers.parse(mobileNo)

    #get Timezone
    print(timezone.time_zones_for_number(mobileNo))


    #Getting Träger 
    print(carrier.name_for_number(mobileNo, "de"))

    #getting region
    print(geocoder.description_for_number(mobileNo,"de"))
    
    #prüfen
    print("Verfügbare Nummer: ", phonenumbers.is_valid_number(mobileNo))

    #check wahrscheinlichkeit 
    print("Wahrscheinlichkeit: ",phonenumbers.is_possible_number(mobileNo))

Phonenumber()
