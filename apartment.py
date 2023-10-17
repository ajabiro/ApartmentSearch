# -Write a function named apt_search1. It takes a city parameter (string), a max_rent parameter (int),
#  a min_beds parameter (int), and a pets_allowed parameter (boolean).

def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        print(f"Welcome to GC Property Management! Looking up listings in {city} "
              f"for {min_beds} bedroom apartments that allows pets, "
              f"all within a budget of $ {max_rent} per month...")
    else:
        print(f"Welcome to GC Property Management! Looking up listings in {city} for "
              f"{min_beds} bedroom apartments,all within a budget of $ {max_rent} per month...")


apt_search1("Flint", 1000, 2, False)


# -Write a function named apt_search2. It takes the same parameters as last time,
# but with this one, make min_beds and pets_allowed optional by providing some default values for those.

def apt_search2(city, max_rent, min_beds=3, pets_allowed=False):
    if pets_allowed:
        print(f"Welcome to GC Property Management! Looking up listings in {city} "
              f"for {min_beds} bedroom apartments that allows pets, "
              f"all within a budget of $ {max_rent} per month...")
    else:
        print(f"Welcome to GC Property Management! Looking up listings in {city} for "
              f"{min_beds} bedroom apartments,all within a budget of $ {max_rent} per month...")


# Call this function once with arguments for min_beds and pets_allowed both omitted.
apt_search2("Fenton", 1700)
# Then call it with just min_beds and no pets_allowed
apt_search2("Detroit",2000, 4)
# Now call it with just pets_allowed and not min_beds (You’ll want to use named arguments for this one).
apt_search2(city="Detroit", max_rent=2000, pets_allowed=True)

# Write a lambda function that adds 100 to any given number
plus_one_hundred = lambda x: x + 100
print(plus_one_hundred(30))

# Write a lambda function that squares any given number
square_num = lambda x: x * x
print(square_num(4))

# Write a lambda function that concatenates “- “ before any string
concatenate = lambda x: "- " + x
print(concatenate("Hello"))

# Write a lambda function that divides any number by 3
divide_by_three = lambda x: x / 3
print(divide_by_three(9))
