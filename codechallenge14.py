list = []

print("Pick Your Anime List")
while True:
    anime = input("Enter Anime Title (Type 'exit' to stop): ")
    if anime.lower()== 'exit':
        print("End")
        break
    list.append(anime)

num = len(list)
print("Your List Contains:")
for i in range(1,num+1,1):
    print(f'- {list[i-1]}')
print("You know ball dawg")
