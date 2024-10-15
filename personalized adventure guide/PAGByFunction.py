def total_cost(budget, days):
    return budget * days

def get_valid_num(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def plane(name, destination, budget, days):
    '''Format and display the user's name'''
    message = f"Hello, {name.title()}!"
    print(message)

    '''Confirm the destination'''
    print(f"You have elected {destination}.")

    '''Evaluate budget'''
    if budget >= 500:
        print("Luxury")
    elif budget >= 200:
        print("Good")
    else:
        print('Invalid budget.')

    '''Display total cost'''
    total_cost_value = total_cost(budget, days)
    print(f"Total cost for {days} days is: {total_cost_value}")

'''Get user inputs in the specified order'''
name = input("Enter your name: ")
destination = input('Where do you want to go').strip().lower()

budget = get_valid_num('Enter your budget: ')
days = get_valid_num("Enter the number of days: ")

'''Call the travel planner function'''
plane(name, destination, budget, days)