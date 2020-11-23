import unittest
from src.sample.main import MealApi


class MealApiTests(unittest.TestCase):
    def setUp(self):
        self.temp = MealApi()

    def test_searchByName_equal(self):
        result = [{'idMeal': '52940', 'strMeal': 'Brown Stew Chicken', 'strDrinkAlternate': None,
                   'strCategory': 'Chicken', 'strArea': 'Jamaican',
                   'strInstructions': 'Squeeze lime over chicken and rub well. Drain off excess lime juice.\r\nCombine tomato, scallion, onion, garlic, pepper, thyme, pimento and soy sauce in a large bowl with the chicken pieces. Cover and marinate at least one hour.\r\nHeat oil in a dutch pot or large saucepan. Shake off the seasonings as you remove each piece of chicken from the marinade. Reserve the marinade for sauce.\r\nLightly brown the chicken a few pieces at a time in very hot oil. Place browned chicken pieces on a plate to rest while you brown the remaining pieces.\r\nDrain off excess oil and return the chicken to the pan. Pour the marinade over the chicken and add the carrots. Stir and cook over medium heat for 10 minutes.\r\nMix flour and coconut milk and add to stew, stirring constantly. Turn heat down to minimum and cook another 20 minutes or until tender.',
                   'strMealThumb': 'https://www.themealdb.com/images/media/meals/sypxpx1515365095.jpg',
                   'strTags': 'Stew', 'strYoutube': 'https://www.youtube.com/watch?v=_gFB1fkNhXs',
                   'strIngredient1': 'Chicken', 'strIngredient2': 'Tomato', 'strIngredient3': 'Onions',
                   'strIngredient4': 'Garlic Clove', 'strIngredient5': 'Red Pepper', 'strIngredient6': 'Carrots',
                   'strIngredient7': 'Lime', 'strIngredient8': 'Thyme', 'strIngredient9': 'Allspice',
                   'strIngredient10': 'Soy Sauce', 'strIngredient11': 'Cornstarch', 'strIngredient12': 'Coconut Milk',
                   'strIngredient13': 'Vegetable Oil', 'strIngredient14': '', 'strIngredient15': '',
                   'strIngredient16': '', 'strIngredient17': '', 'strIngredient18': '', 'strIngredient19': '',
                   'strIngredient20': '', 'strMeasure1': '1 whole', 'strMeasure2': '1 chopped',
                   'strMeasure3': '2 chopped', 'strMeasure4': '2 chopped', 'strMeasure5': '1 chopped',
                   'strMeasure6': '1 chopped', 'strMeasure7': '1', 'strMeasure8': '2 tsp', 'strMeasure9': '1 tsp ',
                   'strMeasure10': '2 tbs', 'strMeasure11': '2 tsp', 'strMeasure12': '2 cups ', 'strMeasure13': '1 tbs',
                   'strMeasure14': '', 'strMeasure15': '', 'strMeasure16': '', 'strMeasure17': '', 'strMeasure18': '',
                   'strMeasure19': '', 'strMeasure20': '',
                   'strSource': 'http://www.geniuskitchen.com/recipe/authentic-jamaican-brown-stew-chicken-347996',
                   'dateModified': None}]
        self.assertEqual(self.temp.searchByName('Brown Stew Chicken'), result)

    def test_searchByName_notInDb(self):
        self.assertEqual(self.temp.searchByName('wujo'), None)

    def test_allmeal_categories(self):
        result = [{'strCategory': 'Beef'}, {'strCategory': 'Breakfast'}, {'strCategory': 'Chicken'},
                  {'strCategory': 'Dessert'}, {'strCategory': 'Goat'}, {'strCategory': 'Lamb'},
                  {'strCategory': 'Miscellaneous'}, {'strCategory': 'Pasta'}, {'strCategory': 'Pork'},
                  {'strCategory': 'Seafood'}, {'strCategory': 'Side'}, {'strCategory': 'Starter'},
                  {'strCategory': 'Vegan'}, {'strCategory': 'Vegetarian'}]
        self.assertEqual(self.temp.allMealCategories_Ingredients(), result)

    def test_return_random(self):
        self.assertEqual(type(self.temp.returnrandom()), list)

    def test_searchById(self):
        result = [{'idMeal': '52772', 'strMeal': 'Teriyaki Chicken Casserole', 'strDrinkAlternate': None, 'strCategory': 'Chicken', 'strArea': 'Japanese', 'strInstructions': 'Preheat oven to 350° F. Spray a 9x13-inch baking pan with non-stick spray.\r\nCombine soy sauce, ½ cup water, brown sugar, ginger and garlic in a small saucepan and cover. Bring to a boil over medium heat. Remove lid and cook for one minute once boiling.\r\nMeanwhile, stir together the corn starch and 2 tablespoons of water in a separate dish until smooth. Once sauce is boiling, add mixture to the saucepan and stir to combine. Cook until the sauce starts to thicken then remove from heat.\r\nPlace the chicken breasts in the prepared pan. Pour one cup of the sauce over top of chicken. Place chicken in oven and bake 35 minutes or until cooked through. Remove from oven and shred chicken in the dish using two forks.\r\n*Meanwhile, steam or cook the vegetables according to package directions.\r\nAdd the cooked vegetables and rice to the casserole dish with the chicken. Add most of the remaining sauce, reserving a bit to drizzle over the top when serving. Gently toss everything together in the casserole dish until combined. Return to oven and cook 15 minutes. Remove from oven and let stand 5 minutes before serving. Drizzle each serving with remaining sauce. Enjoy!', 'strMealThumb': 'https://www.themealdb.com/images/media/meals/wvpsxx1468256321.jpg', 'strTags': 'Meat,Casserole', 'strYoutube': 'https://www.youtube.com/watch?v=4aZr5hZXP_s', 'strIngredient1': 'soy sauce', 'strIngredient2': 'water', 'strIngredient3': 'brown sugar', 'strIngredient4': 'ground ginger', 'strIngredient5': 'minced garlic', 'strIngredient6': 'cornstarch', 'strIngredient7': 'chicken breasts', 'strIngredient8': 'stir-fry vegetables', 'strIngredient9': 'brown rice', 'strIngredient10': '', 'strIngredient11': '', 'strIngredient12': '', 'strIngredient13': '', 'strIngredient14': '', 'strIngredient15': '', 'strIngredient16': None, 'strIngredient17': None, 'strIngredient18': None, 'strIngredient19': None, 'strIngredient20': None, 'strMeasure1': '3/4 cup', 'strMeasure2': '1/2 cup', 'strMeasure3': '1/4 cup', 'strMeasure4': '1/2 teaspoon', 'strMeasure5': '1/2 teaspoon', 'strMeasure6': '4 Tablespoons', 'strMeasure7': '2', 'strMeasure8': '1 (12 oz.)', 'strMeasure9': '3 cups', 'strMeasure10': '', 'strMeasure11': '', 'strMeasure12': '', 'strMeasure13': '', 'strMeasure14': '', 'strMeasure15': '', 'strMeasure16': None, 'strMeasure17': None, 'strMeasure18': None, 'strMeasure19': None, 'strMeasure20': None, 'strSource': None, 'dateModified': None}]

        self.assertEqual(self.temp.searchById(52772), result)

    def test_searchById_None(self):
        self.assertEqual(self.temp.searchById(0), None)

    def test_searchByMainIngredient(self):
        result = {'strMeal': 'Brown Stew Chicken',
                   'strMealThumb': 'https://www.themealdb.com/images/media/meals/sypxpx1515365095.jpg',
                   'idMeal': '52940'}

        self.assertEqual(self.temp.searchByMainIngredient('Chicken')[0], result)
    def test_searchByMainIngredient_Error(self):
        self.assertEqual(self.temp.searchByMainIngredient('wwww'), None)

'''
print(temp.searchById(52772))
print(temp.searchByMainIngredient("chicken"))
print(temp.allMealCategories_Ingredients())
print(temp.searchByName('Brown Stew Chicken'))
print(type(temp.returnrandom()))
'''
