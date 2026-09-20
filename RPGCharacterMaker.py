yesno = ["yes","no"]
def CharacterName():
    while True:
        name = input("Please Enter Your Character Name: ")
        print(f"Your name is",name)
        sure = input("Are you sure you want this name?(yes/no): ").lower()
        if sure == "yes":
            print("Confirmed player's name")
            return name
        elif sure == "no":
            continue
        else:
            print("please type only ","yes or no")
name = CharacterName()

PassGender = ["male","female"]
def CharacterGender():
    while True:
        gender = input("Please choose your gender(Male/Female): ").strip().lower()

        if gender in PassGender:
            print(f"Your gender is",gender)
            sure = input("Are you sure you want this gender?(yes/no): ").lower()

            if sure == "yes":
                print("Confirmed player's gender")
            elif sure == "no":
                continue
            else:
                print("please type only ","yes or no")

            print("Done selected your gender")
            return gender
        else:
            print("Only choose gender from list")
gender = CharacterGender()

PassRace = ["human","elf","dwarf","demon"]
def CharacterRace():
    while True:
        race = input("Please choose your race(Human,Elf,Dwarf,Demon): ").strip().lower()

        if race in PassRace:
            print(f"Your race is",race)
            sure = input("Are you sure you want this race?(yes/no): ").lower()
     
            if sure == "yes":
                print("Confirmed player's race")
            elif sure == "no":
                continue
            else:
                print("please type only ","yes or no")       
            print("Done selected your race")
            return race
        else:
            print("Only choose race from list")
race = CharacterRace()

PassClass = ["warrior","rogue","mage","priest","archer"]
def CharacterClass():
    while True:
        classs = input("Please choose your class(warrior,rogue,mage,priest,archer): ").strip().lower()

        if classs in PassClass:
            print(f"Your gender is",classs)
            sure = input("Are you sure you want this class?(yes/no): ").lower()
            
            if sure == "yes":
                print("Confirmed player's class")
            elif sure == "no":
                continue
            else:
                print("please type only ","yes or no")

            print("Done selected your class")
            return classs
        else:
            print("Only choose class from list")
classs = CharacterClass()
