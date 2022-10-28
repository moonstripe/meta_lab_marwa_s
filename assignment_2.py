import math

# useful functions

def spherical_volume_from_radius(r):
    pi = math.pi
    return 4/3 * pi * r ** 3

# initializing firstname and last name

print("Hello, world!")
print("What's your first name?")
Firstname = input()
print("What is your last name?")
Lastname = input()

# initializing and empty variable

lang = ""

# while loop to complete consequitive functions

while not lang:
    print("Please select a language: (E)nglish , (S)panish, or (F)rench?")
    language = input()
    lang = language[0]
    print("Hey, I'm seeing a language of " + language + " and a lang of " + lang)

    # determine language from user input

    if lang in ["e", "E"]:
        print(("Hello, ") + Firstname + Lastname)
    elif lang == "s" or lang == "S":
        print(("Que pasa, ") + Firstname + Lastname)
    elif lang == "f" or lang == "F":
        print(("Enchanté, ") + Firstname + Lastname)
    else:
        print("You have entered an invalid response!")

    # favorite number section

    favoritenumber = len(Firstname)
    secondfavoritenumber = len(Lastname)
    print(str(favoritenumber) + " plus " + str(secondfavoritenumber) + " = " + 
        str(favoritenumber + secondfavoritenumber))
    print(str(favoritenumber) + " times " + str(secondfavoritenumber) + " = " +
        str(favoritenumber * secondfavoritenumber))
    print(str(favoritenumber) + " to the " + str(secondfavoritenumber) + " = " +
        str(favoritenumber ** secondfavoritenumber))
    print(str(favoritenumber) + " divided by " + str(secondfavoritenumber) + " = " +
        str(favoritenumber / secondfavoritenumber))
    print("A sphere with radius " + str(favoritenumber) + " will have a volume of " + str(spherical_volume_from_radius(favoritenumber)))