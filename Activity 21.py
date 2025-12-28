bird = True
sum = 0

while bird == True:
    tweet = input("Do you want the bird to tweet? ")
    sum += 1
    
    if tweet == 'yes':
        print("Tweet Tweet ")
        continue
    else:
        print("Tweet stops ")
        break
        
print("Count of Tweet is", sum)
    
        
    
