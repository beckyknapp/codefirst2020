import requests
import json

#COOL STUFF: json- it massively helped to see it in a user friendly format- can install viewer on browser

import pprint

#COOL STUFF: install pprint- can make things more pretty easily by limiting line return length.

# MUST: have read API documentation - done. Not the easiest!
# MUST: create a function using Edamam API with the ingredient in the search query
# MUST: get the returned recipes based on this ingredient.
# SHOULD: show more than 1 recipe. Default with API was 10! This currently returns three recipes.

def recipe_search(ingredient):

    api_id= '4b0e0436'
    api_key = '63f4824ec631d3247cc281ea6922a025'
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&to=3'.format(ingredient,api_id,api_key)
    result = requests.get(url)

    data = result.json()
    return (data ['hits'])


# MUST: ask user for an ingredient and display details of this search result

# def run():
#     ingredient = input('Enter an ingredient: ')
#     results = recipe_search(ingredient)
#
#     print(results)
#
# run()

# Way too much info.
# Therefore: decided to return JUST the name,url and ingredients of recipes!

# COOL STUFF: inserting a new line!!*** much nicer to read

def output():
    ingredient = input('Welcome to FODMAP Friendly Recipe Search. \r\n  Please enter an ingredient: ')
    results = recipe_search(ingredient)

    pretty = pprint.PrettyPrinter(width=50)


    for item in results:

        print('\r\n')
        pretty.pprint (item['recipe']['label'])
        pretty.pprint (item['recipe']['url'])

        print ('You need the following ingredients: ')
        pretty.pprint (item['recipe']['ingredientLines'])
        print ()

        # SHOULD: Save the results to a file


    with open('recipes.txt', 'w+') as text_file:
        for item in results:
            text_file.write(str(item['recipe']['label'])+ '\r\n' + str(item['recipe']['url']) + '\r\n')



#output()



#COULD: ask more questions to identify more suitable recipes
# mealType- The type of meal a recipe belongs to – lunch, dinner, breakfast *this doesn't work-not many labelled well!**
# Health: “vegan”, “vegetarian” **this does, still not ideal results**


def recipe_search(ingredient, health):

    api_id= '4b0e0436'
    api_key = '63f4824ec631d3247cc281ea6922a025'
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&to=3{}'.format(ingredient,api_id,api_key,health)

    #COOL STUFF: break up with print functions to see what works!
    #print(url)

    result = requests.get(url)

    data = result.json()
    return (data ['hits'])

def print_write(text, file):
    print(text)
    file.write((text) + '\r\n')


def output2():
    ingredient = input('Welcome to FODMAP Friendly Recipe Search. \r\n  Please enter an ingredient: ')
    diet_type = input ('Do you have any other dietary requirements?:\r\n 1=none , 2=vegan, 3=vegetarian: ')

    if diet_type == '1':
        health = str('')
    elif diet_type == '2':
        health = str('&health=vegan')
    elif diet_type == '3':
        health = str('&health=vegetarian')
    else: health = str('')


    #print (mealType)

    results = recipe_search(ingredient, health)

    pretty = pprint.PrettyPrinter(width=50)

    #opening the file in write mode- clears previous one
    file = open('recipes.txt', 'w')

    for item in results:

        # COULD: return FODMAP diet suitable recipes only- "cautions" : [ "FODMAP" ]
        ## cannot exclude on cautions, only ingredients in API

        cautions = (item['recipe']['cautions'])
        if 'FODMAP' in cautions:
            print('\r\n**WARNING: contains FODMAPS, please substitute as necessary.**')
        else:
            print('\r\n**Good news, this recipe is FODMAP friendly.**')

        print_write(item['recipe']['label'],file)
        print_write(item['recipe']['url'],file)

        # print (item['recipe']['label'])
        # file.write (item['recipe']['label']+'\r\n')
        # print (item['recipe']['url'])
        # file.write(item['recipe']['url']+'\r\n')


        print ('You need the following ingredients: ')

        # pretty.pprint (item['recipe']['ingredientLines'])
        #return each item in the list, rather than the array - used function instead of pprint

        ingredient_items = item['recipe']['ingredientLines']
        for ingredient in ingredient_items:
            print (ingredient)

    file.close()


output2()


# COULD/ WON'T:
# after returning recipes, ask user if they want to see others, or start again with a new ingredient ?
#
more = input ('\r\n Would you like to see more recipes for this ingredient (y/n)?: ')
if more =='y':
    print ('\r\n Sorry I have not worked this out yet! Please come back later')

else:
    newsearch = input ('\r\n Would you like to search for recipes with a different ingredient (y/n)?: ')
    if newsearch == 'n':
        print ('\r\n Thank you for using FODMAP Friendly RS.')
    else:
        output2()