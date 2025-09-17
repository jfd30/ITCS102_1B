temp = input("Input Temperature --> ")
if int(temp.isnumeric()):
    if int(temp) <= 0:
        print("Your temperature is Below Freezing")
    elif int(temp) >=1 and int(temp) <= 15:
        print("Your temperature is Extreme Cold")
    elif int(temp) >= 16 and int(temp) <= 30:
        print("Your temperature is Cold")
    elif int(temp) >= 31 and int(temp) <= 38:
        print("Your Temperature is Lukewarm")
    elif int(temp) >= 39 and int(temp) <= 42:
        print("Your temperature is Warm")
    elif int(temp) >= 43 and int(temp) <= 50:
        print("Your temperature is Hot temp")
    elif int(temp) >= 51 and int(temp) <= 60:
        print("Your temperature is Extremely Hot Temp")
    elif int(temp) >= 61:
        print("Your temperature is Burning Temp")
else:
    print("Invalid Temp")
