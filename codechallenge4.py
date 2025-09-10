print("Welcome to MangGodz ")
manga = input("What is your preferred manga you want to read? (action / romance / horror)")
length = input("How long do you want? (short / medium / long)") 
year = input("which year would you like to read? (2000s / 2010s): ")

if manga == 'action':
    if year == '2000s':
        if length == 'short':
            print("This is what I recommend you (Samurai Champloo)")
        elif length == 'medium':
            print("This is what I recommend you (Yu Yu Hakusho)")
        else:
            print("This is what I recommend you (One Piece)")
    if year == '2010s':
        if length == 'short':
            print("This is what I recommend you (Demon Slayer)")
        elif length == 'medium':
            print("This is what I recommend you (HunterxHunter)")
        else:
            print("This is what I recommend you (Soul Eater)")


if manga == 'romance':
    if year == '2000s':
        if length == 'short':
            print("This is what I recommend you (Ouran OC High School)")
        elif length == 'medium':
            print("This is what I recommend you (Fruit Basket)")
        else:
            print("This is what I recommend you (Kimi ni Todoke)")
    if year == '2010s':
        if length == 'short':
            print("This is what I recommend you (My Bunny Girl Senpai)")
        elif length == 'medium':
            print("This is what I recommend you (Ao Haru Ride)")
        else:
            print("This is what I recommend you (A Silent Voice)")


if manga == 'horror':
    if year == '2000s':
        if length == 'short':
            print("This is what I recommend you (I am A Hero)")
        elif length == 'medium':
            print("This is what I recommend you (Uzumaki)")
        else:
            print("This is what I recommend you (Ghost Stories)")
    if year == '2010s':
        if length == 'short':
            print("This is what I recommend you (Made in Abyss)")
        elif length == 'medium':
            print("This is what I recommend you (Attack on Titan)")
        else:
            print("This is what I recommend you (Tokyo Ghoul)")

   


