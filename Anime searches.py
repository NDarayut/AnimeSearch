import requests
import os

os.system('cls')

typelist=["tv", "movie", "ova", "special", "ona", "music"]
filterlist=["airing", "upcoming", "bypopularity", "favorite"]

#code for top anime
def topanime():
  print("Type: tv, movie, ova, special, ona, music")
  print("Filter: airing, upcoming, bypopularity, favorite")
  print()
  type = input("Type>   ")
  filter = input("Filter> ")
  if type in typelist and filter in filterlist:            
    top = f"https://api.jikan.moe/v4/top/anime/?type={type}&filter={filter}"
    r = requests.get(top)
    data_top = r.json()
    
    for item in data_top["data"]:
      title = item["title"]
      studios = item["studios"][0]["name"]
      eps = item["episodes"]
      anime_info = f"Title: {title} \nStudios: {studios}     \nEpisodes: {eps}"
      os.system('cls')
      print(anime_info)
    


  
#code for anime rec
def anime_rec():
  recommend = f"https://api.jikan.moe/v4/recommendations/anime"
  r2 = requests.get(recommend)
  data_recommend = r2.json()
  data_recommend["data"]
  recommendation = data_recommend["data"][0]["entry"][0]["title"]
  os.system('cls')
  print(f"Your recommendation is: {recommendation}")

  

  
#asking user
def ask_user():
  print("1) Top 10 anime recommendation \n2) Anime recommendation")
  user_response = input("> ")
  if user_response.isnumeric() and user_response == "1":
    os.system('cls')
    topanime()
  elif user_response == "2":
    os.system('cls')
    anime_rec()
  else:
    ask_user()
  
ask_user()
  






    
    

