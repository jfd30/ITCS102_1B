print("Welcome to MangGodz ")
manga = input("What is your recomended manga you want to read?? (action / love / horror)")
length = input("How long do you want? (short / medium / long)") 
year = input("which year would you like to read?? (2000s / 2010s): ")

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
            print("This is what I recomend you (All You Need Is Kill)")
        else:
            print("This is what I recomend you (Bakuman)")


if manga == 'love':
    if year == '2000s':
        if length == 'short':
            print("This is what I recomend you (Nana)")
        elif length == 'medium':
            print("This is what I recomend you (Fruit Basket)")
        else:
            print("This is what I recomend you (Kimi ni Todoke)")
    if year == '2010s':
        if length == 'short':
            print("This is what I recomend you (A Condition Called Love)")
        elif length == 'medium':
            print("This is what I recomend you (Ao Haru Ride)")
        else:
            print("This is what I recomend you (A Silent Voice)")


if manga == 'horror':
    if year == '2000s':
        if length == 'short':
            print("This is what I recomend you (I am A Hero)")
        elif length == 'medium':
            print("This is what I recomend you (When They Cry)")
        else:
            print("This is what I recomend you (The Drifting Classroom)")
    if year == '2010s':
        if length == 'short':
            print("This is what I recomend you (Demi-Human)")
        elif length == 'medium':
            print("This is what I recomend you (Attack on Titan)")
        else:
            print("This is what I recomend you (Tokyo Ghoul)")
   