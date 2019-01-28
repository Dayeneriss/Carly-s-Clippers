'''L'objectif de ce projet est d'aider une entreprise (un salon de coiffure) à planifier son fonctionnement pour le reste du mois. Pour ce faire, nous parcourons les listes de données collectées au cours des deux dernières semaines et calculons quelques paramètres importants.

#Voici trois listes:
hairstyles: les noms des coupes offertes chez Carly's Clippers
prices: le prix de chaque coiffure dans la hairstylesliste
last_week: le nombre de chaque coiffure hairstylesqui a été acheté la semaine dernière.'''
  
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price = total_price + price
  
  average_price = total_price/ len(prices)
  print("total_price: "+ str(average_price))
  
  new_prices = [price - 5 for price in prices]
  print(new_prices)
  
  total_revenue = 0
  
  for i in range(len(hairstyles)):
    total_revenue = prices[i] * last_week[i]
    print("Total revenue: " + str(total_revenue))
    
    average_daily_revenue = total_revenue/7
    
    print(average_daily_revenue)
    
    cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles[1])) if new_prices[i]<30]
    print(cuts_under_30)
  
  
