# Name: Quang Le
# Student ID: 1768324

class FoodItem:

    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

name = input()
fat = float(input())
carbs = float(input())
protein = float(input())
num_serv = float(input())

food_format = FoodItem()
food_format.print_info()
print('Number of calories for {:.2f} serving(s): 0.00\n'.format(num_serv))

food_item = FoodItem(name, fat, carbs, protein)
calories = food_item.get_calories(num_serv)

food_item.print_info()
print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_serv, calories))
