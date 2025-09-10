print("Welcome to MangGodz ")
manga = input("What is your preferred manga you want to read? (action / romance / horror)")
length = input("How long do you want? (short / medium / long)") 
year = input("which year would you like to read? (2000s / 2010s): ")

if manga == 'action':
    if year == '2000s':
        if length == 'short':
            print("This is what I recomend you (Samurai Champloo)")
        elif length == 'medium':
            print("This is what I recomend you (Yu Yu Hakusho)")
        else:
            print("This is what I recomend you (One Piece)")
    if year == '2010s':
        if length == 'short':
            print("This is what I recomend you (Demon Slayer)")
        elif length == 'medium':
            print("This is what I recomend you (HunterxHunter)")
        else:
            print("This is what I recomend you (Soul Eater)")


if manga == 'romance':
    if year == '2000s':
        if length == 'short':
            print("This is what I recomend you (Ouran OC High School)")
        elif length == 'medium':
            print("This is what I recomend you (Fruit Basket)")
        else:
            print("This is what I recomend you (Kimi ni Todoke)")
    if year == '2010s':
        if length == 'short':
            print("This is what I recomend you (My Bunny Girl Senpai)")
        elif length == 'medium':
            print("This is what I recomend you (Ao Haru Ride)")
        else:
            print("This is what I recomend you (A Silent Voice)")


if manga == 'horror':
    if year == '2000s':
        if length == 'short':
            print("This is what I recomend you (I am A Hero)")
        elif length == 'medium':
            print("This is what I recomend you (Uzumaki)")
        else:
            print("This is what I recomend you (Ghost Stories)")
    if year == '2010s':
        if length == 'short':
            print("This is what I recomend you (Made in Abyss)")
        elif length == 'medium':
            print("This is what I recomend you (Attack on Titan)")
        else:
            print("This is what I recomend you (Tokyo Ghoul)")

   

