import itertools
import csv

def lottery_combinations(balls_drawn, total_balls, special_balls_drawn, total_special_balls):
    """Determines all possible lottery number combinations.  Normal balls are pulled from
one pool of numbers and special balls (mega ball, power ball, etc.) are pulled from another.
For example, for a normal ball if the number 4 is drawn it is removed from the pool of numbers
and another number 4 cannot be drawn.  Unaware of lotteries that have more than one special ball,
all special balls are pulled from the same pool in this code which could cause issues if the rules
for the lottery are different."""
    combinations = []
    for balls in itertools.combinations(range(1, total_balls + 1), balls_drawn):
        balls = list(balls)
        for specialball in itertools.combinations(range(1, total_special_balls + 1), special_balls_drawn):
            specialball = list(specialball)

            combinations.append(list(balls + specialball))
    return combinations

def lottery_stats(combinations, ticket_cost):
    """Prints stats related to the combinations based on the user input of the lottery_combinations function."""
    print()
    print(f'There are {len(combinations)} different combinations of numbers in this lottery')
    print()
    print(f'At {ticket_cost} per ticket, to buy every combination of numbers, it would')
    print(f'cost {len(combinations) * ticket_cost}.')
    print()
    print(f'Assuming you were the only jackpot winner, anything you won over the amount of')
    print(f'the cost of buying the tickets would be profit.')
    print()
    

def combinations_to_csv(balls_drawn, special_balls_drawn, combinations):
    """Writes all of the possible lottery combinations to a csv file."""
    header = []
    for ball in range(1, balls_drawn + 1):
        header.append('Ball ' + str(ball))
    for special_ball in range(1, special_balls_drawn + 1):
        header.append('Special Ball ' + str(special_ball))

    with open('lottery-combinations.csv', 'w', newline='') as data:
        writer = csv.writer(data)
        writer.writerow(header)
        writer.writerows(combinations)
        
                                  

if __name__ == "__main__":
    balls_drawn = int(input('How many balls are drawn in this lottery? '))
    total_balls = int(input('How many total balls are in the pool? '))
    special_balls_drawn = int(input('How many special balls are drawn (mega ball, power ball, etc)? '))
    total_special_balls = int(input('How many special balls are in the pool? '))
    ticket_cost = float(input('How much does each ticket cost? '))

    #TEST INPUTS - COMMENT OUT INPUT LINES ABOVE FOR TESTING SO THEY DON'T HAVE TO BE ENTERED EACH TIME
    #balls_drawn = 3
    #total_balls = 10
    #special_balls_drawn = 1
    #total_special_balls = 10
    #ticket_cost = 2

    combinations = lottery_combinations(balls_drawn, total_balls, special_balls_drawn, total_special_balls)
    lottery_stats(combinations, ticket_cost)
    
    export_choice = input('Do you want to export the lottery combinations to CSV? (Enter y for yes or n for no) ').casefold()

    if export_choice == 'y':
    
        combinations_to_csv(balls_drawn, special_balls_drawn, combinations)
        print('Lottery combinations have been saved as lottery-combinations.csv')

    
