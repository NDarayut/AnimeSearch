import requests




#code for top anime
def topanime():
  print("Type: tv, movie, ova, special, ona, music")
  print("Filter: airing, upcoming, bypopularity, favorite")
  print()
  type = input("Type>   ")
  filter = input("Filter> ")
  top = f"https://api.jikan.moe/v4/top/anime/?type={type}&filter={filter}"
  r = requests.get(top)
  data_top = r.json()
  
  for item in data_top["data"]:
    title = item["title"]
    studios = item["studios"][0]["name"]
    eps = item["episodes"]
    anime_info = f"Title: {title} \nStudios: {studios}\nEpisodes: {eps}"
    print()
    print(anime_info)
  


  
#code for anime rec
def anime_rec():
  recommend = f"https://api.jikan.moe/v4/recommendations/anime"
  r2 = requests.get(recommend)
  data_recommend = r2.json()
  data_recommend["data"]
  recommendation = data_recommend["data"][0]["entry"][0]["title"]
  print(f"Your recommendation is: {recommendation}")

  

  
#asking user
def ask_user():
  print("1) Top anime recommendation \n2) Anime recommendation")
  user_response = float(input("> "))
  if user_response == 1:
    print()
    topanime()
  elif user_response == 2:
    print()
    anime_rec()
  else:
    ask_user()
  
ask_user()
  






    
    

