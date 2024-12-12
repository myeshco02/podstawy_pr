#popular games
computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
#function that sorts array alphabetically
computer_games.sort()
index = 1 #defining index to numerize each item
i=0 #defining i to start while loop from 0 

while i < len(computer_games):
    print(f"{index}. {computer_games[i]} ")
    index+=1
    i+=1
