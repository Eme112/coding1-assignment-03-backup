drinks = ["tea", "coffee", "water"]
chosen_drink = drinks[1]
print(chosen_drink)
print(len(drinks))

# 1. What does each print statement display? Explain why drinks[1] selects that drink.
# Your answer:
# print(chosen_drink) --> "coffee"
#   Reasoning: From the list named 'drinks', the value of item with index=1 is "coffee", which
#              is then stored in the variable 'chosen_drink'. Finally, 'chosen_drink' is printed.
# print(len(drinks)) --> 3
#   Reasoning: The lenght of the list is 3. In this situation, 0-based indexing doesn't matter. 

# 2. What are the Python types of drinks and chosen_drink?
# Your answer: 
# type of 'drinks' --> list (because of the [])
# type of 'chosen_drink' --> string (because of the "")
