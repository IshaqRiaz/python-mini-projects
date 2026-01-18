# List of Italian food items
italian_food = [
    "Pasta Bolognese",
    "Pepperoni pizza",
    "Margherita pizza",
    "Lasagna"
]

# List of Pakistani food items
pakistani_food = [
    "Curry",
    "Chutney",
    "Samosa",
    "Naan"
]

# Function to find a specific meal in the given menu list
def find_meal(name, menu):
    # Make comparison case-insensitive
    for meal in menu:
        if meal.lower() == name.lower():
            return meal
    return None

# Function to select a meal based on food type (Italian or Pakistani)
def select_meal(name, food_type):
    if food_type.lower() == "italian":
        return find_meal(name, italian_food)
    elif food_type.lower() == "pakistani":
        return find_meal(name, pakistani_food)
    else:
        return None

# Function to display available meals based on the food type
def display_available_meals(food_type):
    if food_type.lower() == "italian":
        print("\nAvailable Italian Meals:")
        for meal in italian_food:
            print("-", meal)
    elif food_type.lower() == "pakistani":
        print("\nAvailable Pakistani Meals:")
        for meal in pakistani_food:
            print("-", meal)
    else:
        print("Invalid food type")

# Function to create a summary of the user’s order
def create_summary(name, amount, food_type):
    order = select_meal(name, food_type)
    if order:
        return f"\nYou ordered {amount} {order}(s) from the {food_type.capitalize()} menu."
    else:
        return "\nMeal not found. Please check your spelling."

# ---- Main Program ----
print("Welcome to the Food Order System!")

# Ask user for the type of food they want
type_input = input("Enter the type of food you want to order (Italian/Pakistani): ")

# Display the available meals for that food type
display_available_meals(type_input)

# Ask user for the meal name and quantity
name_input = input("\nEnter the name of the meal you want to order: ")
amount_input = int(input("Enter the quantity you want to order: "))

# Generate and print the final summary
result = create_summary(name_input, amount_input, type_input)
print(result)
