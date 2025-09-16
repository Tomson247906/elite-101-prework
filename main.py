
#This is a simple chatbot that helps users find recipes and cook food
#The chatbot will ask the user for their name and age to personalize the experience
print("hello im a food chat bot. My goal is to help you find recipes and cook food to find something that you might love.")
name = input("what is your name:")
age = int(input("hello welcome "+ name + ",how old are you:"))

#The reason for this if statement is to help the user get more personalized experience
#example if ther user is under 18 you can assume that they harderly cook and you can give them easier recipes
#but if they are over 18 you can assume that they cook more often and you can give them more complex recipes
if 18 <= age <= 24:
    school = input("do you go to collage high school?:")
    print("hi there young adult, hope you find something you like")
elif age > 25:
    print("hi there adult, hope you find something you like")
else:
    print("hi there young cook, hope you find something you like")

#The chatbot will ask the user for their food preferences to help them find recipes that they might like
print("to help me find recipes that you might like, please answer the following questions:")
cuisine = input("what type of cuisine do you like? (e.g. Italian, Chinese, Mexican):")
meal_type = input("what type of meal are you looking for? (e.g. breakfast, lunch, dinner, dessert):")
dietary_restrictions = input("do you have any dietary restrictions? (e.g. vegetarian, vegan, gluten-free):")

#The chatbot will ask the user for their cooking skill level to help them find recipes that are appropriate for their skill level
cooking_skill = input("what is your cooking skill level? (e.g. beginner, intermediate, advanced):")
