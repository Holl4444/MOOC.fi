# Write your solution here
def get_inputs():
    if False:
        recipe_file = input('Recipes file: ')
        search_word = input('Search for: ')
        prep_time = int(input('Prep_time: '))
        ingredient = input('Ingredient: ')
    else:
        recipe_file = 'recipes1.txt'
        search_word = 'cake'
        prep_time = 20
        ingredient = 'eggs'
    return (recipe_file, search_word, prep_time, ingredient)

def get_recipes(filename: str) -> object:
    with open(filename) as recipes:
        lines = [line.strip() for line in recipes]
        recipe_list = {}
        parts = []
        for line in lines:
            if line == '':
                recipe_list[parts[0]] = (int(parts[1]), parts[2:])
                parts = []
            else:
                parts.append(line)
        if parts:
            recipe_list[parts[0]] = (int(parts[1]), parts[2:])
        return recipe_list
    
# def get_recipes(filename: str) -> object:
#     with open(filename) as f:
#         content = f.read().strip()
#     recipe_list = {}
#     for block in content.split('\n\n'):
#         parts = block.strip().split('\n')
#         if len(parts) >= 2:
#             recipe_list[parts[0]] = (int(parts[1]), parts[2:])
#     return recipe_list

def search_by_name(filename: str, word: str) -> list[str]:
    recipes = get_recipes(filename)
    found_recipes = []
    for title in recipes.keys():
        print(title)
        if word.lower() in title.lower():
            found_recipes.append(title)
    return found_recipes

def search_by_time(filename: str, prep_time: int) -> list[str]:
    recipes = get_recipes(filename)
    found_recipes = []
    for title, info in recipes.items():
        if info[0] <= prep_time:
            found_recipes.append(f'{title}, preparation time {info[0]} min')
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipes = get_recipes(filename)
    found_recipes = []
    for title, info in recipes.items():
        if ingredient.lower() in info[1]:
            found_recipes.append(f'{title}, preparation time {info[0]} min')
    return found_recipes

def main():
    f, word, prep, ingredient = get_inputs()
    recipes_with_string = search_by_name(f, word)
    recipes_under_prep_time = search_by_time(f, prep)
    recipes_including_ingredient = search_by_ingredient(f, ingredient)
    print(recipes_including_ingredient)

if __name__ == '__main__':
    main()