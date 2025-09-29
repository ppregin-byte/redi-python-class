# Alice goes to the store with a bag containing a pen.
Alice_bag= ["pen"]
# Alice buys a notebook and puts it in her bag.
Alice_bag.append("Notebook")
# Alice buys a laptop and puts it in her bag.
Alice_Bag.append("laptop")
# Alice buys a pencil and puts it in her bag.
Alice_Bag.append("pencil")
# On the way home, Alice meets a friend and gives them the pen.
Alice_bag.remove("pen")
# But Alice then hesitate if she has enough room in her bag for another item. She checks.
number_of_itens = len(alice_bag)
print(number_of_itens)
# Alice find the number of items in her bag, and wants to remember if she has a laptop in her bag.
Alice_bag.index("laptop")
if "Laptop" in Alice_bag:
    print("Laptop Found")
else:
    print("Laptop Not Found")
# When Alice gets home, she takes all the items out of her bag and shows them to her family.
    print(Alice_bag)



#append(element) → Adds an element at the end of the list
#count(element) → Returns the number of elements with the specified value
#index(element) → Returns the index of the first element with the specified value
#insert(element) → Adds an element at the specified position
#remove(element) → Removes the first item with the specified value
#reverse() → Reverses the order of the list
#sort() → Sorts the list


#Dictionary methods:
#clear() → Removes all key-value pairs from the dictionary.
#get(key, default=None) → Returns the value for a key, or a default if the key is not found.
#keys() → Returns a list-like view of all keys.
#values() → Returns a list-like view of all values.
#items() → Returns a list-like view of key-value pairs as tuples.
#pop(key, default=None) → Removes and returns the value of a key, or returns default if the key is missing.
#update(dict2) → Adds or updates key-value pairs from another dictionary.


# Game
# We want to store the highests
best_player = ("Alice", 1500, "16.09.2025", "Munich", 5)

# Very soon, the data gets more complex, and it is hard to remember what each value means
# We can use a dictionary instead
best_player = {
  "name": "Alice",
  "score": 1500,
  "date": "16.09.2025",
  "city": "Munich",
  "level": 5
}

# To access a value, we use its key
player_name = best_player["name"] # "Alice"
player_score = best_player["score"] # 1500

# To set an existing key to a new value
best_player["score"] = 1600 # Now the score is 1600

# To add a new key-value pair
best_player["lives"] = 3 # Now the dictionary has a new key "lives" with value 3

Stael Tchinda 20:44
# Some basic rules: 
# - Keys must be unique (no duplicates allowed)
# - Keys must be immutable (strings, numbers, tuples are allowed;) - please rather use strings

# Some useful methods:

# To get safely a value, without risking an error if the key does not exist
player_city = best_player.get("city") # "Munich"
player_country = best_player.get("country") # None, because "country" key does not
player_country_with_default = best_player.get("country", "Germany") # "Germany", the default value

# To get all keys:
player_keys = best_player.keys() # dict_keys(['name', 'score', 'date', 'city', 'level', 'lives'])
# You can use it in a for loop. Otherwise, convert it to a list:
list_of_keys = list(best_player.keys()) # ['name', 'score', 'date', 'city', 'level', 'lives']
# To get all values:
player_scores = {
  "Alice": 1600,
  "Bob": 1200,
  "Charlie": 800
}
player_score_values = player_scores.values() # dict_values([1600, 1200, 800])
# You can use it in a for loop. Otherwise, convert it to a list:
list_of_values = list(player_scores.values()) # [1600, 1200, 800]
# Please rather use values() as a list, only when they all have the same type (e.g. all numbers)

# To get all key-value pairs:
player_items = best_player.items() # dict_items([('name', 'Alice'), ('score', 1600), ('date', '16.09.2025'), ('city', 'Munich'), ('level', 5), ('lives', 3)])
# You can use it in a for loop.
for key, value in best_player.items():
    print(f"{key}: {value}")

# To remove a key-value pair
removed_score = best_player.pop("score") # removed_score is 1600, and the "score" key is removed from the dictionary
# If the key does not exist, it throws a KeyError
removed_non_existing = best_player.pop("non_existing", None) # removed_non_existing is None, no error is thrown
# To update the dictionary with another dictionary
additional_info = {
  "country": "Germany",
  "age": 25
}
best_player.update(additional_info)
# Important: if a key already exists, its value is overwritten
more_info = {
  "age": 26,
  "lives": 4
}
best_player.update(more_info) # Now "age" is 26, and "lives" is 4

# We can have a dictionary of dictionaries.  We call it a nested dictionary
players = {
    "Alice": {"score": 1600, "level": 5},
    "Bob": {"score": 1200, "level": 4},
    "Charlie": {"score": 800, "level": 3},
}

bag_contents = {
    "Alice": ("pen", "notebook", "laptop", "pencil"),
    "Bob": ("book", "laptop"),
    "Charlie": ("notebook", "pencil")
}