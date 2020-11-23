import requests

class MealApi:
    def searchByName(self, name):
        req = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?", {"s": name})
        return req.json()["meals"]
    def searchByMainIngredient(self, ingredient):
        req = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?", {"c": ingredient})
        return req.json()["meals"]
    def searchById(self, id):
        req = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?', {'i': id})
        return req.json()["meals"]
    def returnrandom(self):
        req = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
        return req.json()["meals"]
    def allMealCategories_Ingredients(self):
        req = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?c=list")
        return req.json()["meals"]
