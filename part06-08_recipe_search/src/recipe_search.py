# Write your solution here

def process_recipe(recipe):
    recipe_dic = {}
    line_counter = 0
    for line in recipe:
        if line_counter == 0:
            line = line.strip() 
            recipe_dic[line] = {"Ingredients": []}
            recipe_name = line.strip()
            line_counter += 1
        elif line_counter == 1:
            line = line.strip() 
            recipe_dic[recipe_name]['Prep Time'] = int(line)
            line_counter += 1
        elif line == '\n':
            line_counter = 0
            recipe_name = ''
            continue
        else:
            line = line.strip()
            line_counter += 1
            recipe_dic[recipe_name]["Ingredients"].append(line)
    return(recipe_dic)       

def load_file(filename):
    recipe = []
    with open(filename) as f:
        for line in f:
            recipe.append(line)
    dic_recipe = process_recipe(recipe)
    return dic_recipe

def search_by_name(filename, search_term):
    found_recipes = []
    recipe = load_file(filename)

    for key, value in recipe.items():
        if search_term.lower() in key.lower():
            found_recipes.append(key)
    return found_recipes

def search_by_time(filename, search_term):
    found_recipes = []
    recipe = load_file(filename) 
    for key in recipe:
        if recipe[key]["Prep Time"] <= search_term:
            term = key + ', preparation time '+ str(recipe[key]["Prep Time"]) + ' min'
            found_recipes.append(term)
    return found_recipes

def search_by_ingredient(filename, search_term):
    found_recipes = []
    recipe = load_file(filename)
    for key, value in recipe.items():
        # print(key, value['Ingredients'])
        if search_term in value['Ingredients']:
            term = key + ', preparation time '+ str(recipe[key]["Prep Time"]) + ' min'
            found_recipes.append(term)
    return found_recipes






if __name__ == '__main__':
    # found_recipes = search_by_name("recipes1.txt", "cake")
    # for recipe in found_recipes:
    #     print(recipe)

    # found_recipes = search_by_time("recipes1.txt", 20)
    # for recipe in found_recipes:
    #     print(recipe)


    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)