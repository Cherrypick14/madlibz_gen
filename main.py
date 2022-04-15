#   this is a madlibz game generator
#   the game is all about coming up with a story
#   a user isprovided with some few words and they get to complete the story
#   we are gonna use tkinter for our GUI

#   recipies for the game
#   import tkinter module
#   display a window
#   Buttons
#   add functionalities to the button

from tkinter import *
from turtle import bgcolor

#    create our window display
screen = Tk(className='window-color')
screen.configure(bg='lightblue')
screen.geometry('400x400')
screen.title('Tell us your story...')
Label(screen, text="Hey there, let's create a story\n Make it awesome!..", font='arial 18 bold').pack()
Label(screen, text="You can select any of the buttons below", font='arial 15 bold').place(x=10, y=80)

# define our functions
def main_story():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    location = input("Enter your current location: ")
    siblings = int(input("Enter the total no of siblings you have: "))
    profession= input("Enter your profession: ")
    books = input("Enter your favorite book: ")
    university = input("Enter your university: ")
    major = input("Enter your major: ")
    year_of_graduation = input("Enter your year of graduation: ")
    company =input("Enter a company you wanna work for: ")
     
    print(f"Hey there, my name is {name} and I am {age} years of age. My current location is {location} and I have {siblings} siblings in total.\nI'm curently enrolled in {university} and my major is {major}.\nI'm happy to announce that my graduation will be on {year_of_graduation}and one of my favorite books of all time is {books}.\nMy profession is{profession} and I'd love to work for {company} because when I say my name and it's name, it's like a march made in heaven. ")

def game_story():
    game = input("Enter your fav sport: ")
    awards= int(input("Enter the no of awards you've earned playing this game: "))
    year = int(input("Enter the year you earned this achievement: "))
    future_sport=input("Enter a sport you see yourself playing in the future: ")

    print(f"Well my favorite sport is {game} and so far the number of awards I have are {awards} since {year}\nIn the near future I'd love to play{future_sport}")


#define our buttons
Button(screen, text="Get to know me",font='arial 13 italic', command = main_story).place(x=120, y=160)

Button(screen, text="Check out my sport's story!",font='arial 13 italic', command=game_story).place(x=80, y=220)



#   run the program
screen.mainloop()


